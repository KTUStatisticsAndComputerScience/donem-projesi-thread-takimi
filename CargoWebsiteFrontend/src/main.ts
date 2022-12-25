import {createApp} from 'vue'
import {createPinia} from 'pinia'
import App from './App.vue'
import {createRouter, createWebHistory} from 'vue-router'


import {
    faTruck,
    faList,
    faUserPlus,
    faPlus,
    faPaperPlane,
    faPenToSquare,
    faTrash,
    faUpRightAndDownLeftFromCenter,
    faArrowsLeftRight,
    faArrowsUpDown,
    faWeightHanging,
    faCube,
    faCircle,
    faSquare,
    faHashtag,
    faArrowsRotate,
    faChevronRight,
    faChevronLeft,
    faPhone,
    faInbox,
    faMapLocationDot,
    faUsers

} from '@fortawesome/free-solid-svg-icons'

import './assets/main.css'

import {library} from '@fortawesome/fontawesome-svg-core'
import {FontAwesomeIcon} from '@fortawesome/vue-fontawesome'
import KargoListesiComponent from "@/components/KargoListesiComponent.vue";
import KisiListesiComponent from "@/components/KisiListesiComponent.vue";
import KargoEklemeComponent from "@/components/KargoEklemeComponent.vue";
import KisiEklemeComponent from "@/components/KisiEklemeComponent.vue";







library.add(faTruck, faList, faUserPlus, faPlus, faPaperPlane, faPenToSquare, faTrash, faUpRightAndDownLeftFromCenter,
    faArrowsLeftRight, faArrowsUpDown, faWeightHanging, faCube, faCircle, faSquare, faHashtag, faArrowsRotate,
    faChevronRight, faChevronLeft, faPhone, faInbox, faMapLocationDot, faUsers)


const router = createRouter({
    history: createWebHistory(),
    routes: [
        {path: '/', component: KargoListesiComponent},
        {path: '/kargo-ekle', component: KargoEklemeComponent},
        {path: '/kisiler', component: KisiListesiComponent},
        {path: '/kisi-ekle', component: KisiEklemeComponent},

    ]
});

const app = createApp(App)
    .use(createPinia())
    .use(router)
    .component('font-awesome-icon', FontAwesomeIcon)
app.mount('#app')
