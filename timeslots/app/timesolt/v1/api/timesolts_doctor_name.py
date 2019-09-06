# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas
from pickle import *


class TimesoltsDoctorName(Resource):

    def get(self, doctor_name):
        doctor_name = ' '.join([e.capitalize() for e in doctor_name.split()])
        try:
            data_input = open('data.pkl', 'rb')
            timesolts = load(data_input)
            data_input.close()
        except:
            return {"message: no record"}, 400
        result = []
        if doctor_name not in timesolts.keys():
            return {"message": "invalid doctor name"}, 400
        for item in timesolts[doctor_name]:
            tmp = {}
            tmp['time'] = item['datetime']
            tmp['status'] = item['status']
            result.append(tmp)
        return result, 200