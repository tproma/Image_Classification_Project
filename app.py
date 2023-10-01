from flask import Flask, request, jsonify, render_template 
import os
from flask_cors import CORS, cross_origin
from ImageClassifier.utils.common import decodeImage
from ImageClassifier.pipeline.predict import PredictionPipeline


os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')


app = Flask(__name__)


@app.route('/pro', methods= ['POST'])
def strs():
    if (request.method =='POST'):
        name  = request.json['name']
        email = request.json['email']
        
        return jsonify(name + email)

if __name__=='__main__':
    app.run()