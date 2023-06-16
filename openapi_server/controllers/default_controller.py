import connexion
import six
import numpy as np
from typing import Dict
from typing import Tuple
from typing import Union

from flask import current_app

import time

from openapi_server.models.done_response import DoneResponse  # noqa: E501
from openapi_server.models.done_response_parameters_inner import DoneResponseParametersInner
from openapi_server.models.m_request import MRequest  # noqa: E501
from openapi_server.models.m_response import MResponse  # noqa: E501
from openapi_server.models.model_request import ModelRequest  # noqa: E501
from openapi_server.models.model_response import ModelResponse  # noqa: E501
from openapi_server import util

import plotly.graph_objects as go
import plotly.io as pio

from . import gd
from . import sf

def reset():
    current_app.config['__kousei_expr'] = None
    current_app.config['__kousei_m'] = []
    current_app.config['__kousei_v'] = []


def fitting():
    code = current_app.config['__kousei_expr']
    # モデル式
    f = sf.str_to_func(code)
    # 目的変数
    ms = np.array(current_app.config['__kousei_m'])
    # 入力変数
    vs = np.array(current_app.config['__kousei_v'])
    # 損失関数
    loss_func = gd.get_loss_function(f)
    # パラメータの初期値
    initial_params = 5.0 * np.random.rand(5)

    # 勾配降下法を適用
    params = gd.gradient_descent(vs, ms, loss_func, 0.01, initial_params, 1e-3)
    return params

def save_html_graph(params):
    code = current_app.config['__kousei_expr']
    # モデル式
    f = sf.str_to_func(code)
    # 目的変数
    ms = np.array(current_app.config['__kousei_m'])
    # 入力変数
    vs = np.array(current_app.config['__kousei_v'])
    
    plots = []
    d = go.Scatter(x=vs, y=ms, mode='markers')
    plots.append(d)

    ms_fit = []
    vs_fit = []
    v = np.min(vs)
    dv = (np.max(vs) - np.min(vs)) / 100.0
    while v < np.max(vs):
        vs_fit.append(v)
        ms_fit.append(f(v, params))
        v += dv

    d = go.Scatter(x=vs_fit, y=ms_fit, mode='lines')
    plots.append(d)
    layout = go.Layout(
      title=dict(text='校正結果'),
      xaxis=dict(title='V'),
      yaxis=dict(title='m'),
    )
    fig = go.Figure(data=plots, layout=layout)
    pio.write_html(fig, './static/out.html')


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
    params = fitting()
    save_html_graph(params)
    res = DoneResponse()
    res.expression = current_app.config['__kousei_expr']
    p = []
    for i in range(len(params)):
        drpi = DoneResponseParametersInner()
        drpi.name = 'p[' + str(i) + ']'
        drpi.value = params[i]
        p.append(drpi)
    res.parameters = p
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

    th = current_app.config['__th__']
    v = 0.0
    for _i in range(3):
        while not th.received:
            time.sleep(0.1)
        v += th.get_data()[0]

    v /= 3.0
    current_app.config['__kousei_v'].append(v)
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
