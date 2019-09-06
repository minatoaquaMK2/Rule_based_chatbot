# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas
from pickle import *
import json

class TimesoltsDoctorNameDateTime(Resource):

    def get(self, doctor_name, date, time):
        doctor_name = ' '.join([e.capitalize() for e in doctor_name.split()])
        tmp_datetime = date+" "+time;
        try:
            data_input = open('data.pkl', 'rb')
            timesolts = load(data_input)
            data_input.close()
        except:
            return {}, 404
        result = {
            "time":"null",
            "status": "null"
        }
        suggestion  ={
            "time":"null",
            "status": "null"
        }
        found = 0;
        if(doctor_name not in timesolts.keys()):
            return {'message':"invalid doctor name"},400
        for item in timesolts[doctor_name]:
            print(item['datetime'].replace(',','').replace(':','').lower())
            print(tmp_datetime)
            if item['datetime'].replace(',','').replace(':','').lower() == tmp_datetime:
                tmp_dic = {
                    "time": item['datetime'],
                    "status": item['status']
                }
                result = tmp_dic;
                if(item['status'] == 'available'):
                    found = 1;
                continue;
            if item['status']=="available":
                suggestion = {
                    "time": item['datetime'],
                    "status": item['status']
                }
        if found:
            return {"timesolt":result,"suggestion":{ "time":"null","status": "null"}},200
        else:
            return {"timesolt":result,
                "suggestion":suggestion
               },200

