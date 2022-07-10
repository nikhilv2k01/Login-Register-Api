import { Button, Grid, Paper } from "@material-ui/core";
import { Link, useNavigate } from "react-router-dom";
import axios from "axios";
import { useState } from "react";
import FormInput from "./FormInput";

const paperStyle = {
  padding: 20,
  width: 280,
  margin: "20px auto",
};

function Login() {


  const [username, setUsername] = useState('')
  const [password1, setPassword1] = useState('')

  const navigate = useNavigate();

  function handleSubmit() {
    var config = {
      method: 'post',
      url: 'http://127.0.0.1:8000/api/patient/login',
      headers: {
        'Content-Type': 'application/json'
      },
      data: {
        username: username,
        password1: password1,
      }
    };

    axios(config)
      .then(function (response) {
        let result = JSON.stringify(response.data.message)
        let res = result.includes("success")
        console.log(JSON.stringify(response.data));

        if (res === true) {
          navigate('/Home')
        }
      })
      .catch(function (error) {
        console.log(error);
      });


  }


  const inputs = [
    {
      id: 1,
      name: "username/email",
      type: "text",
      placeholder: "Username / E-mail",
      errorMessage: "*Please fill this field",
      required: true,
      value: username,
      onChange: (e) => setUsername(e.target.value),
    },

    {
      id: 2,
      name: "password",
      type: "password",
      placeholder: "Password",
      errorMessage: "*Please fill this field",
      required: true,
      value: password1,
      onChange: (e) => setPassword1(e.target.value),

    },
  ];


  return (
    <div className="app">
      <Grid>
        <Paper style={paperStyle} elevation={10}>
          <Grid style={{ alignItems: "center" }}>
            <center>
              <h3>Login</h3>
            </center>
          </Grid>

          <form>
            {inputs.map((input) => (
              <FormInput
                key={input.id}
                {...input}

              />
            ))}
            <Button
              component={Link}
              to=""
              color="primary"
              variant="contained"
              onClick={handleSubmit}
              style={{ marginTop: 10 }}
            >
              Login
            </Button>
            <p>

              {" "}
              Not a User? <Link to={"/Register"}>Register</Link>{" "}
            </p>
          </form>
        </Paper>
      </Grid>
    </div>
  );
}

export default Login;
