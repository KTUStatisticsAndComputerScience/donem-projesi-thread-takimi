from sqlalchemy import Column

from db.baglanti import db


class Kargo(db.Model):
    kargo_id = db.Column(db.BigInteger, primary_key=True)
    kargo_alici_id = db.Column(db.Integer, db.ForeignKey('kisi.kisi_id'))
    kargo_gonderici_id = db.Column(db.Integer, db.ForeignKey('kisi.kisi_id'))
    kargo_en = db.Column(db.Float)
    kargo_boy = db.Column(db.Float)
    kargo_yukseklik = db.Column(db.Float)
    kargo_agirlik = db.Column(db.Float)

    alici = db.relationship('Kisi', foreign_keys=[kargo_alici_id], backref="alici")
    gonderici = db.relationship('Kisi', foreign_keys=[kargo_gonderici_id], backref="gonderici")
