import connexion
import six
from typing import Dict
from typing import Tuple
from typing import Union

from flask import current_app

from openapi_server.models.done_response import DoneResponse  # noqa: E501
from openapi_server.models.m_request import MRequest  # noqa: E501
from openapi_server.models.m_response import MResponse  # noqa: E501
from openapi_server.models.model_request import ModelRequest  # noqa: E501
from openapi_server.models.model_response import ModelResponse  # noqa: E501
from openapi_server import util


def reset():
    ...


def fitting():
    ...


def get_health():  # noqa: E501
    """サーバー(コウセイくん☆)が正常に動作していれば\&quot;OK\&quot;を返す

     # noqa: E501


    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    th = current_app.config["__th__"]
    sensor_data = th.get_data()
    return ", ".join([str(d) for d in sensor_data])


def post_done():  # noqa: E501
    """m_iの入力を終了してフィッティングを開始する

     # noqa: E501


    :rtype: Union[DoneResponse, Tuple[DoneResponse, int], Tuple[DoneResponse, int, Dict[str, str]]
    """
    fitting()
    res = DoneResponse()
    res.expression = current_app.config['__kousei_expr']
    res.parameters = []
    return res


def post_m(m_request=None):  # noqa: E501
    """m_iを追加する

     # noqa: E501

    :param m_request: 
    :type m_request: dict | bytes

    :rtype: Union[MResponse, Tuple[MResponse, int], Tuple[MResponse, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        m_request = MRequest.from_dict(connexion.request.get_json())  # noqa: E501

    index = m_request.index
    value = m_request.value
    if '__kousei_m' not in current_app.config:
        current_app.config['__kousei_m'] = []

    current_app.config['__kousei_m'].append(value)

    res = MResponse()
    res.index = index
    v = current_app.config['__th__'].get_data()[0]
    res.v = v

    return res


def post_start():  # noqa: E501
    """校正のための一連の処理を開始する

     # noqa: E501


    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    reset()
    return None


def put_model(model_request=None):  # noqa: E501
    """モデル式m&#x3D;f(V)を指定する

     # noqa: E501

    :param model_request: 
    :type model_request: dict | bytes

    :rtype: Union[ModelResponse, Tuple[ModelResponse, int], Tuple[ModelResponse, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        model_request = ModelRequest.from_dict(connexion.request.get_json())  # noqa: E501

    expr = model_request.expression
    current_app.config['__kousei_expr'] = expr

    res = ModelResponse()
    res.expression = current_app.config['__kousei_expr']
    res.parameters = []
    return res
