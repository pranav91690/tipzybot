import React from "react";
import { connect } from "react-redux";
import { getMatches, getLeague, setLeague } from "../../actions/index";
import {
  Grid,
  Header,
  Tab,
  Dropdown,
  Button,
  Form,
  Input,
  Label,
  Icon,
} from "semantic-ui-react";
import _ from "lodash";

class ManageLeagueView extends React.Component {
  render() {
    const teams = () => {
      return this.state.league
        ? this.state.league.teams.map((team, index) => {
            return {
              key: index,
              text: team.name,
              value: index,
            };
          })
        : [];
    };

    const playerColor = (active) => {
      if (active === 1) {
        return "blue";
      } else {
        return "red";
      }
    };

    const renderDropButton = (index, active) => {
      if (active === 1) {
        return (
          <Button
            icon
            value={index}
            onClick={(e, data) => {
              if (
                this.state.selectedTeam === null ||
                this.selectedMatchDay === null
              ) {
                this.setState({ error: "Select Team And Match" });
                return;
              }

              if (this.state.error) {
                this.setState({ error: "" });
              }

              const league = _.cloneDeep(this.state.league);
              const player =
                league.teams[this.state.selectedTeam].players[data.value];
              player["end"] = this.state.selectedMatchDay + 1;
              player["active"] = 0;
              league.teams[this.state.selectedTeam].players[data.value] =
                player;

              // Add player back to Open
              const player2 = _.cloneDeep(player);
              player2["owner"] = "Open";
              player2["start"] = 0;
              player2["end"] = 100;
              delete player2["active"];
              league.open.push(player2);

              this.setState({ league: league });
            }}
          >
            <Icon color="red" name="cancel" />
          </Button>
        );
      } else {
        return <div></div>;
      }
    };

    const renderDeleteButton = (index, active) => {
      if (active === 0) {
        return (
          <Button
            icon
            value={index}
            onClick={(e, data) => {
              if (
                this.state.selectedTeam === null ||
                this.selectedMatchDay === null
              ) {
                this.setState({ error: "Select Team And Match" });
                return;
              }

              if (this.state.error) {
                this.setState({ error: "" });
              }

              const league = _.cloneDeep(this.state.league);
              const player =
                league.teams[this.state.selectedTeam].players[data.value];
              // Delete player from team
              league.teams[this.state.selectedTeam].players.splice(
                data.value,
                1
              );

              // // Add player back to Open
              // player["owner"] = "Open";
              // player["start"] = 0;
              // player["end"] = 100;
              // delete player["active"];
              // league.open.push(player);

              this.setState({ league: league });
            }}
          >
            <Icon color="black" name="trash" />
          </Button>
        );
      } else {
        return <div></div>;
      }
    };
    const players = () => {
      if (!(this.state.selectedTeam == null)) {
        return this.state.league.teams[this.state.selectedTeam].players.map(
          (player, index) => {
            return (
              <Grid.Row divided index={index}>
                <Grid.Column width={6}>
                  <Label color={playerColor(player.active)} size="large">
                    {player.name}
                  </Label>
                </Grid.Column>
                <Grid.Column>{player.start}</Grid.Column>
                <Grid.Column>{player.end}</Grid.Column>
                <Grid.Column width={1}>
                  {renderDropButton(index, player.active)}
                </Grid.Column>

                <Grid.Column width={1}>
                  {renderDeleteButton(index, player.active)}
                </Grid.Column>
              </Grid.Row>
            );
          }
        );
      } else {
        return <div></div>;
      }
    };

    const playersToAdd = () => {
      return this.state.league.open.map((player, index) => {
        return {
          key: index,
          text: player["name"],
          value: index,
        };
      });
    };

    const matches = () => {
      return this.props.matches.map((match, index) => {
        return {
          key: index,
          text: match["number"],
          value: index,
        };
      });
    };

    const renderSaveReponse = () => {
      if (this.props.response) {
        return (
          <Button icon>
            <Icon color="green" name="check" />
          </Button>
        );
      } else {
        return <div></div>;
      }
    };

    const renderForm = () => {
      return (
        <Form>
          <Grid container={true}>
            <Grid.Row></Grid.Row>
            <Grid.Row></Grid.Row>
            <Grid.Row>
              <Grid.Column>
                <Header as="h4">
                  Manage "
                  {this.state.league ? this.state.league.name : "Loading.."}"
                </Header>
              </Grid.Column>
            </Grid.Row>
            <Grid.Row>
              <Grid.Column width={6}>
                <Form.Dropdown
                  placeholder="Team"
                  fluid
                  selection
                  options={teams()}
                  onChange={(e, data) => {
                    this.setState({ selectedTeam: data.value });
                  }}
                />
              </Grid.Column>
              <Grid.Column width={6}>
                <Form.Dropdown
                  placeholder="Match Day"
                  fluid
                  selection
                  options={matches()}
                  onChange={(e, data) => {
                    this.setState({ selectedMatchDay: data.value });
                  }}
                />
              </Grid.Column>
            </Grid.Row>
            <Grid.Row>
              <Grid.Column width={6}>
                <Form.Dropdown
                  placeholder="Player"
                  fluid
                  selection
                  search
                  label="Add Player"
                  options={playersToAdd()}
                  onChange={(e, data) => {
                    this.setState({ selectedPlayer: data.value });
                  }}
                />
              </Grid.Column>
              <Grid.Column verticalAlign="bottom">
                <Button
                  color="blue"
                  size="large"
                  onClick={() => {
                    if (
                      this.state.selectedTeam === null ||
                      this.selectedMatchDay === null ||
                      this.state.selectedPlayer === null
                    ) {
                      this.setState({ error: "Select Team,Match and Player" });
                      return;
                    }

                    if (this.state.error) {
                      this.setState({ error: "" });
                    }

                    const league = _.cloneDeep(this.state.league);
                    const player = league.open[this.state.selectedPlayer];
                    player["active"] = 1;
                    player["start"] = this.state.selectedMatchDay + 1;
                    player["owner"] =
                      league.teams[this.state.selectedTeam].name;
                    league.open.splice(this.state.selectedPlayer, 1);
                    league.teams[this.state.selectedTeam].players.push(player);
                    this.setState({ league: league });
                  }}
                >
                  Add
                </Button>
              </Grid.Column>
            </Grid.Row>
            <Grid.Row></Grid.Row>
            <Grid.Row>
              <Grid.Column verticalAlign="middle">
                <Header as="h4">Players</Header>
              </Grid.Column>
              <Grid.Column>
                <Button
                  icon
                  onClick={() => {
                    const league = _.cloneDeep(this.state.league);
                    delete league["_id"];
                    this.props.setLeague(this.props.leagueid, league);
                  }}
                >
                  <Icon color="black" name="save" />
                </Button>
              </Grid.Column>
              <Grid.Column>{renderSaveReponse()}</Grid.Column>
            </Grid.Row>
            {players()}
            <Grid.Row>
              <Grid.Column>{this.state.error}</Grid.Column>
            </Grid.Row>
          </Grid>
        </Form>
      );
    };

    return this.state.league ? renderForm() : <div>Loading</div>;
  }

  constructor(props) {
    super(props);
    this.state = {
      selectedTeam: null,
      selectedPlayer: null,
      selectedMatchDay: null,
      error: "",
      league: null,
    };
  }

  componentDidMount() {
    this.props.getLeague(this.props.leagueid);
    this.props.getMatches();
  }

  componentDidUpdate() {
    if (this.state.league === null && this.props.league) {
      this.setState({ league: this.props.league });
    }
  }
}

const mapStateToProps = (state) => {
  return {
    matches: state.league.matches,
    league: state.league.current_league,
    response: state.league.response,
  };
};

export default connect(mapStateToProps, { getLeague, getMatches, setLeague })(
  ManageLeagueView
);
