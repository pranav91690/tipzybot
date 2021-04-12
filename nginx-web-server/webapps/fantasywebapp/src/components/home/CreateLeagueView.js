import React from "react";
import CreateLeagueForm from "./CreateLeagueForm";
import BackEnd from "../../api/BackEnd";
import { useHistory } from "react-router-dom";

const CreateLeagueView = () => {
  let history = useHistory();

  // When this form is submitted, we will send a axios request back to our
  // db to submit it
  // Ideally this should have the league id as well...lets get it to it later!!
  const onSubmit = async (values) => {
    const json_values = JSON.stringify(values);
    await BackEnd.post("/league", json_values).then(
      (response) => {
        // Go Back by 1 to the leagues page
        history.goBack();
      },
      (error) => {
        // We Should populate the error here and let the user know that we
        // could not create the league
        window.alert(error);
      }
    );
  };

  return (
    <div class="ui two column centered grid">
      <div class="row">
        <div class="column">
          <h2>Create League ...</h2>
        </div>
      </div>
      <div class="row">
        <div class="column">
          <CreateLeagueForm onSubmit={onSubmit}></CreateLeagueForm>
        </div>
      </div>
    </div>
  );
};

export default CreateLeagueView;
