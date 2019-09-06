# -*- coding: utf-8 -*-
from __future__ import absolute_import

from flask import Flask
from pickle import *
from datetime import datetime

import v1


def create_app():
    initdata();
    app = Flask(__name__, static_folder='static')
    app.register_blueprint(
        v1.bp,
        url_prefix='/v1')
    return app

def initdata():
    try:
        data_input = open('data.pkl', 'rb')
        data_input.close()
    except:
        timesolts = {
            "Jessica Wong":[
                {
                    "datetime":"Tue, 06 Aug 09:00",
                    "status":"reserved",
                    "Reservation_id": None
                },
                {
                    "datetime": "Tue, 06 Aug 10:00",
                    "status": "available",
                    "Reservation_id": None
                },
                {
                    "datetime": "Tue, 06 Aug 11:00",
                    "status": "available",
                    "Reservation_id": None
                },
                {
                    "datetime": "Tue, 06 Aug 14:00",
                    "status": "available",
                    "Reservation_id": None
                }
            ],
            "Tim McDonald":[
                {
                    "datetime": "Tue, 06 Aug 09:00",
                    "status": "available",
                    "Reservation_id": None
                },
                {
                    "datetime": "Tue, 06 Aug 10:00",
                    "status": "available",
                    "Reservation_id": None
                },
                {
                    "datetime": "Tue, 06 Aug 15:00",
                    "status": "available",
                    "Reservation_id": None
                },
                {
                    "datetime": "Tue, 06 Aug 16:00",
                    "status": "available",
                    "Reservation_id": None
                }
            ],
            "Bob Adela": [
                {
                    "datetime": "Tue, 06 Aug 09:00",
                    "status": "available",
                    "Reservation_id": None
                },
                {
                    "datetime": "Tue, 06 Aug 10:00",
                    "status": "available",
                    "Reservation_id": None
                },
                {
                    "datetime": "Tue, 06 Aug 11:00",
                    "status": "available",
                    "Reservation_id": None
                },
                {
                    "datetime": "Tue, 06 Aug 13:00",
                    "status": "available",
                    "Reservation_id": None
                }
            ]
        }
        dump(timesolts ,open('data.pkl','wb'),protocol= HIGHEST_PROTOCOL)

if __name__ == '__main__':
    create_app().run('0.0.0.0',debug=True,port = 7778)