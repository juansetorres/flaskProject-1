import React, { useState } from 'react';
import '../node_modules/bootstrap/dist/css/bootstrap.min.css';
import './App.css';
import { BrowserRouter as Router, Switch, Route, Link, useHistory } from "react-router-dom";

import Login from "./components/login.component";
import SignUp from "./components/signup.component";
import ConcursosList from "./components/Concurso/concursos.component"

function App() {
  const [token, setToken] = useState();
  let history = useHistory();

  const logout = () => {
    setToken(null);
    history.push({
      pathname: "/sign-in"
    });
  }

  return (
    <Router>
      <div className="App">
        <nav className="navbar navbar-expand-lg navbar-light sticky-top">
          <div className="container">
            <Link className="navbar-brand" to={"/"}>Proyecto 1</Link>
            <div className="collapse navbar-collapse" id="navbarTogglerDemo02">
              {token ?
                <ul className="navbar-nav ml-auto">
                  <li className="nav-item">
                    <button onClick={logout}>Cerrar sesión</button>
                  </li>
                </ul> :
                <ul className="navbar-nav ml-auto">
                  <li className="nav-item">
                    <Link className="nav-link" to={"/sign-in"}>Iniciar sesión</Link>
                  </li>
                  <li className="nav-item">
                    <Link className="nav-link" to={"/sign-up"}>Registro</Link>
                  </li>
                </ul>
              }
            </div>
          </div>
        </nav>

        <Switch>
          <Route exact path='/' render={(props) => (
            <Login {...props} setToken={setToken} token={token} />
          )} />
          <Route path="/sign-in" render={(props) => (
            <Login {...props} setToken={setToken} token={token} />
          )} />
          <Route path="/sign-up" component={SignUp} />
          <Route path="/concursos" render={(props) => (
            <ConcursosList {...props} token={token} setToken={setToken} />
          )} />
        </Switch>

      </div>
    </Router>
  );
}

export default App;