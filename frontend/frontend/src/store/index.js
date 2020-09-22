import Vue from "vue";
import Vuex from "vuex";
import covid19Data from "./covid19Data";

Vue.use(Vuex);

export const store = new Vuex.Store({
  modules: {
    covid19Data,
  },
});
