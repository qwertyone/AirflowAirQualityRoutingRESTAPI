from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

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

#Product Class/Model
class Product(db.Model):
    id   = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description =db.Column(db.String(190))
    price = db.Column(db.Float)
    qty  = db.Column(db.Integer)
    
    def __init__(self, name, description, price, qty):
        self.name = name
        self.description  = description
        self.price = price
        self.qty = qty

#product schema
class ProductSchema(ma.Schema):
    class Meta:
        fields = ('name', 'description', 'price', 'qty')

#init schema
productSchema = ProductSchema(strict=True)
productsSchema = ProductSchema(many=True, strict=True)

#submit JSON request
@app.route('/product', methods=['POST'])
def add_product():
    name = request.json['name']
    description  = request.json['description']
    price = request.json['price']
    qty = request.json['qty']

    newProduct = Product(name, description, price, qty)

    db.session.add(newProduct)
    db.session.commit()

    return ProductSchema.jsonify(newProduct)

#get JSON requests
@app.route('/product', methods=['GET'])
def getProducts():

    allProducts = Product.query.all()
    result = ProductsSchema(allProducts)

    return jsonify(result.data)

#get a JSON request
@app.route('/product/<id>', methods=['GET'])
def getProduct():

    product = Product.query.get(id)

    return jsonify(product)

@app.route('/product/<id>', methods=['PUT'])
def updateProduct():

    product = Product.query.get(id)
    name = request.json['name']
    description  = request.json['description']
    price = request.json['price']
    qty = request.json['qty']

    product.name = name
    product.description  = description
    product.price = price
    product.qty = qty

    db.session.commit()

    return ProductSchema.jsonify(Product)

@app.route('/product/<id>', methods=['DELETE'])
def deleteProduct(id):

    product = Product.query.get(id)
    db.session.delete(product)
    db.session.commit()

    return jsonify(product)


if __name__ == '__main__':
    app.run(debug=True)

#https://www.youtube.com/watch?v=PTZiDnuC86g
