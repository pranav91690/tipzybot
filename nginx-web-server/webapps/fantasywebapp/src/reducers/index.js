import { combineReducers } from "redux";
import authReducer from "./authReducer";
import leagueReducer from "./leagueReducer";
import scoresReducer from "./scoresReducer";

export default combineReducers({
  auth: authReducer,
  league: leagueReducer,
  scores: scoresReducer,
});
