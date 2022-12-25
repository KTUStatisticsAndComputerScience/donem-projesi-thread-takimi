import {defineStore} from "pinia";
import {useLoadingState} from "@/stores/loading_state";
import axios from "axios";


export const useCargoState = defineStore('cargo',
    {
        state: () => ({
            kargolar: [],
            selectedCargo: null
        }),
        actions: {
            yukle() {
                const load = useLoadingState();

                load.yuklemeyeBasla();
                this.selectedCargo = null;
                axios.get('http://127.0.0.1:5000/api/v1/kargo/').then((response) => {
                    this.kargolar = response.data;
                    load.yuklemeyiBitir()
                })
            },
            kargoEkle(kargo) {
                axios.post('http://127.0.0.1:5000/api/v1/kargo/', kargo).then((response) => {
                    const kargo = response.data;
                    console.log(kargo);
                    this.yukle();
                })
            },
            kargoDuzenle(kargo, kargo_id) {
                axios.put('http://127.0.0.1:5000/api/v1/kargo/' + kargo_id, kargo).then((response) => {
                    const kargo = response.data;
                    console.log(kargo);
                    this.yukle();
                })
            },
            kargoSil(kargo) {

                axios.delete('http://127.0.0.1:5000/api/v1/kargo/' + kargo["kargo_id"]).then((response) => {
                    const kargo = response.data;
                    console.log(kargo);
                    this.yukle();
                })
            }
        }
    });