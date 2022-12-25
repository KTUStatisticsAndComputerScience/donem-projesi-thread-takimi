<script setup>

import {ref} from "vue";
import {useCargoState} from "@/stores/cargo_state";
import {usePersonState} from "@/stores/person_state";

const cargoStore = useCargoState();
const personStore = usePersonState();

personStore.yukle()
cargoStore.yukle()

const eklenecek_kargo = ref({
  kargo_gonderici_id : "",
  kargo_alici_id : "",
  kargo_en: "",
  kargo_yukseklik: "",
  kargo_boy: "",
  kargo_agirlik: "",
});

function kaydet() {
  cargoStore.kargoEkle(eklenecek_kargo.value);
  eklenecek_kargo.value = {
    kargo_gonderici_id : "",
    kargo_alici_id : "",
    kargo_en: "",
    kargo_yukseklik: "",
    kargo_boy : "",
    kargo_agirlik: ""
  };
}

</script>


<template>
  <div class="row">
    <div class="col-1"></div>
    <div class="col-10">
      <h1>Kargo Ekle</h1>
      <hr class="style">
      <div class="row">
        <div class="col-3">
          <label for="fgonderici">Gönderici</label>
        </div>
        <div class="col-9">
          <select name="fgonderici" v-model="eklenecek_kargo.kargo_gonderici_id">
            <option selected="selected" value="">Değiştirmek için seçim yapın</option>
            <option v-for="kisi in personStore.persons" :value="kisi.kisi_id"> {{ kisi.kisi_ad + ' ' + kisi.kisi_soyad}}</option>
          </select>
        </div>
      </div>
      <div class="row">
        <div class="col-3">
          <label for="falici">Alıcı</label>
        </div>
        <div class="col-9">

          <select name="falici" v-model="eklenecek_kargo.kargo_alici_id">
            <option selected="selected" value="">Değiştirmek için seçim yapın</option>
            <option v-for="kisi in personStore.persons" :value="kisi.kisi_id"> {{ kisi.kisi_ad + ' ' + kisi.kisi_soyad }}</option>
          </select>
        </div>
      </div>

      <div class="row">
        <div class="col-3">
          <label for="fen">En</label>
        </div>
        <div class="col-9">
          <input type="number" placeholder="En Giriniz" v-model="eklenecek_kargo.kargo_en">
        </div>
      </div>
      <div class="row">
        <div class="col-3">
          <label for="fyukseklik">Yükseklik</label>
        </div>
        <div class="col-9">
          <input type="number" placeholder="Yükseklik Giriniz" v-model="eklenecek_kargo.kargo_yukseklik">
        </div>
      </div>
      <div class="row">
        <div class="col-3">
          <label for="fgenislik">Genişlik</label>
        </div>
        <div class="col-9">
          <input type="number" placeholder="Genişlik Giriniz" v-model="eklenecek_kargo.kargo_boy">
        </div>
      </div>
      <div class="row">
        <div class="col-3">
          <label for="fagirlik">Ağırlık</label>
        </div>
        <div class="col-9">
          <input type="number" placeholder="Ağırlık Giriniz" v-model="eklenecek_kargo.kargo_agirlik">
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