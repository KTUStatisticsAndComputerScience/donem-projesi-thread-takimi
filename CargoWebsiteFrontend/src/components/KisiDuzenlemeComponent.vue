<script setup>


import {usePersonState} from "@/stores/person_state";
import {ref} from "vue";


const personStore = usePersonState();

const duzenlenecek_kisi = ref({
  kisi_ad: "",
  kisi_soyad: "",
  telefon: "",
  adres: "",
  email: "",
})

function duzenle() {
  personStore.kisiDuzenle(duzenlenecek_kisi.value, personStore.selectedPerson.kisi_id);
  duzenlenecek_kisi.value = {
    kisi_ad: "",
    kisi_soyad: "",
    telefon: "",
    adres: "",
    email: "",
  }
}
</script>

<template>
  <div class="row">
    <div class="col-1"></div>
    <div class="col-10" v-if="personStore.selectedPerson === null">Düzenlenecek kisiyi seçiniz..</div>
    <div class="col-10" v-if="personStore.selectedPerson !== null">
      <h1>Düzenle</h1>
      <hr class="style">
      <p> Tüm alanları şuan doldurmak gerekiyor. Daha sonra düzenleme yapılacak.</p>
      <br>


      <div class="row">
        <div class="col-3">
          <label for="fad">Ad</label>
        </div>
        <div class="col-9">
          <input type="text" v-model="duzenlenecek_kisi.kisi_ad"
                 :placeholder="'Şuan ki ad: ' + personStore.selectedPerson.kisi_ad">
        </div>
      </div>
      <div class="row">
        <div class="col-3">
          <label for="fsoyad">Soyad</label>
        </div>
        <div class="col-9">

          <input type="text"  v-model="duzenlenecek_kisi.kisi_soyad"
                 :placeholder="'Şuan ki soyad: ' + personStore.selectedPerson.kisi_soyad">
        </div>
      </div>
      <div class="row">
        <div class="col-3">
          <label for="ftelefon">Telefon</label>
        </div>
        <div class="col-9">
          <input type="text" v-model="duzenlenecek_kisi.telefon"
                 :placeholder="'Şuan ki telefon: ' + personStore.selectedPerson.telefon">
        </div>
      </div>
      <div class="row">
        <div class="col-3">
          <label for="femail">Email</label>
        </div>
        <div class="col-9">
          <input type="text" id="femail" name="email" v-model="duzenlenecek_kisi.email"
                 :placeholder="'Şuan ki email: ' + personStore.selectedPerson.email">
        </div>
      </div>
      <div class="row">
        <div class="col-3">
          <label for="adres">Adres</label>
        </div>
        <div class="col-9">
          <input type="text" v-model="duzenlenecek_kisi.adres"
                 :placeholder="'Şuan ki adres: ' + personStore.selectedPerson.adres">
        </div>
      </div>


      <div class="right">
        <button class="btn" @click="duzenle">
          <font-awesome-icon icon="fa-solid fa-paper-plane"/>
          Yolla
        </button>
      </div>

    </div>
    <div class="col-1"></div>
  </div>


</template>


<style scoped>


</style>