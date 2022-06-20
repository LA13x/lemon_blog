import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    user: {
      username: window.localStorage.getItem('user' || '[]') == null ? '' : window.localStorage.getItem('user' || '[]')
    }
  },
  mutations: {
    login (state, user) {
      state.user = user
      window.localStorage.setItem('user', user.username)
    }
  }
})
