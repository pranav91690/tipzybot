import React from "react";
import { Form, Field } from "react-final-form";

const CreateLeagueForm = (props) => {
  const { onSubmit } = props;
  const required = (value) => (value ? undefined : "Required");
  return (
    // You can give the fields of the form to be submitted as a child of that component!!
    <Form onSubmit={onSubmit}>
      {({ handleSubmit, values, submitting }) => (
        <form class="ui form" onSubmit={handleSubmit}>
          <div>
            <Field
              name="leagueName"
              placeholder="League Name"
              validate={required}
            >
              {({ input, meta, placeholder }) => (
                <div class="required field">
                  <label>League Name</label>
                  <input {...input} placeholder={placeholder} />
                  {meta.error && meta.touched && (
                    <span style={{ color: "red" }}>{meta.error}</span>
                  )}
                </div>
              )}
            </Field>

            <Field
              name="teams_per_league"
              placeholder="teams per league"
              validate={required}
            >
              {({ input, meta, placeholder }) => (
                <div class="required field">
                  <label>Teams Per League</label>
                  <input {...input} placeholder={placeholder} />
                  {meta.error && meta.touched && (
                    <span style={{ color: "red" }}>{meta.error}</span>
                  )}
                </div>
              )}
            </Field>

            <Field
              name="salarycap"
              placeholder="Salary Cap"
              validate={required}
            >
              {({ input, meta, placeholder }) => (
                <div class="required field">
                  <label>Salary Cap (In Crores) Per Team</label>
                  <input {...input} placeholder={placeholder} />
                  {meta.error && meta.touched && (
                    <span style={{ color: "red" }}>{meta.error}</span>
                  )}
                </div>
              )}
            </Field>

            <button class="ui button" type="submit">
              Submit
            </button>
          </div>
        </form>
      )}
    </Form>
  );
};

export default CreateLeagueForm;
