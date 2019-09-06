# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas
import json

from pickle import *


class Doctors(Resource):

    def get(self):

        try:
            data_input = open('data.pkl', 'rb')
            doctors = load(data_input)
            data_input.close()
        except:
            return [], 200

        return {"doctors": doctors}, 200, None

    def post(self):
        r = request.data.decode()
        doctor = json.loads(r)
        print(doctor)
        try:
            data_input = open('data.pkl', 'rb')
            doctors = load(data_input)
            data_input.close()
        except:
            doctors = []
        for e in doctors:
            if e['name'] == doctor['name']:
                return {"message": "input is invalid"}, 400
        doctors.append(doctor);
        dump(doctors, open('data.pkl', 'wb'), protocol=HIGHEST_PROTOCOL)
        print(json.dumps(doctor));
        return {
                "name": doctor['name'],
                "location": doctor['location'],
                "specialization": doctor['specialization']
               }, 200
