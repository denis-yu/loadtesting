HOST = 'https://qa.api.healthinsurance.com'
#HOST = 'https://staging.medicare.healthinsurance.com'

CREDENTIALS = {
    'USR': 'qabo',
    'EMAIL': 'qa@healthpocket.com',
    'PWORD': 'DSJFVSQE9u-D9rlwD8YYh'
    #PWORD = "JcVPzmypOat2y4gIpn_GZ"
}

ENDPOINT_URL = {
    'AUTH': '/auth/login',
    'AFFILIATE': '/affiliate',
    'DISCLAIMERS': '/product/disclaimers',
    'ZIP': '/zip',
    'MEDICARE': '/medicare/v2/',
    'MEDICARE_PLANS': '/medicare/v2/plans',
    'MEDICARE_PROFILE': '/medicare/v2/profile',
    'MEDICARE_PROFILE_NEWID': '/medicare/v2/profile/newId',
    'Get_Doc': '/doc'
}

FILES = {
    'ZIP_CODES_CSV': 'src/data/zip_codes.csv'
}