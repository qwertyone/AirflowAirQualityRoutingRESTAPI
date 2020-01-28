from flask import Flask, request, jsonify, render_template
#from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from helper import gettrafficFlow, overwrite_JSONvalues, azureJSONmaparser, tileToCoordJSON
from flask import make_response

from temp_helper import main

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

@app.route('/Coordinate', methods=['GET','POST'])
def pull():
	long = request.args.get('long')
	lat  = request.args.get('lat')	
	type(long)
	return '''long is: {} and lat is: {}'''.format(long,lat)
	
@app.route('/CoordinateJSON', methods=['GET','POST'])
def add_CoordinateJSON():

	long = float(request.args.get('long'))
	lat  = float(request.args.get('lat'))	 
	tileSize = 256
	zoom = 15
    
	tileX, tileY = gettrafficFlow(lat, long, tileSize, zoom)
	#print('Tile X Calculated: ' + str(tileX))
	#print('Tile Y calculated: ' + str(tileY))
	##return JSON file as obj
	obj = azureJSONmaparser(tileX, tileY, tileSize, zoom)
	
	##calculate pollution levels
	key = 'traffic_level'
	overwrite_JSONvalues(obj, key)

	##change tile vector coordinates to lat and long
	##this section of code is buggy. but this is an alpha
	key = 'coordinates'
	print('IMPORTANT')
	tileToCoordJSON(obj, key, zoom)
	#print(obj)
	return '''{}'''.format(obj)

@app.route('/GetRoute', methods=['GET','POST'])
def get_Route():
	lonA = float(request.args.get('lonA'))
	latA = float(request.args.get('latA'))

	lonB = float(request.args.get('lonB'))
	latB = float(request.args.get('latB'))	
	A = (lonA,latA)
	B = (lonB,latB)
	obj = main(A,B)
	#print(obj)
	return '''{}'''.format(obj)



@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

#    CoordinateJSON = CoordinateJSON.query.get(id)
#    db.session.delete(CoordinateJSON)
#    db.session.commit()

#    return jsonify(CoordinateJSON)




@app.route("/")

def index():

     return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
