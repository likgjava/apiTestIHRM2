import app
import requests


class EmployeeApi:
    def __init__(self):
        self.add_emp_url = app.BASE_URL + "/api/sys/user"
        self.query_emp_url = app.BASE_URL + "/api/sys/user/{}"
        self.update_emp_url = app.BASE_URL + "/api/sys/user/{}"
        self.delete_emp_url = app.BASE_URL + "/api/sys/user/{}"

    def add_emp(self, username, mobile):
        data = {"username": username,
                "mobile": mobile,
                "timeOfEntry": "2019-07-01",
                "formOfEmployment": 1,
                "workNumber": "1322131",
                "departmentName": "开发部",
                "departmentId": "1066240656856453120",
                "correctionTime": "2019-11-30"}
        return requests.post(self.add_emp_url, json=data, headers=app.headers_data)

    # 查询员工
    def query_emp(self, emp_id):
        url = self.query_emp_url.format(emp_id)
        return requests.get(url, headers=app.headers_data)

    # 修改员工
    def update_emp(self, emp_id, username):
        url = self.update_emp_url.format(emp_id)
        data = {"username": username}
        return requests.put(url, json=data, headers=app.headers_data)

    # 删除员工
    def delete_emp(self, emp_id):
        url = self.delete_emp_url.format(emp_id)
        return requests.delete(url, headers=app.headers_data)
