from flask import Flask, request
from flask_restful import Resource, Api
from werkzeug.exceptions import HTTPException

from pipeline import pipeline
import deploy_model


app = Flask(__name__)
api = Api(app)


class Test(Resource):

    def get(self):
        return 'working'


class Pipeline(Resource):

    def post(self):
        file = request.files['file']
        pipeline(file)
        return 'worked?'


class Deploy(Resource):

    def post(self):
        model_id = request.form['model_id']
        deploy_model.run(model_id)
        return 'worked?'


api.add_resource(Test, '/')
api.add_resource(Pipeline, '/pipeline')
api.add_resource(Deploy, '/deploy_model')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8085)