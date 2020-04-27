import unittest

from api.login import LoginApi
import logging
import utils
import app
from parameterized import parameterized
import json


# 构建测试数据，读取JSON文件
# [(), (), ()]
def build_data():
    test_data = []
    with open(app.BASE_DIR + "/data/login.json", encoding="UTF-8") as f:
        json_data = json.load(f)
        for case_data in json_data:
            mobile = case_data.get("mobile")
            password = case_data.get("password")
            status_code = case_data.get("status_code")
            success = case_data.get("success")
            code = case_data.get("code")
            message = case_data.get("message")
            test_data.append((mobile, password, status_code, success, code, message))
    logging.info("test_data={}".format(test_data))
    return test_data


class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.login_api = LoginApi()

    # 登录
    @parameterized.expand(build_data)
    def test_login(self, mobile, password, status_code, success, code, message):
        logging.info("param mobile={} password={} status_code={} success={} code={} message={}"
                     .format(mobile, password, status_code, success, code, message))
        # 定义测试数据
        # mobile = "13800000002"
        # password = "123456"

        response = self.login_api.login(mobile, password)
        result = response.json()
        logging.info("login response data={}".format(result))

        # 断言
        utils.common_assert(self, response, status_code, success, code, message)
        # utils.common_assert(self, response)

        # self.assertEqual(200, response.status_code)
        # self.assertTrue(result.get("success"))
        # self.assertEqual(10000, result.get("code"))
        # self.assertIn("操作成功", result.get("message"))

        if success:
            # 获取token数据，并保存
            app.TOKEN = "Bearer " + result.get("data")
            app.headers_data["Authorization"] = app.TOKEN
            logging.info("token={}".format(app.TOKEN))
            logging.info("headers={}".format(app.headers_data))

    # 登录成功
    # @unittest.skip("废弃")
    def test_login_success(self):
        # 定义测试数据
        mobile = "13800000002"
        password = "123456"

        response = self.login_api.login(mobile, password)
        result = response.json()
        logging.info("login response data={}".format(result))

        # 断言
        utils.common_assert(self, response, 200, True, 10000, "操作成功")
        # utils.common_assert(self, response)

        # self.assertEqual(200, response.status_code)
        # self.assertTrue(result.get("success"))
        # self.assertEqual(10000, result.get("code"))
        # self.assertIn("操作成功", result.get("message"))

        # 获取token数据，并保存
        app.TOKEN = "Bearer " + result.get("data")
        app.headers_data["Authorization"] = app.TOKEN
        logging.info("token={}".format(app.TOKEN))
        logging.info("headers={}".format(app.headers_data))

    # 用户名不存在
    @unittest.skip("废弃")
    def test_login_username_is_not_exist(self):
        # 定义测试数据
        mobile = "13888889999"
        password = "123456"

        response = self.login_api.login(mobile, password)
        result = response.json()
        logging.info("login response data={}".format(result))

        # 断言
        utils.common_assert(self, response, 200, False, 20001, "用户名或密码错误")

        # self.assertEqual(200, response.status_code)
        # self.assertFalse(result.get("success"))
        # self.assertEqual(20001, result.get("code"))
        # self.assertIn("用户名或密码错误", result.get("message"))

    # 密码错误
    @unittest.skip("废弃")
    def test_login_pwd_is_error(self):
        # 定义测试数据
        mobile = "13800000002"
        password = "error"

        response = self.login_api.login(mobile, password)
        result = response.json()
        logging.info("login response data={}".format(result))

        # 断言
        utils.common_assert(self, response, 200, False, 20001, "用户名或密码错误")

        # self.assertEqual(200, response.status_code)
        # self.assertFalse(result.get("success"))
        # self.assertEqual(20001, result.get("code"))
        # self.assertIn("用户名或密码错误", result.get("message"))

    # 请求参数为空
    @unittest.skip("废弃")
    def test_login_req_param_is_null(self):
        # 定义测试数据
        mobile = None
        password = None

        response = self.login_api.login(mobile, password)
        result = response.json()
        logging.info("login response data={}".format(result))

        # 断言
        utils.common_assert(self, response, 200, False, 99999, "系统繁忙")

    # 用户名为空
    @unittest.skip("废弃")
    def test_login_username_is_empty(self):
        # 定义测试数据
        mobile = ""
        password = "123456"

        response = self.login_api.login(mobile, password)
        result = response.json()
        logging.info("login response data={}".format(result))

        # 断言
        utils.common_assert(self, response, 200, False, 20001, "用户名或密码错误")

    # 密码为空
    @unittest.skip("废弃")
    def test_login_pwd_is_empty(self):
        # 定义测试数据
        mobile = "13800000002"
        password = ""

        response = self.login_api.login(mobile, password)
        result = response.json()
        logging.info("login response data={}".format(result))

        # 断言
        utils.common_assert(self, response, 200, False, 20001, "用户名或密码错误")
