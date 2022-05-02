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
import ManageLeague from "../league/ManageLeague";
import LeagueList from "../home/LeagueList";
import League from "../league/League";

const Leagues = () => {
  let { path } = useRouteMatch();
  return (
    <Switch>
      {/* <Route path={`${path}/team/:teamid`}>
        <TeamView />
      </Route>
      <Route path={`${path}/createteam`}>
        <CreateTeamView />
      </Route> */}
      <Route path={`${path}/manage`}>
        <ManageLeague />
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
        {/* <Route path="/createleague">
          <CreateLeagueView />
        </Route> */}
        <Route exact path="/">
          <LeagueList />
        </Route>
      </Switch>
    </Router>
  );
};

export default AppRouter;
