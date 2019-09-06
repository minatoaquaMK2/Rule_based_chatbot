# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function
from pickle import *
import json
from flask import request, g
from datetime import datetime
from pickle import *

from . import Resource
from .. import schemas


class ReservationsReservationId(Resource):

    def put(self, reservation_id):
        r = request.data.decode()

        reservation = json.loads(r)
        if 'status' not in reservation.keys():
            return {"message": "no status in body"}, 400
        else:
            if reservation['status'] != 'available':
                return {"message": "invalid status"}, 400
            else:
                try:
                    data_input = open('data.pkl', 'rb')
                    data = load(data_input)
                    data_input.close()
                except:
                    return {"message": "no record"}, 400
                for doctor in data.keys():
                    for index, timesolt in enumerate(data[doctor]):
                        if timesolt['Reservation_id'] == reservation_id:
                            data[doctor][index]['status'] = 'available';
                            data[doctor][index]['Reservation_id'] = None;
                            dump(data, open('data.pkl', 'wb'), protocol=HIGHEST_PROTOCOL)
                            return {
                                "reservation_id":reservation_id,
                                "message":"canceled successful"
                            }, 200
        return {"message": "Booking id is invalid"}, 400