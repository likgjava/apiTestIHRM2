import unittest

import app
from script.test_employee import TestEmployee
from script.test_login import TestLogin
from tools.HTMLTestRunner import HTMLTestRunner
import time

# 封装测试套件
suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestLogin))
suite.addTest(unittest.makeSuite(TestEmployee))

# 执行测试套件
# unittest.TextTestRunner().run(suite)

# 定义测试报告文件路径
# report_path = app.BASE_DIR + "/report/report-{}.html".format(time.strftime("%Y%m%d-%H%M%S"))
report_path = app.BASE_DIR + "/report/report.html"

# 打开文件流
with open(report_path, "wb") as f:
    # 创建HTMLTestRunner运行器对象
    runner = HTMLTestRunner(f, title="IHRM接口测试报告", description="V1.0")

    # 执行测试套件
    runner.run(suite)

    print("over...")
