<script setup>


import {useLoadingState} from "@/stores/loading_state";

import {usePersonState} from "@/stores/person_state";
import KisiDuzenlemeComponent from "@/components/KisiDuzenlemeComponent.vue";

const load = useLoadingState();

const personStore = usePersonState()



personStore.yukle()

</script>

<template>

  <div class="row">
    <div class="col-1"></div>
    <div class="col-10">
      <div class="loader" v-if="load.loading"></div>
      <div class="col-12">
        <h1>Kisiler</h1>
        <hr class="style">

        <table>
          <tr>
            <th> <font-awesome-icon icon="fa-solid fa-hashtag" /></th>
            <th><font-awesome-icon icon="fa-solid fa-circle" /> Müşteri Ad</th>
            <th><font-awesome-icon icon="fa-solid fa-square" /> Müşteri Soyad</th>
            <th><font-awesome-icon icon="fa-solid fa-phone" /> Telefon</th>
            <th><font-awesome-icon icon="fa-solid fa-inbox" />  Email</th>
            <th><font-awesome-icon icon="fa-solid fa-map-location-dot" /> Adres</th>
            <th><button class="btn white right" @click="personStore.yukle()"><font-awesome-icon icon="fa-solid fa-arrows-rotate" /> Yenile</button></th>
          </tr>
          <div class="col-12" v-if="personStore.persons.length === 0">Kişi Bulunamadı kişi eklenmesi gerekiyor.</div>
          <tr v-for="person in personStore.persons">

            <td>{{ person["kisi_id"] }}</td>
            <td>{{ person["kisi_ad"] }}</td>
            <td>{{ person["kisi_soyad"] }}</td>
            <td>{{ person["telefon"] }}</td>
            <td>{{ person["email"] }}</td>
            <td>{{ person["adres"] }}</td>
            <td class="right">
              <button class="btn" @click="personStore.selectedPerson=person"><font-awesome-icon icon="fa-solid fa-pen-to-square" /> Düzenle</button>
            </td>
          </tr>
        </table>
        <br class="space">

        <br class="space">


      </div>
    </div>
    <div class="col-1"></div>
  </div>

  <KisiDuzenlemeComponent></KisiDuzenlemeComponent>


</template>


<style scoped>
/* Table */




table {
  border-collapse: collapse;
  border-spacing: 0;
  width: 100%;
  /* border: 1px solid #d4d4d4; */
}

th {
  background-color: #161612;
  color: #f2f2f2;
}

th, td {

  text-align: left;
  padding: 16px;
  transition: all 300ms ease-out;
}

tr:nth-child(even) {
  background-color: #f2f2f2;
}

/* ---Table */







</style>