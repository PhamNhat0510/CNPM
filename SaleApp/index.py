from itertools import product
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import  dao
from SaleApp import  app

@app.route("/")
def index():
    q=request.args.get("q")
    cate_id=request.args.get("cate_id")
    cates=dao.load_categories()
    return render_template("index.html",cates=cates,prods=dao.load_products(q=q,cate_id=cate_id))
@app.route("/product/<int:id>")
def details(id):
    return render_template("product-details.html")
@app.context_processor
def common_attribute():
    return  {
        "cate":dao.load_categories()
    }
if __name__=="__main__":
    app.run(debug=True)