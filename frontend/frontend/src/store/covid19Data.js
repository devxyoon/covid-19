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
  foreignPatientsList: [],
  koreaNewsList: [],
};

const actions = {
  async korea_patients({ commit }, payload) {
    let commitMenu = "";
    switch (payload) {
      case "korean_patient":
        commitMenu = "KOREA_PATIENTS_COMMIT";
        break;
      case "foreign_patient":
        commitMenu = "FOREIGN_PATIENTS_COMMIT";
        break;
      case "korea_news":
        commitMenu = "KOREA_NEWS_COMMIT";
        break;
    }
    axios
      .get(`${state.context}/${payload}`)
      .then((response) => {
        commit(commitMenu, response.data);
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
  FOREIGN_PATIENTS_COMMIT(state, data) {
    state.foreignPatientsList = [];
    data.forEach((item) => {
      state.foreignPatientsList.push({
        natDeathCnt: item.netDeathCnt,
        natDeathRate: item.natDeathRate,
        natDefCnt: item.natDefCnt,
        nationNm: item.nationNm,
      });
    });
  },
  KOREA_NEWS_COMMIT(state, data) {
    state.koreaNewsList = [];
    data.forEach((item) => {
      state.koreaNewsList.push({
        title: item.title,
        link: item.link,
      });
    });
  },
};

export default {
  name: "covid19Data",
  namespaced: true,
  state,
  actions,
  mutations,
};
