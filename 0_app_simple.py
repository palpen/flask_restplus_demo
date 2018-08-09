from flask import Flask

# Using flask restplus is really simple---
# just replace flask_restful with flask_resplus!

from flask_restful import Resource, Api
# from flask_restplus import Resource, Api

app = Flask(__name__)   # Create a Flask WSGI application
api = Api(app)          # Create a Flask-RESTPlus API

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}
api.add_resource(HelloWorld, '/hello')

# Alternatively (only for Flask Restplus)
# @api.route('/hello')
# class HelloWorld(Resource):
#     def get(self):
#         return {'hello': 'world'}

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
