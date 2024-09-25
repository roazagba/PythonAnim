import axios from "axios";
import { useStore } from "vuex";
import { useRouter } from "vue-router"

const store = useStore()
const router = useRouter()

const axiosUser = axios.create({
  baseURL: import.meta.env.VITE_APP_URL
})

axiosUser.interceptors.request.use(config => {
  config.headers.Authorization = `Bearer ${localStorage.getItem('token')}`
  return config;
})

axiosUser.interceptors.response.use(
  (res) => {
    return res;
  },
  (error) => {
    if (error.response.status === 401) {
      localStorage.clear()

      window.location.href = "/connexion"
      toast.fire({
        icon: 'warning',
        title: "Votre session a expiré. Vous êtes automatiquement déconnecté"
      })
    }
    return Promise.reject(error);
  }
)

export default axiosUser;