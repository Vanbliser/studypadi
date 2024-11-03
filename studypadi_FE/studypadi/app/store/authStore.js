// app/store/authStore.js
import { create } from 'zustand';


const useAuthStore = create((set) => ({
  accessToken: null,
  refreshToken: null,
  login: (accessToken, refreshToken) => set({ accessToken, refreshToken }),
  logout: () => set({ accessToken: null, refreshToken: null }),
}));
export default useAuthStore;
