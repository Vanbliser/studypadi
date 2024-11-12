import {create} from 'zustand';

export const useQuizStore = create((set) => ({
    userAnswers: JSON.parse(localStorage.getItem('userAnswers')) || {},
    setUserAnswers: (questionId, answer) => {
      set((state) => {
        const updatedAnswers = { ...state.userAnswers, [questionId]: answer };
        localStorage.setItem('userAnswers', JSON.stringify(updatedAnswers));
        return { userAnswers: updatedAnswers };
      });
    },
    clearAnswers: () => set(() => ({ userAnswers: {} })),
    setTimeTaken: (time) => set(() => ({ timeTaken: time })),
  }));

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
