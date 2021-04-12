import React from "react";
import { connect } from "react-redux";
import { signIn, signOut } from "../../actions";

class GoogleAuth extends React.Component {
  onSignInClick = () => {
    this.auth = window.gapi.auth2.getAuthInstance();
    this.auth.signIn().then((googleUser) => {
      let user = {
        userId: googleUser.getId(),
        auth_token: googleUser.getAuthResponse().id_token,
      };

      this.props.signIn(user);
      this.props.history.push(this.props.from);
    });
  };

  onSignOutClick = () => {
    this.auth = window.gapi.auth2.getAuthInstance();
    this.auth.signOut().then(() => {
      this.props.signOut();
      this.props.history.push("/");
    });
  };

  renderAuthButton() {
    if (!this.props.isSignedIn) {
      return (
        <button className="ui black google button" onClick={this.onSignInClick}>
          <i className="google icon" />
          Sign In with Google
        </button>
      );
    } else {
      return (
        <button
          className="ui black google button"
          onClick={this.onSignOutClick}
        >
          <i className="google icon" />
          Sign Out
        </button>
      );
    }
  }

  render() {
    return <div>{this.renderAuthButton()}</div>;
  }
}

const mapStateToProps = (state) => {
  return {
    isSignedIn: state.auth.isSignedIn,
  };
};

export default connect(mapStateToProps, { signIn, signOut })(GoogleAuth);
