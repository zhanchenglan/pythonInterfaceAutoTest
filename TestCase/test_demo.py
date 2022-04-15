"""

@author:f2849440

@Description:搭建环境demo

@file:test_demo.py

@time:2021/08/16

"""
import json
import os

import allure
import pytest
import requests
from jsonpath import jsonpath

@allure.epic("我的测试报告")
@allure.feature("环境搭建")
@allure.severity(allure.severity_level.TRIVIAL)
class TestDemo(object):

    @allure.story("用例1")
    @allure.description("demo1")
    def test_demo1(self):
        url = "https://mi-api-test.sunvalleycloud.com/oauth/login?&timeStamp=20201010112513&lang=en"

        params = {

            "auth_type": "email_password",

            "auto": False,

            "client_id": "0778a347853545c08d496566e0d0180c",

            "client_secret": "a0b5ca0e003a398fc4793514b0b3f754",

            "device_name": "HUAWEI EVA-AL10",

            "email": "100020@hyhpzengweifang.com.cn",

            "grant_type": "password",

            "imei": "a000006d937c5f",

            "password": "2868fc65d8ee171b213488ab47a5b36e",

            "product_line_id": "4f975dc1a43d4117a6f3eb83b2cbc778",

            "scope": "all"

        }

        headers = {'content-type': "application/json"}

        r = requests.post(url, data=json.dumps(params), headers=headers)

        d = json.loads(r.text)

        print(r.json())

        print(r.json()["data"]["access_token"])

        dict_type = r.json()

        print(type(dict_type))

        access_token = jsonpath(dict_type, '$..access_token')

        print(access_token[0])


if __name__ == '__main__':
    pytest.main(["test_demo.py", '--alluredir', './reports'])
    os.system('allure generate ./reports/ -o ./reports/html --clean')
