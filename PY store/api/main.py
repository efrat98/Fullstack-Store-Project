# This is a sample Python script.
import datetime

from flask import Flask,request,jsonify,send_from_directory #יבוא הספריה
from flask_cors import CORS # לאפשר גשה לכל תוכנה חיצונית שרוצה לפנות אלינו
from datetime import date #הבאתי ספריה של תאריך

from sqlalchemy.orm import joinedload

from Models.Base import Session, base, engine
from Models.User import User
from Models.Category import Catrgory
from Models.Company import Company
from Models.Item import Item
from sqlalchemy import select
from datetime import datetime, timedelta

from werkzeug.security import generate_password_hash, check_password_hash

from routes.user_routes import user_bp
from routes.item_routes import item_bp

app=Flask(__name__)#  name זה השם יצירת המופע אובייקט שמייצג את הישום app אובייקט מסוג    fask
app.register_blueprint(user_bp,url_prefix='/api/user')
app.register_blueprint(item_bp,url_prefix='/api/item')
CORS(app, resources={r"/*": {"origins": "*"}})# הגדרנו שכולם יכולים לפנות
base.metadata.create_all(bind=engine)

@app.route('/get_items', methods=['GET'])
def get_items():
    db = Session()
    items = db.query(Item).options(
    joinedload(Item.company),
    joinedload(Item.category)).all()
    items_list = [item.to_dict() for item in items]
    print (items_list)
    return jsonify(items_list)

@app.route('/get_img/<int:img>', methods=['GET'])
def get_img(img):
    img_with_extention = f"{img}.jpg"
    print(img_with_extention)
    return send_from_directory("images",img_with_extention)#החזרת הקובץ הבינארי בדפדפן





if __name__ == '__main__':
    app.run(debug=True)
