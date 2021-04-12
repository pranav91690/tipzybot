import React from "react";
import { connect } from "react-redux";
import { getAllLeagues } from "../../actions/index";
import { Link } from "react-router-dom";
import LeagueItemView from "./LeagueItemView";

// We will get the list of actions at later point!!
class LeagueListView extends React.Component {
  componentDidMount() {
    this.props.getAllLeagues();
  }
  // Here will have to create the list of leagues and button to create a new league
  renderLeagues() {
    return this.props.leagues.map((league) => {
      return (
        <div className="item" key={league._id.$oid}>
          <div className="content">
            <LeagueItemView league={league}></LeagueItemView>
          </div>
        </div>
      );
    });
  }

  render() {
    return (
      <div class="ui two column grid">
        <div class="row"></div>
        <div class="row">
          <div class="column">
            {/* <div className="right floated right aligned six wide column"> */}
            <button className="ui button">
              <i className="plus icon" />
              <Link to="/createleague">Create League</Link>
            </button>
            {/* </div> */}
          </div>
        </div>
        <div class="row">
          <div class="column">
            <h2>Leagues</h2>
            <div className="ui list">{this.renderLeagues()}</div>
          </div>
        </div>
      </div>
    );
  }
}

const mapStateToProps = (state) => {
  return { leagues: state.league.leagues };
};

export default connect(mapStateToProps, { getAllLeagues })(LeagueListView);
