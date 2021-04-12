import React from "react";
import { Link } from "react-router-dom";

const LeagueItemView = ({ league }) => {
  console.log(league);
  return (
    <div class="row">
      <div>
        <Link to={`/league/${league._id.$oid}`}>{league.leagueName}</Link>
      </div>
      <div>{league.teams_per_league}</div>
      <div>{league.salarycap}</div>
    </div>
  );
};

export default LeagueItemView;
