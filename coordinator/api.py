from flask import Flask, request
from flask_restful import Resource, Api
from werkzeug.exceptions import HTTPException
from pipeline import pipeline

app = Flask(__name__)
api = Api(app)


class Pipeline(Resource):

    def post(self):
        file = request.files['file']
        pipeline(file)
        return 'worked?'


api.add_resource(Pipeline, '/')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=80)
