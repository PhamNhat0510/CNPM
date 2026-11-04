from itertools import product
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from models import db, Category, Product
import  dao
from SaleApp import  app
app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/saledb?charset=utf8mb4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db.init_app(app)

# ===== CẤU HÌNH FLASK-ADMIN =====
admin = Admin(app, name='QUẢN TRỊ BÁN HÀNG')

# Thêm các trang quản lý model vào Admin
admin.add_view(ModelView(Category, db.session))
admin.add_view(ModelView(Product, db.session))

@app.route("/")
def index():
    q = request.args.get("q")
    cate_id = request.args.get("cate_id")
    cates = dao.load_categories()
    return render_template("index.html", cates=cates, prods=dao.load_products(q=q, cate_id=cate_id))
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