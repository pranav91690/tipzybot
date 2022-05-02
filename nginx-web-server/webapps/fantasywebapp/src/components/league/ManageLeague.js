import React from "react";
import ManageLeagueView from "./ManageLeagueView";
import { useParams, useRouteMatch } from "react-router-dom";

const ManageLeague = () => {
  let { leagueid } = useParams();
  let { path, url } = useRouteMatch();
  console.log(leagueid, path, url);
  return <ManageLeagueView leagueid={leagueid} path={path} url={url} />;
};

export default ManageLeague;
