'''
    使用flaskwebtest进行测试
'''
from basic_flask import app as test_app
from flask_webtest import TestApp
import os
import unittest


class TestMyApp(unittest.TestCase):
    
    def setUp(self):
        http_server = os.environ.get('HTTP_SERVER', None)
        # 根据环境切换测试环境
        if http_server is not None:
            self.app = TestApp(http_server) # 为url字符串.http://example.com这种
        else:
            self.app = TestApp(test_app)

    def test_change(self):
#app = TestApp(test_app)

        hello = self.app.get("/api")

        assert hello.json['Hello'] == 'world'


