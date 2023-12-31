# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class MResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, index=None, v=None):  # noqa: E501
        """MResponse - a model defined in OpenAPI

        :param index: The index of this MResponse.  # noqa: E501
        :type index: int
        :param v: The v of this MResponse.  # noqa: E501
        :type v: float
        """
        self.openapi_types = {
            'index': int,
            'v': float
        }

        self.attribute_map = {
            'index': 'index',
            'v': 'v'
        }

        self._index = index
        self._v = v

    @classmethod
    def from_dict(cls, dikt) -> 'MResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The m_response of this MResponse.  # noqa: E501
        :rtype: MResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def index(self):
        """Gets the index of this MResponse.


        :return: The index of this MResponse.
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this MResponse.


        :param index: The index of this MResponse.
        :type index: int
        """
        if index is None:
            raise ValueError("Invalid value for `index`, must not be `None`")  # noqa: E501

        self._index = index

    @property
    def v(self):
        """Gets the v of this MResponse.


        :return: The v of this MResponse.
        :rtype: float
        """
        return self._v

    @v.setter
    def v(self, v):
        """Sets the v of this MResponse.


        :param v: The v of this MResponse.
        :type v: float
        """
        if v is None:
            raise ValueError("Invalid value for `v`, must not be `None`")  # noqa: E501

        self._v = v
