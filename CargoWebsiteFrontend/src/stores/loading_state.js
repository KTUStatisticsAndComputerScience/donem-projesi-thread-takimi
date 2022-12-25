import {defineStore} from "pinia";
import {ref} from "vue";

export const useLoadingState = defineStore('loading',
    {
        state: () => ({loading : false}),
        actions: {
            yuklemeyeBasla(){
                this.loading = true;
            },
            yuklemeyiBitir(){
                this.loading = false
            }

        },
    });