from flask import Blueprint

from db import Kargo, Kisi
from export.semalar import KargoSema, KisiSema
from .genel_bitis_noktalari import genel_bitis_noktasi_olustur

v1 = Blueprint('v1', __name__)
v1.register_blueprint(genel_bitis_noktasi_olustur("kargo", Kargo, KargoSema), url_prefix="/kargo")
v1.register_blueprint(genel_bitis_noktasi_olustur("kisi", Kisi, KisiSema), url_prefix="/kisi")

api = Blueprint('api', __name__)
api.register_blueprint(v1, url_prefix="/v1")