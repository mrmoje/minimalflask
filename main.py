#!/usr/bin/env python
from flask import Flask
from flask_restful import Resource, Api
from sympy import mpmath

app = Flask(__name__)
api = Api(app)


class GetPi(Resource):
    def get(self, dp):
        mpmath.mp.dps = dp or 1000
        return {'pi': str(mpmath.mp.pi)}

api.add_resource(GetPi, '/<int:dp>')

if __name__ == '__main__':
    app.run()
