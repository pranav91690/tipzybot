import React from "react";
import { connect } from "react-redux";
import { getScores, getLeague } from "../../actions/index";
import "./LeagueView.css";
import { Accordion, Icon, Item, Table, Grid, Button } from "semantic-ui-react";
import { Link } from "react-router-dom";
import _ from "lodash";

class LeagueView extends React.Component {
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

    const detailedScore = (players, condition = 0) => {
      if (condition == 0) {
        condition = Object.keys(players).length;
      }
      const playerList = Object.keys(players).map((key) => players[key]);

      const sortedPlayers = playerList.sort(
        (a, b) => parseInt(b.points) - parseInt(a.points)
      );

      const playersItems = playerList
        .slice(0, condition)
        .map((player, index) => {
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

    const scores = sorted_scores
      .filter((score) => score.owner !== "open")
      .map((score, index) => {
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

    const freeagentscores = sorted_scores
      .filter((score) => score.owner === "open")
      .map((score, index) => {
        return (
          <Table size="small" unstackable compact>
            <Table.Header>
              <Table.HeaderCell>Name</Table.HeaderCell>
              <Table.HeaderCell>Points</Table.HeaderCell>
              <Table.HeaderCell>Batting</Table.HeaderCell>
              <Table.HeaderCell>Bowling</Table.HeaderCell>
              <Table.HeaderCell>Fielding</Table.HeaderCell>
              <Table.HeaderCell>Awards</Table.HeaderCell>
            </Table.Header>

            <Table.Body>{detailedScore(score.players, 25)}</Table.Body>
          </Table>
        );
      });

    return (
      <div class="ui one column grid container">
        <div class="row"></div>
        <div class="row"></div>
        {/* <div class="row">
          <h2>{map[this.props.leagueid]}</h2>
        </div> */}
        <div class="row"></div>
        <div class="row">
          <div class="column">
            <Link to={`${this.props.url}/manage`}>
              <Button>Manage</Button>
            </Link>
          </div>
        </div>
        <div class="row">
          <div class="column">
            <h4>{this.props.league ? this.props.league.name : ""}</h4>
          </div>
        </div>
        <div class="row">
          <div class="column">
            <b>Standings</b>
          </div>
        </div>
        <div class="row">
          <div class="column">
            <Accordion styled fluid>
              {scores}
            </Accordion>
          </div>
        </div>
        <div class="row">
          <div class="column">
            <b>Top 10 Free Agents</b>
          </div>
        </div>
        <div class="row">
          <div class="column">
            <Accordion styled fluid>
              {freeagentscores}
            </Accordion>
          </div>
        </div>

        <div class="row"></div>
        <div class="row"></div>
      </div>
    );
  }

  componentDidMount() {
    this.props.getScores(this.props.leagueid);
    this.props.getLeague(this.props.leagueid);
  }
}

const mapStateToProps = (state) => {
  return {
    current_score: state.scores.current_score,
    league: state.league.current_league,
  };
};

export default connect(mapStateToProps, { getScores, getLeague })(LeagueView);
