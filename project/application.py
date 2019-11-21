from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from helper import gettrafficFlow

import os

#init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

#database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#init ma
ma = Marshmallow(app)

#CoordinateJSON Class/Model
class CoordinateJSON(db.Model):
    id   = db.Column(db.Integer, primary_key=True)
    long = db.Column(db.Float)
    lat  = db.Column(db.Float)
    
    def __init__(self, long, lat):

        self.long = long
        self.lat = lat

#CoordinateJSON schema
class CoordinateJSONSchema(ma.Schema):
    class Meta:
        fields = ('long', 'lat')

#init schema
CoordinateJSONSchema  = CoordinateJSONSchema(strict=True)

#submit JSON request
@app.route('/CoordinateJSON', methods=['POST'])
def add_CoordinateJSON():

    long = request.json['long']
    lat = request.json['lat']

    newCoordinateJSON = CoordinateJSON(long, lat)

    db.session.add(newCoordinateJSON)
    db.session.commit()

    tileSize = 256
    zoom = 15
    
    URL = gettrafficFlow(lat, long, tileSize, zoom)

    return jsonify(URL)

    #return CoordinateJSONSchema.jsonify(newCoordinateJSON)

#get a JSON request
@app.route('/CoordinateJSON/', methods=['GET'])
def getCoordinateJSON():

    CoordinateJSON = CoordinateJSON.query.get(id)

    return jsonify(CoordinateJSON)

#@app.route('/CoordinateJSON/<id>', methods=['DELETE'])
#def deleteCoordinateJSON(id):

#    CoordinateJSON = CoordinateJSON.query.get(id)
#    db.session.delete(CoordinateJSON)
#    db.session.commit()

#    return jsonify(CoordinateJSON)


if __name__ == '__main__':
    app.run(debug=True)

#https://www.youtube.com/watch?v=PTZiDnuC86g
