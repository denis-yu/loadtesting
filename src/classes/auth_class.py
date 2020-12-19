import json
from locust import SequentialTaskSet, task

@task()
class auth_class(SequentialTaskSet):

    @task()
    def login(self, end_point, headers, json):
        response= self.client.post(end_point, headers=headers, json=json)
        return(response.json())
    
    @task()
    def stop(self):
        self.interrupt()