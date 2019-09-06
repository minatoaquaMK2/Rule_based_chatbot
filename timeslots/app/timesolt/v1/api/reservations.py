# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas
import json
import random
from datetime import datetime
from pickle import *

class Reservations(Resource):

    def post(self):
        r = request.data.decode()
        random.seed(datetime.now())
        reservation = json.loads(r)

        print(g.json)
        try:
            data_input = open('data.pkl', 'rb')
            data = load(data_input)

            data_input.close()
        except:
            return {"message": "input is invalid"}, 400
        doctor_name = ' '.join([e.capitalize() for e in reservation['doctor_name'].split()])
        print(doctor_name)
        if doctor_name in data.keys():
            for index,timesolt in enumerate(data[doctor_name]):
                print(timesolt['datetime'].replace(',','').replace(':',''))
                if timesolt['datetime'].replace(',','').replace(':','').lower() == reservation['timesolt']:
                    r_id = random.randint(1, 10000);
                    if(data[doctor_name][index]['Reservation_id']!=None):
                        return {"message": "the time slot is reserved"}, 400
                    data[doctor_name][index]['Reservation_id']=r_id;
                    data[doctor_name][index]['status']='reserved';
                    result = {
                        "reservation_id":r_id,
                        "doctor_name":doctor_name,
                        "timesolt":timesolt['datetime']
                    }
                    dump(data, open('data.pkl', 'wb'), protocol=HIGHEST_PROTOCOL)
                    return result,200
            return {"message": "invalid time slot"}, 400
        else:
            return {"message": "invalid doctor name"}, 400
