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

  render() {
    const map = {
      1: "Operation Kill Sree",
      2: "The OG",
    };

    const leagues = this.props.leagues.map((league) => {
      return (
        <div class="row" key={league}>
          <div class="column" key={league}>
            <Link to={`/league/${league}`}>{map[league]}</Link>
          </div>
        </div>
      );
    });

    return (
      <div class="ui two column grid container">
        <div class="row"></div>
        <div class="row">
          <h2>Leagues</h2>
        </div>
        {leagues}
      </div>
    );
  }
}

const mapStateToProps = (state) => {
  return { leagues: state.league.leagues };
};

export default connect(mapStateToProps, { getAllLeagues })(LeagueListView);
