from flask import send_from_directory, jsonify, Blueprint
from sqlalchemy.orm import joinedload

from Models.Base import Session
from Models.Item import Item

item_bp=Blueprint("item_bp",__name__)
@item_bp.route('/get_items', methods=['GET'])
def get_items():
    try:
        db = Session()
        items = db.query(Item).options(
        joinedload(Item.company),
        joinedload(Item.category)).all()
        items_list = [item.to_dict() for item in items]
        return jsonify(items_list)
    except:
        return jsonify({"status": "error", "message": "התרחשה שגיאה"})
    finally:
        db.close()

@item_bp.route('/get_img/<int:img>', methods=['GET'])
def get_img(img):
    img_with_extention = f"{img}.jpg"
    return send_from_directory("images",img_with_extention)#החזרת הקובץ הבינארי בדפדפן
