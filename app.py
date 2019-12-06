from flask import Flask, request, jsonify, render_template
#from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from helper import gettrafficFlow, overwrite_JSONvalues, azureJSONmaparser

import os

#init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

#database
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.db')
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#db = SQLAlchemy(app)

#init ma
ma = Marshmallow(app)

#CoordinateJSON Class/Model
#class CoordinateJSON(db.Model):
#    id   = db.Column(db.Integer, primary_key=True)
#    long = db.Column(db.Float)
#    lat  = db.Column(db.Float)
    
#    def __init__(self, long, lat):

#        self.long = long
#        self.lat = lat

##CoordinateJSON schema
class CoordinateJSONSchema(ma.Schema):
    class Meta:
        fields = ('long', 'lat')

#init schema
#CoordinateJSONSchema  = CoordinateJSONSchema()

#submit JSON request
@app.route('/CoordinateJSON', methods=['GET'])
def add_CoordinateJSON():

    long = request.json['long']
    lat = request.json['lat']

#    newCoordinateJSON = CoordinateJSON(long, lat)

#    db.session.add(newCoordinateJSON)
#    db.session.commit()

    tileSize = 256
    zoom = 15
    
    tileX, tileY = gettrafficFlow(lat, long, tileSize, zoom)
    print('Tile X Calculated: ' + str(tileX))
    print('Tile Y calculated: ' + str(tileY))
    obj  = azureJSONmaparser(tileX, tileY, tileSize, zoom)
    print('PBF File returned')
    key = 'traffic_level'
    print('Success @ Key: ' + str(obj))
    overwrite_JSONvalues(obj, key)
    print(obj)
    return obj
    #return CoordinateJSONSchema.jsonify(newCoordinateJSON)

#get a JSON request
#@app.route('/CoordinateJSON/', methods=['GET'])
#def getCoordinateJSON():

#    CoordinateJSON = CoordinateJSON.query.get(id)

#    return jsonify(CoordinateJSON)

#@app.route('/CoordinateJSON/<id>', methods=['DELETE'])
#def deleteCoordinateJSON(id):

#    CoordinateJSON = CoordinateJSON.query.get(id)
#    db.session.delete(CoordinateJSON)
#    db.session.commit()

#    return jsonify(CoordinateJSON)




@app.route("/")

def index():

     return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
