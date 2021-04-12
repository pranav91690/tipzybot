// Every reducer will have a set of actions to define logic for!
// Then we have the initial state!! <-- this is what we will access every time. THe actual data we are interested in
// The the final function which will take the state and an action <-- this is the core reducer functopm
import { SIGN_IN, SIGN_OUT, SET_AUTH_STATE } from "../actions/types";

// Initializer state for our state object
const INITIAL_STATE = {
  isSignedIn: null,
  userId: null,
  auth_token: null,
};

export default (state = INITIAL_STATE, action) => {
  switch (action.type) {
    case SIGN_IN:
      return {
        ...state,
        isSignedIn: true,
        userId: action.payload.userId,
        auth_token: action.payload.auth_token,
      };

    case SIGN_OUT:
      return { ...state, isSignedIn: false, userId: null, auth_token: null };

    case SET_AUTH_STATE:
      return {
        ...state,
        isSignedIn: action.payload.authState.isSignedIn,
        userId: action.payload.authState.userId,
        auth_token: action.payload.authState.auth_token,
      };
    default:
      return state;
  }
};
