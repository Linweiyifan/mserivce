'''
    功能测试
'''
import unittest
import json
from flask_error import app as tested_app


#class TestApp(unittest.TestCase):
#    def test_help(self):
#        app = tested_app.test_client()
#
#        hello = app.get("/api")
#
#        body = json.loads(str(hello.data, 'utf-8'))
#        self.assertEqual(body['Hello'], 'world')


# 使用nosetest测试.setUp初始化,tearDown清理环境,和unittest类似.装饰器方法会报错
class TestFlaskError(unittest.TestCase):
    def setUp(self):
        self.app = tested_app.test_client()

    def test_raise_error(self):
        hello = self.app.get('/api') # 以get方式请求
        body = json.loads(str(hello.data, 'utf-8')) # 获取的参数会保存在rsp.data中,字符串形式
        assert body[0]['code'] == 500
    
    def test_page_not_found(self):
        hello = self.app.get('/lastdance')

        assert hello.status_code == 404


if __name__ == "__main__":
    unittest.main()














