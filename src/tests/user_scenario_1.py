import datetime
import json
from locust import HttpUser, task, between, SequentialTaskSet
from src.config_env import HOST, CREDENTIALS, ENDPOINT_URL, FILES
from src.classes import auth_class, product_class, medicare_class, zip_code_location_class
from src.common_functions import read_csv

#This class mimic the scenario 1
@task()
class user_scenario_1(SequentialTaskSet):

    headers = {}
    counties_data = {}
    profile = {}
    access_token = ''
    zipId = ''
    profileId = ''
    

    #This method logins to the api and gets a JWT to use in all the subsequent calls.
    def on_start(self):
        self.headers['Accept'] = 'application/json'
        json = {'email':CREDENTIALS['EMAIL'], 'password':CREDENTIALS['PWORD']}
        auth_obj = auth_class.auth_class(self.parent)
        data = auth_obj.login(ENDPOINT_URL['AUTH'], self.headers, json)
        self.access_token = data['access_token']
        self.headers['Authorization']= 'Bearer ' + self.access_token

    #This method calls the disclaimers for all states
    @task()
    def post_disclaimer(self):
        json = {'productLine':'medicare', 'pageType':'census', 'carriers':[], 'state':'ALL'}
        product_obj = product_class.product_class(self.parent)
        response = product_obj.post_disclaimer(ENDPOINT_URL['DISCLAIMERS'], self.headers, json)
        #data = response.json()
        #print ('========POST DISCLAIMER' + str(data))

    #This method gets a new profile
    @task()
    def get_profile_newId(self):
        medicare_obj = medicare_class.medicare_class(self.parent)
        response = medicare_obj.get_profile_newId(ENDPOINT_URL['MEDICARE_PROFILE_NEWID'], self.headers)
        data = json.loads (response.text)
        self.profileId = data['profileId']
        #print ('========GET PROFILE NEW ID' + data['profileId'])

    #This method gets the counties based on a given random zip code
    @task()
    def get_zip_zipId_counties(self):
        zip_code_location_obj = zip_code_location_class.zip_code_location_class(self.parent)
        self.zipId = str(read_csv(FILES['ZIP_CODES_CSV']))
        uri = ENDPOINT_URL['ZIP'] + f'/{self.zipId}/counties'
        response = zip_code_location_obj.get_zip_zipId_counties(uri, self.headers)
        self.counties_data = response.json()
        self.counties_data= self.counties_data[0]
        #print('===========GET ZIP ZIPID COUNTIES ')
        #print(self.counties_data)

    
    #This method set a profile for the vuser. 
    #Note that this method must be executed after get_profile_new_id since it will set the profileId
    @task()
    def put_profile_profileId(self):
        location = {}
        census = {}
        today = datetime.datetime.today()
        year = today.year + 1
        member = {'role':'P', 'gender':'M', 'smoker':False, 'dob':'1955-11-10'}
        self.profile['profileId'] = self.profileId
        self.profile['drugs'] = []
        self.profile['preferredPharmacyType'] = 'RETAIL'
        location['county']=self.counties_data['county']
        location['fips']=self.counties_data['fips']
        location['state']=self.counties_data['state']
        location['_id']=self.counties_data['_id']
        location['fullCodeList']=self.counties_data['fullCodeList']
        location['code']=self.counties_data['code']
        location['maRegionCode']=self.counties_data['maRegionCode']
        location['pdpRegionCode']=self.counties_data['pdpRegionCode']
        location['ifpRegionCode']=self.counties_data['ifpRegionCode']
        location['zip'] = self.zipId
        census['location']  = location
        census['year'] = str(year)
        census['member'] = member
        self.profile['census'] = census
        medicare_obj = medicare_class.medicare_class(self.parent)
        uri= ENDPOINT_URL['MEDICARE_PROFILE'] + f'/{self.profileId}'
        response = medicare_obj.put_profile_profileId(uri, self.headers, self.profile)
        #print('===========put_profile_profileId')
        #print (response.text)

    #This method gets the plans based on the vuser profile.
    @task()
    def get_plans_profileId(self):
        medicare_obj = medicare_class.medicare_class(self.parent)
        uri = ENDPOINT_URL['MEDICARE_PLANS'] + f'/{self.profileId}'
        response = medicare_obj.get_plans_profileId(uri, self.headers)
        #print ('================= PLANS!!!    ')
        #print (response.text)

#This class sets the parameters for Locust to run
class spawn(HttpUser):
    wait_time = between(5,10)
    host = HOST
    tasks = [user_scenario_1]