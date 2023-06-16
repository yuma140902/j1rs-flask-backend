#!/usr/bin/env python3

import connexion

from openapi_server import encoder

import threading
import time
import socket
import numpy as np

from flask_cors import CORS


class ReceiveThread(threading.Thread):
    def __init__(self, PORT=12345):
        threading.Thread.__init__(self)
        self.data = 0
        self.kill_flag = False
        # line information
        self.HOST = "127.0.0.1"
        self.PORT = PORT
        self.BUFSIZE = 1024
        self.ADDR = (socket.gethostbyname(self.HOST), self.PORT)
        # bind
        self.udpServSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.udpServSock.bind(self.ADDR)
        self.received = False

    def get_data(self):
        data_ary = []
        for i in reversed(range(8)):
            num = int(str(self.data[i*8:(i+1)*8]))
            data_ary.append(num / 167.0 / 10000)
        self.received = False
        return data_ary

    def run(self):
        while True:
            try:
                data, self.addr = self.udpServSock.recvfrom(self.BUFSIZE)
                self.data = data.decode()
                self.received = True
            except:
                pass


def main():
    th = ReceiveThread()
    th.setDaemon(True)
    th.start()

    app = connexion.App(__name__, specification_dir='./openapi/')
    CORS(
        app.app,
        supports_credentials=True
    )
    app.app.json_encoder = encoder.JSONEncoder
    app.app.config['__th__'] = th
    app.add_api('openapi.yaml',
                arguments={'title': '半自動センサー校正器「コウセイくん☆」Web API'},
                pythonic_params=True)

    app.run(host='0.0.0.0', port=8080)


if __name__ == '__main__':
    main()
