import {
  SIGN_IN,
  SIGN_OUT,
  SET_AUTH_STATE,
  GET_ALL_LEAGUES,
  GET_LEAGUE,
  SET_LEAGUE,
  GET_SCORES,
} from "./types";
import BackEnd from "../api/BackEnd";

// Action has a payload and type

export const signIn = (user) => {
  return {
    type: SIGN_IN,
    payload: {
      user: user,
    },
  };
};

export const signOut = () => {
  return {
    type: SIGN_OUT,
  };
};

export const setAuthState = (authState) => {
  return {
    type: SET_AUTH_STATE,
    payload: {
      authState: authState,
    },
  };
};

export const getAllLeagues = () => async (dispatch) => {
  const response = await BackEnd.get("api/leagues");

  dispatch({
    type: GET_ALL_LEAGUES,
    payload: response.data,
  });
};

export const getLeague = (league_id) => async (dispatch) => {
  const response = await BackEnd.get(`api/league/${league_id}`);

  dispatch({
    type: GET_LEAGUE,
    payload: response.data,
  });
};

export const setLeague = (league) => {
  return {
    type: SET_LEAGUE,
    payload: league,
  };
};

export const getScores = () => async (dispatch) => {
  const response = await BackEnd.get("api/getscores");

  dispatch({
    type: GET_SCORES,
    payload: response.data,
  });
};
