import {
  SIGN_IN,
  SIGN_OUT,
  SET_AUTH_STATE,
  GET_ALL_LEAGUES,
  GET_LEAGUE,
  SET_LEAGUE,
  GET_SCORES,
  GET_MATCHES,
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
  const response = await BackEnd.get("/api/league");

  dispatch({
    type: GET_ALL_LEAGUES,
    payload: response.data,
  });
};

export const getLeague = (league_id) => async (dispatch) => {
  const response = await BackEnd.get(`/api/league/${league_id}`);

  dispatch({
    type: GET_LEAGUE,
    payload: response.data,
  });
};

export const setLeague = (league_id, league) => async (dispatch) => {
  const response = await BackEnd.put(`/api/league/${league_id}`, league);

  dispatch({
    type: SET_LEAGUE,
    payload: response.data,
  });
};

export const getScores = (id) => async (dispatch) => {
  const response = await BackEnd.get(`/api/league/${id}/getscores`);

  dispatch({
    type: GET_SCORES,
    payload: response.data,
  });
};

export const getMatches = () => async (dispatch) => {
  const response = await BackEnd.get("/api/match");

  dispatch({
    type: GET_MATCHES,
    payload: response.data,
  });
};
