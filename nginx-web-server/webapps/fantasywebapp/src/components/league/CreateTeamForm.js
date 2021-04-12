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
              name="ownerName"
              placeholder="Owner Name"
              validate={required}
            >
              {({ input, meta, placeholder }) => (
                <div class="required field">
                  <label>Owner Name</label>
                  <input {...input} placeholder={placeholder} />
                  {meta.error && meta.touched && (
                    <span style={{ color: "red" }}>{meta.error}</span>
                  )}
                </div>
              )}
            </Field>

            <Field name="teamName" placeholder="Team Name" validate={required}>
              {({ input, meta, placeholder }) => (
                <div class="required field">
                  <label>Team Name</label>
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
