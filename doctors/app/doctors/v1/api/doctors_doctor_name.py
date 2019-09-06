# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from pickle import *

from .. import schemas
from string import *


class DoctorsDoctorName(Resource):

    def get(self, doctor_name):
        try:
            data_input = open('data.pkl', 'rb')
            doctors = load(data_input)
            data_input.close()
        except:
            return [], 200
        for e in doctors:
            if doctor_name.lower() == e['name'].lower():
                return {
                "name": e['name'],
                "location": e['location'],
                "specialization": e['specialization']
               }, 200
        return {'message':"Not found"}, 404, None
