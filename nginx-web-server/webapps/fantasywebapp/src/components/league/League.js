import React from "react";
import LeagueView from "./LeagueView";
import { useParams, useRouteMatch } from "react-router-dom";

const League = () => {
  let { leagueid } = useParams();
  let { path, url } = useRouteMatch();
  return <LeagueView leagueid={leagueid} path={path} url={url} />;
};

export default League;
