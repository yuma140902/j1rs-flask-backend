# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.done_response import DoneResponse  # noqa: E501
from openapi_server.models.m_request import MRequest  # noqa: E501
from openapi_server.models.m_response import MResponse  # noqa: E501
from openapi_server.models.model_request import ModelRequest  # noqa: E501
from openapi_server.models.model_response import ModelResponse  # noqa: E501
from openapi_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_get_health(self):
        """Test case for get_health

        サーバー(コウセイくん☆)が正常に動作していれば\"OK\"を返す
        """
        headers = { 
        }
        response = self.client.open(
            '/health',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_done(self):
        """Test case for post_done

        m_iの入力を終了してフィッティングを開始する
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/done',
            method='POST',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_m(self):
        """Test case for post_m

        m_iを追加する
        """
        m_request = {"index":42,"value":12.345}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/m',
            method='POST',
            headers=headers,
            data=json.dumps(m_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_start(self):
        """Test case for post_start

        校正のための一連の処理を開始する
        """
        headers = { 
        }
        response = self.client.open(
            '/start',
            method='POST',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_model(self):
        """Test case for put_model

        モデル式m=f(V)を指定する
        """
        model_request = {"expression":"a*m+b"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/model',
            method='PUT',
            headers=headers,
            data=json.dumps(model_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
