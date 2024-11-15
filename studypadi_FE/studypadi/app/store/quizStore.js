// store/quizStore.js
import { create } from 'zustand';

export const useQuizStore = create((set) => ({
  userAnswers: JSON.parse(localStorage.getItem('userAnswers')) || {},
  timeTaken: 0,
  
  // Function to set user answers and store them in localStorage
  setUserAnswers: (questionId, answer) => {
    set((state) => {
      const updatedAnswers = { ...state.userAnswers, [questionId]: answer };
      localStorage.setItem('userAnswers', JSON.stringify(updatedAnswers));
      return { userAnswers: updatedAnswers };
    });
  },

  // Function to clear answers
  clearAnswers: () => {
    set(() => ({ userAnswers: {}, timeTaken: 0 }));
    localStorage.removeItem('userAnswers'); // Also clear localStorage
  },
  
  // Function to set the time taken
  setTimeTaken: (time) => set(() => ({ timeTaken: time })),
}));

//export const useQuizStore = create((set) => ({
//    userAnswers: JSON.parse(localStorage.getItem('userAnswers')) || {},
//    setUserAnswers: (questionId, answer) => {
//      set((state) => {
//        const updatedAnswers = { ...state.userAnswers, [questionId]: answer };
//        localStorage.setItem('userAnswers', JSON.stringify(updatedAnswers));
//        return { userAnswers: updatedAnswers };
//      });
//    },
//    clearAnswers: () => set(() => ({ userAnswers: {} })),
//    setTimeTaken: (time) => set(() => ({ timeTaken: time })),
//  }));
//



//  // app/store/quizStore.js
//import { create } from 'zustand';
//
//export const useQuizStore = create((set) => ({
//  userAnswers: {},
//  timeTaken: 0,
//  setUserAnswers: (questionId, answer) => 
//    set((state) => ({
//      userAnswers: { ...state.userAnswers, [questionId]: answer },
//    })),
//  setTimeTaken: (time) => set(() => ({ timeTaken: time })),
//}));
