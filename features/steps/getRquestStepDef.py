import requests
from behave import *
import json


global response

base_Url = "https://reqres.in"


@given(u'user sets baseUrl')
def step_impl(context):
    url = "https://reqres.in"

@when(u'user sends get request')
def step_impl(context):
    context.response = requests.get(base_Url + "/api/users?page=2")


@then(u'user gets status code 200')
def step_impl(context):
    print(context.response.status_code)
    expected_status_code = 200
    assert expected_status_code == context.response.status_code

    @when(u'user sends get request for a specific user')
    def step_impl(context):
        context.response = requests.get(base_Url + "/api/users/2")


@then(u'user gets a response body with requested details')
def step_impl(context):
    print(context.response.json())
    expected_body = {"data": {"id": 2, "email": "janet.weaver@reqres.in", "first_name": "Janet", "last_name": "Weaver",
                              "avatar": "https://reqres.in/img/faces/2-image.jpg"}, "support": {
        "url": "https://reqres.in/#support-heading",
        "text": "To keep ReqRes free, contributions towards server costs are appreciated!"}}

    assert expected_body == context.response.json()
