import React from "react";
import { connect } from "react-redux";
import { getLeague } from "../../actions/index";
import { Link } from "react-router-dom";

class LeagueView extends React.Component {
  componentDidMount() {
    this.props.getLeague(this.props.leagueid);
  }

  renderTeams() {
    if (this.props.league !== null) {
      return this.props.league.teams.map((team) => {
        return (
          <div className="item" key={team.id}>
            <div className="content">{team.name}</div>
          </div>
        );
      });
    }
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
              <Link to={`${this.props.url}/createteam`}>Create Team</Link>
            </button>
            {/* </div> */}
          </div>
        </div>
        <div class="row">
          <div class="column">
            <h2>Teams</h2>
            <div className="ui list">{this.renderTeams()}</div>
          </div>
        </div>
      </div>
    );
  }
}

const mapStateToProps = (state) => {
  return {
    league: state.league.current_league,
  };
};

export default connect(mapStateToProps, { getLeague })(LeagueView);
