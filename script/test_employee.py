import unittest

from api.employee import EmployeeApi
import logging
import utils
from parameterized import parameterized
import json
import app


# 构建添加员工的测试数据
def build_add_emp_data():
    test_data = []
    with open(app.BASE_DIR + "/data/employee.json", encoding="UTF-8") as f:
        json_data = json.load(f)
        case_data = json_data.get("test01_add_emp")
        username = case_data.get("username")
        mobile = case_data.get("mobile")
        status_code = case_data.get("status_code")
        success = case_data.get("success")
        code = case_data.get("code")
        message = case_data.get("message")
        test_data.append((username, mobile, status_code, success, code, message))
    logging.info("build_add_emp_data={}".format(test_data))
    return test_data


# 构建查询员工的测试数据
def build_query_emp_data():
    test_data = []
    with open(app.BASE_DIR + "/data/employee.json", encoding="UTF-8") as f:
        json_data = json.load(f)
        case_data = json_data.get("test02_query_emp")
        status_code = case_data.get("status_code")
        success = case_data.get("success")
        code = case_data.get("code")
        message = case_data.get("message")
        test_data.append((status_code, success, code, message))
    logging.info("build_query_emp_data={}".format(test_data))
    return test_data


# 构建修改员工的测试数据
def build_update_emp_data():
    test_data = []
    with open(app.BASE_DIR + "/data/employee.json", encoding="UTF-8") as f:
        json_data = json.load(f)
        case_data = json_data.get("test03_update_emp")
        username = case_data.get("username")
        status_code = case_data.get("status_code")
        success = case_data.get("success")
        code = case_data.get("code")
        message = case_data.get("message")
        test_data.append((username, status_code, success, code, message))
    logging.info("build_update_emp_data={}".format(test_data))
    return test_data


# 构建删除员工的测试数据
def build_delete_emp_data():
    test_data = []
    with open(app.BASE_DIR + "/data/employee.json", encoding="UTF-8") as f:
        json_data = json.load(f)
        case_data = json_data.get("test04_delete_emp")
        status_code = case_data.get("status_code")
        success = case_data.get("success")
        code = case_data.get("code")
        message = case_data.get("message")
        test_data.append((status_code, success, code, message))
    logging.info("build_delete_emp_data={}".format(test_data))
    return test_data


class TestEmployee(unittest.TestCase):
    employee_id = "1161494952529903616"  # 保存员工id

    @classmethod
    def setUpClass(cls):
        cls.employee_api = EmployeeApi()

    # 添加员工
    @parameterized.expand(build_add_emp_data)
    def test01_add_emp(self, username, mobile, status_code, success, code, message):
        # 测试数据
        # username = "tom999"
        # mobile = "13012340999"

        # 调用接口
        response = self.employee_api.add_emp(username, mobile)
        result = response.json()
        logging.info("add emp data={}".format(result))

        # 断言
        utils.common_assert(self, response, status_code, success, code, message)

        # 保存员工id
        TestEmployee.employee_id = result.get("data").get("id")

    # 查询员工
    @parameterized.expand(build_query_emp_data)
    def test02_query_emp(self, status_code, success, code, message):
        # 测试数据
        emp_id = TestEmployee.employee_id

        # 调用接口
        response = self.employee_api.query_emp(emp_id)
        result = response.json()
        logging.info("query emp data={}".format(result))

        # 断言
        utils.common_assert(self, response, status_code, success, code, message)

    # 修改员工
    @parameterized.expand(build_update_emp_data)
    def test03_update_emp(self, username, status_code, success, code, message):
        # 测试数据
        emp_id = TestEmployee.employee_id
        # username = "tom999-new"

        # 调用接口
        response = self.employee_api.update_emp(emp_id, username)
        result = response.json()
        logging.info("update emp data={}".format(result))

        # 断言
        utils.common_assert(self, response, status_code, success, code, message)

    # 删除员工
    @parameterized.expand(build_delete_emp_data)
    def test04_delete_emp(self, status_code, success, code, message):
        # 测试数据
        emp_id = TestEmployee.employee_id

        # 调用接口
        response = self.employee_api.delete_emp(emp_id)
        result = response.json()
        logging.info("delete emp data={}".format(result))

        # 断言
        utils.common_assert(self, response, status_code, success, code, message)
