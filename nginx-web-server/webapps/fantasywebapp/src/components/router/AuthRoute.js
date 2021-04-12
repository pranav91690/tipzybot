import { Redirect } from "@reach/router";
import { connect } from "react-redux";
import Login from "./Login";
import LeagueList from "./LeagueList";

const components = {
  login: Login,
  leaguelist: LeagueList,
};

const AuthRoute = (props) => {
  console.log(props);
  const { isSignedIn, path, component } = props;

  if (!isSignedIn && path !== "/login2") {
    return <Redirect from={path} to="/login" />;
  } else {
    const CustomComponent = components[component];
    return <CustomComponent />;
  }
};

const mapStateToProps = (state) => {
  return {
    isSignedIn: state.auth.isSignedIn,
  };
};

export default connect(mapStateToProps)(AuthRoute);
