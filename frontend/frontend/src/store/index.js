import Vue from "vue";
import Vuex from "vuex";
import koreaPatients from "./koreaPatients";

Vue.use(Vuex);

export const store = new Vuex.Store({
  modules: {
    koreaPatients,
  },
});
