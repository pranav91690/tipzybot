import { Route, Link, Redirect } from "react-router-dom";
import Loading from "../util/Loading";

const PrivateRoute = (props) => {
  // if (props.isSignedIn !== null){
  if (props.isSignedIn) {
    return <Route {...props} />;
  } else {
    if (props.path == "/login") {
      return <Route {...props} />;
    } else {
      // return <Link to={{pathname:"/login",state:{referrer : props.location.pathname}}}>Log In</Link>
      return (
        <Redirect
          to={{
            pathname: "/login",
            state: { referrer: props.location.pathname },
          }}
        />
      );
    }
  }
  // }else{
  //     return <Loading></Loading>
  // }
};

export default PrivateRoute;
