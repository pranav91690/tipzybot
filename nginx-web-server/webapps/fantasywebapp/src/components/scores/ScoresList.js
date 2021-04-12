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
        <tr>
          <td class="left aligned">{score.owner}</td>
          <td class="right aligned">{score.points}</td>
        </tr>
      );
    });

    return (
      <div class="four column grid">
        <div class="row"></div>
        <div class="row"></div>
        <div class="row"></div>
        <div class="row">
          <div class="column">
            <table class="ui table">
              <thead>
                <tr>
                  <th class="left aligned">Owner</th>
                  <th class="right aligined">Points</th>
                </tr>
              </thead>
              <tbody>{scores}</tbody>
              <tfoot>
                <tr>
                  <th>Hope Sree Crashes and Burns</th>
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
    this.props.getScores();
  }
}

const mapStateToProps = (state) => {
  return {
    current_score: state.scores.current_score,
  };
};

export default connect(mapStateToProps, { getScores })(ScoresList);
