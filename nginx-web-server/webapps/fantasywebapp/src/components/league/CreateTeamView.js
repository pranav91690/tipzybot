import React from "react";
import CreateTeamForm from "./CreateTeamForm";
import BackEnd from "../../api/BackEnd";
import { useHistory } from "react-router-dom";

// When this form is submitted, we will send a axios request back to our
// db to submit it
// Ideally this should have the league id as well...lets get it to it later!!

const CreateTeamView = () => {
  let history = useHistory();

  // Once the form submission is successful, go in history once!!
  const onSubmit = async (values) => {
    const json_values = JSON.stringify(values);
    await BackEnd.post("/createteam", json_values).then(
      (response) => {
        history.goBack(1);
      },
      (error) => {
        window.alert(error);
      }
    );
  };

  return (
    <div class="ui two column centered grid">
      <div class="row">
        <div class="column">
          <h2>Create Team ...</h2>
        </div>
      </div>
      <div class="row">
        <div class="column">
          <CreateTeamForm onSubmit={onSubmit}></CreateTeamForm>
        </div>
      </div>
    </div>
  );
};

export default CreateTeamView;
