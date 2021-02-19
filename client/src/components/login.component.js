import React, { useState } from 'react';
import {
    useHistory,
    Redirect
} from "react-router-dom"
import PropTypes from 'prop-types';

async function loginUser(credentials) {
    return fetch('http://localhost:4001/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(credentials)
    })
        .then(data => data.json())
}

export default function Login({ token, setToken }) {

    const [email, setEmail] = useState();
    const [pssw, setPassword] = useState();
    let history = useHistory();

    // Verifica inicialmente si ya está autenticado. 
    if (token)
        return (<>
            <Redirect
                to={{
                    pathname: "/concursos",
                    state: { token }
                }} /></>)


    const handleSubmit = async e => {
        e.preventDefault();
        const data = await loginUser({
            email,
            pssw
        });
        if (data.access_token) {
            setToken(data.access_token);
            console.log(token)
            history.push({
                pathname: "/concursos",
                state: { token: token }
            });
        } else {
            alert(data.message)
        }
    }

    return (
        <>
            <div className="outer">
                <div className="inner">
                    <form onSubmit={handleSubmit}>
                        <h3>Iniciar sesión</h3>

                        <div className="form-group">
                            <label>Correo</label>
                            <input type="email" className="form-control" placeholder="alguno@uniandes.edu.co" onChange={e => setEmail(e.target.value)} />
                        </div>

                        <div className="form-group">
                            <label>Contraseña</label>
                            <input type="password" className="form-control" placeholder="*********" onChange={e => setPassword(e.target.value)} />
                        </div>

                        <div className="form-group">
                            <div className="custom-control custom-checkbox">
                                <input type="checkbox" className="custom-control-input" id="customCheck1" />
                                <label className="custom-control-label" htmlFor="customCheck1">Recuerdame</label>
                            </div>
                        </div>

                        <button type="submit" className="btn btn-dark btn-lg btn-block">Iniciar sesión</button>
                        <p className="forgot-password text-right">
                            ¿Olvidaste tu <a href="#">contraseña?</a>
                        </p>
                    </form>
                </div>
            </div>
        </>
    );
}

Login.propTypes = {
    setToken: PropTypes.func.isRequired
}