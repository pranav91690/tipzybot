import {
  GET_ALL_LEAGUES,
  GET_LEAGUE,
  SET_LEAGUE,
  GET_MATCHES,
} from "../actions/types";

const INITIAL_STATE = {
  leagues: [],
  matches: [],
  current_league: null,
  response: null,
};

export default (state = INITIAL_STATE, action) => {
  switch (action.type) {
    case GET_ALL_LEAGUES:
      return { ...state, leagues: action.payload };

    case GET_LEAGUE:
      return { ...state, current_league: action.payload };

    case SET_LEAGUE:
      return { ...state, response: action.payload };

    case GET_MATCHES:
      return { ...state, matches: action.payload };

    default:
      return state;
  }
};
