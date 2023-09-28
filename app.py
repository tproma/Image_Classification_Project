from flask import Flask, request, jsonify, render_template 
import os
from flask_cors import CORS, cross_origin
from ImageClassifier.utils.common import decodeImage
from ImageClassifier.pipeline.predict import PredictionPipeline



app = Flask(__name__)

@app.route('/via_postman', methods= ['POST'])
def math_postman():
    if (request.method =='POST'):
        n1 = int(request.json['n1'])
        n2 = int(request.json['n2'])
        n3 = int(request.json['n3'])
        result = n1 * n2 *n3
        return jsonify(result)
    


@app.route('/pro', methods= ['POST'])
def strs():
    if (request.method =='POST'):
        name  = request.json['name']
        email = request.json['email']
        
        return jsonify(name + email)

if __name__=='__main__':
    app.run()