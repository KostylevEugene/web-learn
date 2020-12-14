from flask_sqlalchemy import SQLalchemy

db = SQLalchemy()

class News(db.model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Columbn(db.String, nullable=False)
    url = db.Column(db.String, unique=True, nullable=False)
    published = db.Column(db.DateTime, nullable=False)
    text = db.Column(db.Text, nullable=True)