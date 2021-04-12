import { GET_SCORES } from "../actions/types";

const INITIAL_STATE = {
  current_score: [],
};

export default (state = INITIAL_STATE, action) => {
  switch (action.type) {
    case GET_SCORES:
      return { ...state, current_score: action.payload };
    default:
      return state;
  }
};
