import React from "react";
import { connect } from "react-redux";
import { getScores } from "../../actions/index";
import "./ScoresList.css";
import { Accordion, Icon, Item, Table } from "semantic-ui-react";
import _ from "lodash";

class ScoresList extends React.Component {
  state = { activeIndex: -1 };

  handleClick = (e, titleProps) => {
    const { index } = titleProps;
    const { activeIndex } = this.state;
    const newIndex = activeIndex === index ? -1 : index;

    this.setState({ activeIndex: newIndex });
  };

  render() {
    const sorted_scores = this.props.current_score.sort(
      (a, b) => parseInt(b.points) - parseInt(a.points)
    );

    const detailedScore = (players) => {
      const playerList = Object.keys(players).map((key) => players[key]);

      const sortedPlayers = playerList.sort(
        (a, b) => parseInt(b.points) - parseInt(a.points)
      );
      const playersItems = playerList.map((player, index) => {
        return (
          <Table.Row key={index}>
            <Table.Cell>{_.startCase(_.toLower(player.name))}</Table.Cell>
            <Table.Cell>{player.points}</Table.Cell>
            <Table.Cell>{player.categories.batting}</Table.Cell>
            <Table.Cell>{player.categories.bowling}</Table.Cell>
            <Table.Cell>{player.categories.fielding}</Table.Cell>
            <Table.Cell>{player.categories.awards}</Table.Cell>
          </Table.Row>
        );
      });

      return playersItems;
    };

    const scores = sorted_scores.map((score, index) => {
      const { activeIndex } = this.state;
      return (
        <div>
          <Accordion.Title
            active={activeIndex === index}
            index={index}
            onClick={this.handleClick}
          >
            <div class="ui two column grid">
              <div class="column left aligned">
                <Icon name="dropdown" />
                <span>{score.owner}</span>
              </div>
              <div class="column right aligned">
                <span>{score.points}</span>
              </div>
            </div>
          </Accordion.Title>
          <Accordion.Content active={activeIndex === index}>
            <Table size="small" unstackable compact>
              <Table.Header>
                <Table.HeaderCell>Name</Table.HeaderCell>
                <Table.HeaderCell>Points</Table.HeaderCell>
                <Table.HeaderCell>Batting</Table.HeaderCell>
                <Table.HeaderCell>Bowling</Table.HeaderCell>
                <Table.HeaderCell>Fielding</Table.HeaderCell>
                <Table.HeaderCell>Awards</Table.HeaderCell>
              </Table.Header>

              <Table.Body>{detailedScore(score.players)}</Table.Body>
            </Table>
          </Accordion.Content>
        </div>
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
            <Accordion styled fluid>
              {scores}
            </Accordion>
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
