import React from "react";
import GoogleAuth from "./auth/GoogleAuth";
import { Link } from "react-router-dom";

const Login = (props) => {
  const referrer =
    typeof props.location.state == "undefined"
      ? "/"
      : props.location.state.referrer;
  return (
    <div>
      <div class="ui three column centered grid">
        <div class="row"></div>
        <div class="row">
          <div class="column">
            <GoogleAuth history={props.history} from={referrer}></GoogleAuth>
          </div>
        </div>
        <div class="row">
          <div class="column">
            <Link to="/">Go Back To Home</Link>
          </div>
        </div>
        <div class="row"></div>
      </div>
    </div>
  );
};

export default Login;
