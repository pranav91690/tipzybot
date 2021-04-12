import { GET_ALL_LEAGUES, GET_LEAGUE, SET_LEAGUE } from "../actions/types";

const INITIAL_STATE = {
  leagues: [],
  current_league: null,
};

export default (state = INITIAL_STATE, action) => {
  switch (action.type) {
    case GET_ALL_LEAGUES:
      return { ...state, leagues: action.payload };

    case GET_LEAGUE:
      return { ...state, current_league: action.payload };

    case SET_LEAGUE:
      return { ...state, current_league: action.payload };

    default:
      return state;
  }
};
