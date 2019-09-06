# -*- coding: utf-8 -*-
from __future__ import absolute_import

from flask import Flask
from pickle import *

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
        doctors = [
            {
                "location": "Mascot",
                "name": "Jessica Wong",
                "specialization": "Orthodontics"
            },
            {
                "location": "Kingsford",
                "name": "Tim McDonald",
                "specialization": "Paediatric Dentistry"
            },
            {
                "location": "Randwick",
                "name": "Bob Adela",
                "specialization": "Oral Surgery"
            }
        ]
        dump(doctors ,open('data.pkl','wb'),protocol= HIGHEST_PROTOCOL)





if __name__ == '__main__':
    create_app().run('0.0.0.0',debug=True,port = 7777)