from sqlalchemy import Column, Integer,String# ייבאתי ספריה
from .Base import base
class User(base):#יוצרים מחלקה בשם יוזר שיורשת מבייס מחלקה שבה כל מופע של המחלקה הזאת מייצג שורה בטבלת נתונים
    #מחלקה שמשויכת לטבלה מסויימת ORM
    __tablename__='User'# לאיזה טבלה אני שייכת
    id=Column(Integer,primary_key=True,autoincrement=True)# מייצג עמודה שמשמת כמו מפתח ראשי בטבלה שהוא מספר בסדר רץ
    name=Column(String(60),nullable=False,)# שם המשתמש מחרוזת והוא לא יכול להיות נל
    password=Column(String(20),nullable=False)# סיסמה שהיא גם מחרוזת לא יכולה להיות נל והיא צריכה להיות יחודית
    email=Column(String(30),nullable=False,unique=True)
    phone=Column(String(10),nullable=False)
    #יצרנו טבלה
    #מוגדר ברמת דאטה בייס ולא פייתון
