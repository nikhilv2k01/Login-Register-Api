import { useState } from "react";
import FormInput from "./FormInput";
import { Button, Grid, Paper } from "@material-ui/core";
import axios from 'axios'
import { Link, useNavigate } from "react-router-dom";
const paperStyle = {
  padding: 20,

  width: 280,
  margin: "20px auto",
};
const Register = () => {

  const [firstname, setFirstname] = useState('')
  const [lastname, setLastname] = useState('')
  const [username, setUsername] = useState('')
  const [email, setEmail] = useState('')
  const [phone_number, setPhonenumber] = useState('')
  const [password1, setPassword1] = useState('')
  const [password2, setPassword2] = useState('')

  // console.log({firstname,lastname,username,email,phone_number,password1,password2})

  // var data = JSON.stringify({
  //   "firstname": "patient",
  //   "lastname": "6",
  //   "username": "patient6",
  //   "email": "patient6@gmail.com",
  //   "phone_number": "1234567890",
  //   "password1": "patient",
  //   "password2": "patient"
  // });

  const navigate = useNavigate();

  // submit

  function handleSubmit() {
    var config = {
      method: 'post',
      url: 'http://127.0.0.1:8000/api/patient/register',
      headers: {
        'Content-Type': 'application/json'
      },
      data: {
        firstname: firstname,
        lastname: lastname,
        username: username,
        email: email,
        phone_number: phone_number,
        password1: password1,
        password2: password2
      }
    };

    axios(config)
      .then(function (response) {
        let result = JSON.stringify(response.data.message)
        let res = result.includes("success")
        console.log(JSON.stringify(response.data));
        if (res === true) {
          alert("Registered successfully")
          navigate('/')
        }
      })
      .catch(function (error) {
        console.log(error);
      });
  }




  const inputs = [
    {
      id: 1,
      name: "firstname",
      type: "text",
      placeholder: "Firstname",
      errorMessage:
        "Firstname should be 3-16 characters and shouldn't include any special character!",
      label: "Firstname",
      pattern: "^[A-Za-z]{3,16}$",
      required: true,
      value: firstname,
      onChange: (e) => setFirstname(e.target.value),
    },
    {
      id: 2,
      name: "lastname",
      type: "text",
      placeholder: "Lastname",
      errorMessage:
        "Lastname should be 1-15 characters and shouldn't include any special character!",
      label: "Lastname",
      pattern: "^[A-Za-z]{1,15}$",
      required: true,
      value: lastname,
      onChange: (e) => setLastname(e.target.value),
    },
    {
      id: 3,
      name: "username",
      type: "text",
      placeholder: "Username",
      errorMessage:
        "Username should be 3-10 characters and shouldn't include any special character!",
      label: "Username",
      pattern: "^[A-Za-z0-9]{3,16}$",
      required: true,
      value: username,
      onChange: (e) => setUsername(e.target.value),
    },
    {
      id: 4,
      name: "email",
      type: "email",
      placeholder: "Email",
      errorMessage: "It should be a valid email address!",
      label: "Email",
      required: true,
      value: email,
      onChange: (e) => setEmail(e.target.value),
    },

    {
      id: 5,
      name: "phonenumber",
      type: "tel",
      placeholder: "Phonenumber",
      errorMessage: "It should be a valid phonenumber!",
      label: "Phonenumber",
      required: true,
      value: phone_number,
      onChange: (e) => setPhonenumber(e.target.value),
    },

    {
      id: 6,
      name: "password",
      type: "password",
      placeholder: "Password",
      errorMessage:
        "Password should be 8-10 characters and include at least 1 letter, 1 number and 1 special character!",
      label: "Password",
      // pattern: `^(?=.[0-9])(?=.[a-zA-Z])(?=.[!@#$%^&])[a-zA-Z0-9!@#$%^&*]{8,10}$`,
      required: true,
      value: password1,
      onChange: (e) => setPassword1(e.target.value),
    },
    {
      id: 7,
      name: "confirmPassword",
      type: "password",
      placeholder: "Confirm Password",
      errorMessage: "Passwords don't match!",
      label: "Confirm Password",
      required: true,
      value: password2,
      onChange: (e) => setPassword2(e.target.value),
    },

  ];


  return (
    <div className="app">
      <Grid>
        <Paper style={paperStyle} elevation={10}>
          <Grid style={{ alignItems: "center" }}>
            <center><h3>Register</h3></center>
          </Grid>

          <form >

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
              Register
            </Button>
            <p>
              {" "}
              Already a User? <Link to={"/"}>Login</Link>{" "}
            </p>
          </form>
        </Paper>
      </Grid>
    </div>
  );
};

export default Register;