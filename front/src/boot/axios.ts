import axios, { AxiosInstance } from 'axios';
import { boot } from 'quasar/wrappers';

import api, { IAPI } from './api'

declare module 'vue/types/vue' {
  interface Vue {
    $axios: AxiosInstance;
    $api: IAPI;
  }
}

export default boot(({ Vue }) => {
  // eslint-disable-next-line @typescript-eslint/no-unsafe-member-access
  Vue.prototype.$axios = axios;
  // eslint-disable-next-line @typescript-eslint/no-unsafe-member-access
  Vue.prototype.$api = api;
});
