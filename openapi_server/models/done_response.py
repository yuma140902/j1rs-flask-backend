# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.done_response_parameters_inner import DoneResponseParametersInner
from openapi_server import util

from openapi_server.models.done_response_parameters_inner import DoneResponseParametersInner  # noqa: E501

class DoneResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, expression=None, parameters=None):  # noqa: E501
        """DoneResponse - a model defined in OpenAPI

        :param expression: The expression of this DoneResponse.  # noqa: E501
        :type expression: str
        :param parameters: The parameters of this DoneResponse.  # noqa: E501
        :type parameters: List[DoneResponseParametersInner]
        """
        self.openapi_types = {
            'expression': str,
            'parameters': List[DoneResponseParametersInner]
        }

        self.attribute_map = {
            'expression': 'expression',
            'parameters': 'parameters'
        }

        self._expression = expression
        self._parameters = parameters

    @classmethod
    def from_dict(cls, dikt) -> 'DoneResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The done_response of this DoneResponse.  # noqa: E501
        :rtype: DoneResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def expression(self):
        """Gets the expression of this DoneResponse.


        :return: The expression of this DoneResponse.
        :rtype: str
        """
        return self._expression

    @expression.setter
    def expression(self, expression):
        """Sets the expression of this DoneResponse.


        :param expression: The expression of this DoneResponse.
        :type expression: str
        """
        if expression is None:
            raise ValueError("Invalid value for `expression`, must not be `None`")  # noqa: E501

        self._expression = expression

    @property
    def parameters(self):
        """Gets the parameters of this DoneResponse.


        :return: The parameters of this DoneResponse.
        :rtype: List[DoneResponseParametersInner]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this DoneResponse.


        :param parameters: The parameters of this DoneResponse.
        :type parameters: List[DoneResponseParametersInner]
        """
        if parameters is None:
            raise ValueError("Invalid value for `parameters`, must not be `None`")  # noqa: E501

        self._parameters = parameters
