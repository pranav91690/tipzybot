import React from "react";
import { signIn, setAuthState } from "../actions";
import { connect } from "react-redux";
import AppRouter from "./router/AppRouter";
import Loading from "./util/Loading";

// This is a function based component
// Ideally if the user is signed In, display the home page or the previous saved state, whatever!!
// The previously loaded state will come from te backend as a JSON -- Duh!!
// We'll also need a mapStateToProps here

// So what properties does the app have
// User Details and Whether User is signed in or not??

class App extends React.Component {
  componentDidMount() {}

  render() {
    // For now lets skip the login flow
    // if (this.props.isSignedIn == null){
    //     return <Loading></Loading>
    // }else{
    //     return <AppRouter isSignedIn={this.props.isSignedIn}></AppRouter>
    // }
    console.log("App Loaded");
    return (
      <div class="ui container">
        <AppRouter></AppRouter>
      </div>
    );
  }
}

const mapStateToProps = (state) => {
  return {
    isSignedIn: state.auth.isSignedIn,
  };
};

export default connect(mapStateToProps, { signIn, setAuthState })(App);
