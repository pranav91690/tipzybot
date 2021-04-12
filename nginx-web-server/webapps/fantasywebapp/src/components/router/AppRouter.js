import React from "react";
import {
  BrowserRouter as Router,
  Route,
  Switch,
  useRouteMatch,
} from "react-router-dom";
import TeamView from "../team/TeamView";
import CreateLeagueView from "../home/CreateLeagueView";
import CreateTeamView from "../league/CreateTeamView";
import LeagueList from "../home/LeagueList";
import League from "../league/League";
import Scores from "../scores/Scores";

const Leagues = () => {
  let { path, url } = useRouteMatch();

  return (
    <Switch>
      <Route path={`${path}/team/:teamid`}>
        <TeamView />
      </Route>
      <Route path={`${path}/createteam`}>
        <CreateTeamView />
      </Route>
      <Route path={`${path}`}>
        <League />
      </Route>
    </Switch>
  );
};

const AppRouter = (props) => {
  return (
    <Router>
      <Switch>
        <Route path="/league/:leagueid">
          <Leagues />
        </Route>
        <Route path="/createleague">
          <CreateLeagueView />
        </Route>
        <Route path="/getscores">
          <Scores />
        </Route>
        <Route path="/">
          <Scores />
        </Route>
      </Switch>
    </Router>
  );
};

export default AppRouter;
