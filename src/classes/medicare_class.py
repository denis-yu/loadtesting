import json
from locust import SequentialTaskSet, task

@task()
class medicare_class(SequentialTaskSet):

    def get_profile_newId(self, end_point, headers):
        response = self.client.get(end_point, name='get_profile_newId', headers=headers)
        return (response)
    
    def put_profile_profileId(self, end_point, headers, json):
        response = self.client.put(end_point, name='put_profile_profileId', headers=headers, json=json)
        return (response)
    
    def get_plans_profileId(self, end_point, headers):
        response = self.client.get(end_point, name='get_plans_profileId', headers=headers)
        return (response)

    def get_medicare_id(self, end_point, headers):
        response = self.client.get(end_point, name='get_medicare_Id', headers=headers)
        return (response)