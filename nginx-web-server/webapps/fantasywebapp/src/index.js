import React from "react";
import ReactDOM from "react-dom";
import App from "./components/App";
import thunk from "redux-thunk";
import "semantic-ui-css/semantic.min.css";

// npm install --save redux react-redux redux-think react-router-dom lodash

// document is an important global object -- this could contain a lot of stuff!!

// There are three important things needed for a Redux Store
// The store itself (called via createStore duh...), the Provider which takes the store and encapsulates the the whole app
// the createStore will take a list of reducers!!...and also a list of any middelware (things like reduc_thunk)
import { createStore, compose, applyMiddleware } from "redux";
import { Provider } from "react-redux";
import reducers from "./reducers";

const composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;

const store = createStore(reducers, composeEnhancers(applyMiddleware(thunk)));

// The encapsulation
ReactDOM.render(
  <Provider store={store}>
    <App />
  </Provider>,
  document.querySelector("#root")
);
