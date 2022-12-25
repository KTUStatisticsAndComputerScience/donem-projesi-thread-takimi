import {defineStore} from "pinia";
import {useLoadingState} from "@/stores/loading_state";
import axios from "axios";


export const usePersonState = defineStore('kisi',
    {
        state: () => ({
            persons: [],
            selectedPerson: null
        }),
        actions: {
            yukle() {
                const load = useLoadingState();
                load.yuklemeyeBasla()
                axios.get('http://127.0.0.1:5000/api/v1/kisi/').then((response) => {
                    this.persons = response.data;
                    load.yuklemeyiBitir()
                })
            },
            kisiBul(id) {
                for (let i = 0; i < this.persons.length; i++) {

                    if (this.persons[i].kisi_id === id) {
                        return this.persons[i].kisi_ad + " " + this.persons[i].kisi_soyad
                    }
                }
            },
            kisiEkle(kisi) {
                axios.post('http://127.0.0.1:5000/api/v1/kisi/', kisi).then((response) => {
                    const kisi = response.data;
                    this.persons.push(kisi);
                })
            },
            kisiDuzenle(kisi, kisi_id) {
                axios.put('http://127.0.0.1:5000/api/v1/kisi/' + kisi_id, kisi).then((response) => {
                    const kisi = response.data;
                    this.persons.push(kisi);
                    this.yukle();
                })
            }
        }
    })