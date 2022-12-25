
from .baglanti import db
class Kisi(db.Model):
    kisi_id = db.Column(db.Integer, primary_key=True)
    kisi_ad = db.Column(db.String)
    kisi_soyad = db.Column(db.String)
    telefon = db.Column(db.String(10), unique=True)
    email = db.Column(db.String)
    adres = db.Column(db.String)
