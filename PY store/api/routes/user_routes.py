from flask import jsonify, request,Blueprint
from marshmallow import ValidationError

from Models.Base import Session
from Models.User import User
from schemas.user_schema import userRegisterSchema,userLoginSchema

user_bp=Blueprint("user_bp",__name__)
user_register_schema=userRegisterSchema()
user_login_schema=userLoginSchema()
@user_bp.route('/login', methods=['POST'])
def login():
    data =request.get_json()
    pas = data.get("password")
    email = data.get("email")
    db = Session()

    try:
        validate_data=user_login_schema.load(data)
        user = db.query(User).filter(User.email == email).first()
        if user is None:
            return jsonify({"status": "error", "message": "אתה לא קיים במערכת להתחברות הרשם"}), 400
        if user.password==pas:
            return jsonify({"status": "sucsses", "message": "התחברת בהצלחה"}), 200
        return jsonify({"status": "error", "message": "הסיסמה שגויה אנא נסה שנית"}), 400
    except ValidationError as e:
        return jsonify({"status": "error", "message": e.messages})
    except :
        return jsonify({"status": "error", "message": "התרחשה שגיאה" })
    finally:
        db.close()


@user_bp.route('/register', methods=['POST'])
def register():# פונקציה שמטפלת בבקשה
    db = Session()  # מתחברת לדאטה בייס
    data = request.get_json() #שולפת את הבקשה ששלח לי
    name = data.get("name", "")
    pas = data.get("password", "")
    email = data.get("email", "" )
    phone = data.get("phone")
    try:
        print(data)
        validate_data=user_register_schema.load(data)
        print(validate_data)

        if not name or not pas:
            return jsonify({"status": "error", "message": "יש למלא שם משתמש וסיסמה."}), 400
        new_user = User(name=name, password=pas,email=email,phone=phone)#יוצרת אובייקט עם ערכים שהגיעו מהמשתמש
        db.add(new_user)
        db.commit()#מוסיף
        db.refresh(new_user)#מעדכן את הניו יוזר עם כל המידע כולל המידע שהתווסף אוטומטית בהוספת הרשומה לטבלה לדו איי די
        return jsonify({"status": "success", "message": "הרשמתך בוצעה בהצלחה", "user_id": new_user.id}), 201
    except ValidationError as e:
        db.rollback()
        return jsonify({"status": "error", "message": e.messages})
    except:
        db.rollback()
        return  jsonify({"status": "error", "message": "התרחשה שגיאה"})
    finally:

        db.close()