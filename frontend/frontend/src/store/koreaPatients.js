import axios from "axios";
import Vue from "vue";
import router from "@/router";

Vue.use(router);

const state = {
  context: "http://localhost:5000",
  headers: {
    authorization: "JWT fefege..",
    Accept: "application/json",
    "Content-Type": "application/json",
  },
  koreaPatientsList: [],
};

const actions = {
  async korea_patients({ commit }) {
    axios
      .get(state.context)
      .then((response) => {
        commit("KOREA_PATIENTS_COMMIT", response.data);
        router.push("/").catch((error) => {
          if (error.name != "NavigationDuplicated") {
            throw error;
          }
        });
      })
      .catch((error) => {
        console.log(error);
      });
  },
};

const mutations = {
  KOREA_PATIENTS_COMMIT(state, data) {
    state.koreaPatientsList = [];
    data.forEach((item) => {
      state.koreaPatientsList.push({
        deathCnt: item.deathCnt,
        defCnt: item.defCnt,
        name: item.gubun,
        incDec: item.incDec,
        isolClearCnt: item.isolClearCnt,
        isolIngCnt: item.isolIngCnt,
        localOccCnt: item.localOccCnt,
        overFlowCnt: item.overFlowCnt,
        qurRate: item.qurRate,
      });
    });
  },
};

export default {
  name: "koreaPatients",
  namespaced: true,
  state,
  actions,
  mutations,
};
