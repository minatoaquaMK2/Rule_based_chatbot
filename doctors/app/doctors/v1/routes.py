# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###
from __future__ import absolute_import

from .api.doctors import Doctors
from .api.doctors_doctor_name import DoctorsDoctorName


routes = [
    dict(resource=Doctors, urls=['/doctors'], endpoint='doctors'),
    dict(resource=DoctorsDoctorName, urls=['/doctors/<doctor_name>'], endpoint='doctors_doctor_name'),
]