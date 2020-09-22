import Vue from "vue";
import App from "./App.vue";
import Vuex from "vuex";
import axios from "axios";
import router from "./router";
import { store } from "./store";

Vue.config.productionTip = false;
Vue.prototype.$http = axios;
Vue.use(Vuex);

new Vue({
  Vuex,
  axios,
  router,
  store,
  render: (h) => h(App),
}).$mount("#app");
