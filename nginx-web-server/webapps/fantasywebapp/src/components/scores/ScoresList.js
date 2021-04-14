import React from "react";
import { connect } from "react-redux";
import { getScores } from "../../actions/index";

class ScoresList extends React.Component {
  render() {
    const sorted_scores = this.props.current_score.sort(
      (a, b) => parseInt(b.points) - parseInt(a.points)
    );
    const scores = sorted_scores.map((score) => {
      return (
        <tr key={score.owner}>
          <td class="left aligned">{score.owner}</td>
          <td class="right aligned">{score.points}</td>
        </tr>
      );
    });

    const map = {
      1: "Operation Kill Sree",
      2: "The OG",
    };

    const customMessage = {
      1: "Hope Sree Crashes and Burns",
      2: "Kothari is a fat bastard",
    };

    return (
      <div class="ui one column grid container">
        <div class="row"></div>
        <div class="row"></div>
        <div class="row">
          <h2>{map[this.props.leagueid]}</h2>
        </div>
        <div class="row"></div>
        <div class="row">
          <div class="column">
            <table class="ui unstackable table">
              <thead>
                <tr>
                  <th class="left aligned">Owner</th>
                  <th class="right aligned">Points</th>
                </tr>
              </thead>
              <tbody>{scores}</tbody>
              <tfoot>
                <tr>
                  <th>{customMessage[this.props.leagueid]}</th>
                  <th></th>
                </tr>
              </tfoot>
            </table>
          </div>
        </div>
        <div class="row"></div>
        <div class="row"></div>
        <div class="row"></div>
      </div>
    );
  }

  componentDidMount() {
    this.props.getScores(this.props.leagueid);
  }
}

const mapStateToProps = (state) => {
  return {
    current_score: state.scores.current_score,
  };
};

export default connect(mapStateToProps, { getScores })(ScoresList);
