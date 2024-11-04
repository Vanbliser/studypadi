// app/store/authStore.js
import { create } from 'zustand';
import { persist, createJSONStorage } from 'zustand/middleware';


const useAuthStore = create(
  persist(
    (set, get) => ({
      accessToken: null,
      refreshToken: null,
      firstName: null,
      login: (accessToken, refreshToken, firstName) => set({ accessToken, refreshToken, firstName }),
      logout: () => set({ accessToken: null, refreshToken: null }),
    }),
    {
      name: 'auth-storage',
      storage: typeof window !== 'undefined' ? createJSONStorage(() => localStorage) : undefined,
    },
  ),
)

export default useAuthStore;
