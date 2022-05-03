import React from "react";
import ChartRace from "react-chart-race";
import { Grid, Label, Button } from "semantic-ui-react";

class BarChartRace extends React.Component {
  constructor(props) {
    super(props);
    // console.log(props.data);
    // console.log(props.data.length);
    this.state = {
      data: [],
      matchNum: 0,
      intervalRunning: 1,
    };
    this.startAnimationInterval = setInterval(() => {
      this.startAnimation();
    }, 500);
  }

  startAnimation = () => {
    const data = this.props.data[this.state.matchNum];
    this.setState({ data: data, matchNum: this.state.matchNum + 1 });
    if (this.state.matchNum == this.props.data.length) {
      clearInterval(this.startAnimationInterval);
      this.setState({ intervalRunning: 0 });
    }
  };

  render() {
    if (this.props.data) {
      return (
        <Grid container>
          <Grid.Row></Grid.Row>
          <Grid.Row>
            <Grid.Column width={11}>
              <Label>Match Number {this.state.matchNum}</Label>
            </Grid.Column>
            <Grid.Column textAlign="right" width={1}>
              <Button
                size="tiny"
                onClick={() => {
                  this.setState({ matchNum: 0, intervalRunning: 1 });
                  this.startAnimationInterval = setInterval(() => {
                    this.startAnimation();
                  }, 500);
                }}
                disabled={this.state.intervalRunning}
              >
                Replay
              </Button>
            </Grid.Column>
          </Grid.Row>
          <Grid.Row>
            <Grid.Column width={12}>
              <ChartRace
                data={this.state.data}
                backgroundColor="#FFFFFF"
                width={760}
                padding={0}
                itemHeight={58}
                gap={12}
                titleStyle={{ font: "normal 400 13px Arial", color: "#000" }}
                valueStyle={{
                  font: "normal 400 11px Arial",
                  color: "rgba(0,0,0, 0.42)",
                }}
              />
            </Grid.Column>
          </Grid.Row>
          <Grid.Row></Grid.Row>
        </Grid>
      );
    } else {
      return <div></div>;
    }
  }
}

export default BarChartRace;
