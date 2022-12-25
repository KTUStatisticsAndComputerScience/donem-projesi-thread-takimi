<script setup>

import {usePersonState} from "@/stores/person_state";
import {ref} from "vue";

const personStore = usePersonState();
personStore.yukle()

const eklenecek_kisi = ref({
  kisi_ad: "",
  kisi_soyad: "",
  telefon: "",
  email: "",
  adres: "",

});

function kaydet() {
  personStore.kisiEkle(eklenecek_kisi.value);
  eklenecek_kisi.value = {
    kisi_ad: "",
    kisi_soyad: "",
    telefon: "",
    email: "",
    adres: "",
  };
}

</script>

<template>
  <div class="row">
    <div class="col-1"></div>
    <div class="col-10">
      <h1>Kişi Ekle</h1>
      <hr class="style">
      <div class="row">
        <div class="col-3">
          <label for="fadi">Adı</label>
        </div>
        <div class="col-9">
          <input type="text" placeholder="Müşteri Adını Giriniz" v-model="eklenecek_kisi.kisi_ad">
        </div>
      </div>
      <div class="row">
        <div class="col-3">
          <label for="fsoyad">Soyad</label>
        </div>
        <div class="col-9">
          <input type="text" placeholder="Müşterinin Soyadını Giriniz" v-model="eklenecek_kisi.kisi_soyad">
        </div>
      </div>

      <div class="row">
        <div class="col-3">
          <label for="ftelefon">Telefon</label>
        </div>
        <div class="col-9">
          <input type="text" placeholder="Müşterinin Telefonunu Giriniz" v-model="eklenecek_kisi.telefon">
        </div>
      </div>
      <div class="row">
        <div class="col-3">
          <label for="femail">Email</label>
        </div>
        <div class="col-9">
          <input type="text" placeholder="Müşterinin Emailini Giriniz" v-model="eklenecek_kisi.email">
        </div>
      </div>
      <div class="row">
        <div class="col-3">
          <label for="fadres">Adres</label>
        </div>
        <div class="col-9">
          <textarea placeholder="Müşterinin Adresini Giriniz" rows="6" v-model="eklenecek_kisi.adres"></textarea>
        </div>
      </div>
      <div class="right">
        <button class="btn" @click="kaydet"><font-awesome-icon icon="fa-solid fa-paper-plane" /> Yolla</button>
      </div>

    </div>

    <div class="col-1"></div>
  </div>

</template>


<style scoped>

</style>