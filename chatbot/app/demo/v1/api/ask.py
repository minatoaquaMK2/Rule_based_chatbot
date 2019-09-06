# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas
from rivescript import RiveScript
import json

rs = RiveScript()
rs.load_directory("./v1/api/brain")
rs.sort_replies()

class Ask(Resource):

    def post(self):
        r = request.data.decode()
        print(r)
        message = json.loads(r)["message"]
        print(message);

        reply = rs.reply("localuser", message)

        return {
                "message":reply
               }, 200, None