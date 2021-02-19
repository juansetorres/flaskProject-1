import React, { useState, useEffect } from "react";
import { Redirect } from 'react-router-dom';
import Container from 'react-bootstrap/Container';
import Card from 'react-bootstrap/Card'
import Button from 'react-bootstrap/Button'
import ConcursoModal from './concursoModal.component'
import "./concursos.component.css"

const ConcursosList = ({token}) => {
  const [modalShow, setModalShow] = React.useState(false);
  const [concursoActual, setConcursoActual] = React.useState({});

  if (!token) {
      return (<>
        <Redirect
          to={{
            pathname: "/sign-in",
          }} /></>)
  }

  const EstablecerConcursoPorVer = (concurso) => {
    return () => {
      setConcursoActual(concurso);
      setModalShow(true);
    }
  }

  const cerrarModal = () => {
    setConcursoActual({});
    setModalShow(false);
  }

  const concursos = [
    {
      "id": 1,
      "nombre": "Concurso Uniandino",
      "descripcion": "Una pequeña prueba",
      "imageUrl": "https://www.juegocasinos.com.mx/wp-content/uploads/Sorteos-gratis.jpg",
      "url": "www.concursoperron.com",
      "fechaIni": "2021-05-29T19:30:03.283Z",
      "fechaFin": "2021-06-29T19:30:03.283Z",
      "value": 100000,
      "guion:": "Lorem ipsum",
      "recomendaciones": "que esté bien chingon"
    },
    {
      "id": 2,
      "nombre": "Concurso Uniandino",
      "descripcion": "Una pequeña prueba",
      "imageUrl": "https://www.juegocasinos.com.mx/wp-content/uploads/Sorteos-gratis.jpg",
      "url": "www.concursoperron.com",
      "fechaIni": "2021-05-29T19:30:03.283Z",
      "fechaFin": "2021-06-29T19:30:03.283Z",
      "value": 100000,
      "guion:": "Lorem ipsum",
      "recomendaciones": "que esté bien chingon"
    },

    {
      "id": 3,
      "nombre": "Concurso Uniandino",
      "descripcion": "Una pequeña prueba",
      "imageUrl": "https://www.juegocasinos.com.mx/wp-content/uploads/Sorteos-gratis.jpg",
      "url": "www.concursoperron.com",
      "fechaIni": "2021-05-29T19:30:03.283Z",
      "fechaFin": "2021-06-29T19:30:03.283Z",
      "value": 100000,
      "guion:": "Lorem ipsum",
      "recomendaciones": "que esté bien chingon"
    },

    {
      "id": 4,
      "nombre": "Concurso Uniandino",
      "descripcion": "Una pequeña prueba",
      "imageUrl": "https://www.juegocasinos.com.mx/wp-content/uploads/Sorteos-gratis.jpg",
      "url": "www.concursoperron.com",
      "fechaIni": "2021-05-29T19:30:03.283Z",
      "fechaFin": "2021-06-29T19:30:03.283Z",
      "value": 100000,
      "guion:": "Lorem ipsum",
      "recomendaciones": "que esté bien chingon"
    },

    {
      "id": 5,
      "nombre": "Concurso Uniandino",
      "descripcion": "Una pequeña prueba",
      "imageUrl": "https://www.juegocasinos.com.mx/wp-content/uploads/Sorteos-gratis.jpg",
      "url": "www.concursoperron.com",
      "fechaIni": "2021-05-29T19:30:03.283Z",
      "fechaFin": "2021-06-29T19:30:03.283Z",
      "value": 100000,
      "guion:": "Lorem ipsum",
      "recomendaciones": "que esté bien chingon"
    }

  ]

  return (
    <div>
      <Container className="panelBotones">
        <Button onClick={EstablecerConcursoPorVer({})}> Agregar Concurso </Button>
      </Container>

      <Container className="contenedor">
        {concursos.map((value, index) => {
          return (
            <Card className="TarjetaConcurso" style={{ width: '18rem' }}>
              <Card.Img variant="top" src={value.imageUrl} />
              <Card.Body>
                <Card.Title>{value.nombre}</Card.Title>
                <Card.Text> {value.descripcion} </Card.Text>
                <Button variant="primary" onClick={EstablecerConcursoPorVer(value)}>Ver detalles</Button>
              </Card.Body>
            </Card>
          )
        })}
      </Container>

      <ConcursoModal show={modalShow} onHide={cerrarModal} concursoData={concursoActual}></ConcursoModal>
    </div>
  );
};

export default ConcursosList;
