'''
    测试check_bug
'''
import unittest
from unittest import mock
import requests
from requests.exceptions import ConnectionError
import requests_mock
import sys
from check_bug import MyBugzilla


class TestBugzilla(unittest.TestCase):
    def test_bug_id(self):
        zilla = MyBugzilla('tarek@mozilla.com', server="http://example.com")
        link = zilla.bug_link(23)
        self.assertEqual(link, 'http://example.com/show_bug.cgi?id=23')
    
    # 模拟请求,对任何请求都响应,并且返回json结果
    @requests_mock.Mocker()
    def test_get_new_bugs(self, mocker):
        bugs = [{'id': 1184528}, {'id': 1184524}]
        mocker.get(requests_mock.ANY, json={'bugs': bugs})

        zilla = MyBugzilla('tarek@mozilla.com', server="http://example.com")
        bugs = list(zilla.get_new_bugs())
        self.assertEqual(bugs[0]['link'], 'http://example.com/show_bug.cgi?id=1184528')
    
    # 模拟请求,触发错误.参考官方案例
    @requests_mock.Mocker()
    def test_network_error(self, mocker):
        mocker.get(requests_mock.ANY, exc=ConnectionError("No network"))

        zilla = MyBugzilla('tarek@mozilla.com', server="http://example.com")

        bugs = list(zilla.get_new_bugs())
        self.assertEqual(len(bugs), 0)


if __name__ == "__main__":
    unittest.main()
