# 通用的断言方法
def common_assert(test_case, response, status_code=200, success=True, code=10000, message="操作成功"):
    # 响应状态码
    test_case.assertEqual(status_code, response.status_code)

    # 获取返回JSON数据
    result = response.json()
    test_case.assertEqual(success, result.get("success"))
    test_case.assertEqual(code, result.get("code"))
    test_case.assertIn(message, result.get("message"))
