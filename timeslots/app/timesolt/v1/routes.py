# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###
from __future__ import absolute_import

from .api.reservations import Reservations
from .api.reservations_reservation_id import ReservationsReservationId
from .api.timesolts_doctor_name import TimesoltsDoctorName
from .api.timesolts_doctor_name_date_time import TimesoltsDoctorNameDateTime


routes = [
    dict(resource=Reservations, urls=['/reservations'], endpoint='reservations'),
    dict(resource=ReservationsReservationId, urls=['/reservations/<int:reservation_id>'], endpoint='reservations_reservation_id'),
    dict(resource=TimesoltsDoctorName, urls=['/timesolts/<doctor_name>'], endpoint='timesolts_doctor_name'),
    dict(resource=TimesoltsDoctorNameDateTime, urls=['/timesolts/<doctor_name>/<date>/<time>'], endpoint='timesolts_doctor_name_date_time'),
]