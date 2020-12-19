import json
from locust import SequentialTaskSet, task

@task()
class product_class(SequentialTaskSet):

    def post_disclaimer(self, end_point, headers, json):
        response = self.client.post(end_point, name='post_disclaimer', headers=headers, json=json)
        return (response)