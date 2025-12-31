#הגדרות בסיס: לדוגמא התחברנו לדאטה בייס ויצרנו מופע ליצירת סשן
from sqlalchemy.orm import declarative_base,sessionmaker#
from sqlalchemy import create_engine# ייבוא מתוך ספריית SQLAlchemy — ספרייה שמנהלת חיבור לדאטה־בייס ופעולות ORM.
from sqlalchemy.orm import declarative_base #יוצר מחלקת Session — “המסגרת” דרכה מריצים פעולות על הדאטה־בייס

base= declarative_base() # משתנה שיצטרכו לרשת ממנו בכל בניית מחלקה
engine=create_engine("mssql+pyodbc://@DESKTOP-24EQMFH/shop?driver=ODBC+Driver+17+for+SQL+Server&Trusted_Connection=yes")
# מחרוזת חיבור לדאטה בייס היא מורכבת מהשם של המחשב, שם הדאטה בייס והדרייבר
Session= sessionmaker(bind=engine)# התפקיד שלו לימור מחלקה שתשמש ליצירת סשנים חדשים וכל פעם שנרצה לעשות משהו מדאטה בייב ניצור מזה מופע ליצירת סשן ספציפי הבינד מחבר לסשן את הדאטה בייס