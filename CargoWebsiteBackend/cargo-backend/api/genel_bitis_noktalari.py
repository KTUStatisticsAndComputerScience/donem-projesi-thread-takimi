from flask import Blueprint, jsonify, request

from aracgerec import filtrele
from db import db


def genel_bitis_noktasi_olustur(kargo, db_sinifi, sema_sinifi):
    bp = Blueprint(kargo, __name__)

    @bp.route("/", methods=["GET"])
    def tumu():
        kayitlar = filtrele(db_sinifi)
        sema = sema_sinifi()
        return sema.dump(kayitlar, many=True)

    @bp.route("/sayfa/<int:kayit_sayisi>/<int:sayfa_no>")
    def sayfa(kayit_sayisi, sayfa_no):
        sayfa_no -= 1

        atlanacak_kayit_sayisi = kayit_sayisi * sayfa_no
        getirilecek_kayit_sayisi = kayit_sayisi

        kayitlar = filtrele(db_sinifi).offset(atlanacak_kayit_sayisi).limit(getirilecek_kayit_sayisi).all()

        sema = sema_sinifi()
        return sema.dump(kayitlar, many=True)

    @bp.route("/sayfa/<int:kayit_sayisi>")
    def sayfa_sayisi(kayit_sayisi):
        kargo_sayisi = filtrele(db_sinifi).count()
        sayfa_sayisi = kargo_sayisi // kayit_sayisi
        if kargo_sayisi % kayit_sayisi > 0:
            sayfa_sayisi += 1
        return jsonify({"kayit_sayisi": kargo_sayisi, "sayfa_sayisi": sayfa_sayisi})

    @bp.route("/<int:id>", methods=["GET"])
    def detay(id):
        kargo = db.get_or_404(db_sinifi, id)
        sema = sema_sinifi()
        return sema.dump(kargo)

    @bp.route("/", methods=["POST"])
    def ekle():
        yeni_kayit = request.json
        yeni = db_sinifi(**yeni_kayit)
        db.session.add(yeni)
        db.session.commit()
        sema = sema_sinifi()
        return sema.dump(yeni)

    @bp.route("/<int:id>", methods=["PUT", "PATCH"])
    def guncelle(id):
        kayit = db.get_or_404(db_sinifi, id)
        kayit_bilgileri = request.json
        sema = sema_sinifi()
        yeni_kargo = sema.load(kayit_bilgileri, instance=kayit, session=db.session)
        db.session.commit()
        return sema.dump(yeni_kargo)

    @bp.route("/<int:id>", methods=["DELETE"])
    def sil(id):
        kayit = db.get_or_404(db_sinifi, id)
        db.session.delete(kayit)
        db.session.commit()
        return jsonify({"sonuc": "TAMAM"})

    return bp
