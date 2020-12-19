import json
from locust import SequentialTaskSet, task

@task()
class zip_code_location_class(SequentialTaskSet):

    def get_zip_zipId_counties(self, end_point, headers):
        response = self.client.get(end_point, name='get_zip_zipId_counties', headers=headers)
        return (response)

    def get_zip_id(self, end_point, headers):
        response = self.client.get(end_point, name='get_zip_Id', headers=headers)
        return (response)