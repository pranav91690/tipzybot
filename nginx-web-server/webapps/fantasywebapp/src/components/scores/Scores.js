import React from "react";
import ScoresList from "./ScoresList";
import { useParams, useRouteMatch } from "react-router-dom";

const Scores = () => {
  let { leagueid } = useParams();
  let { path, url } = useRouteMatch();
  return <ScoresList leagueid={leagueid} path={path} url={url} />;
  // return <ScoresList />;
};

export default Scores;
