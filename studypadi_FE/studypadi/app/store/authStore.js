// app/store/authStore.js
import { create } from 'zustand';

const useAuthStore = create((set) => ({
    accessToken: null,
    refreshToken: null,
    login: (accessToken, refreshToken, firstName) => set({ accessToken, refreshToken, firstName }),
    logout: () => set({ accessToken: null, refreshToken: null, firstname: null }),
}));

export default useAuthStore;
