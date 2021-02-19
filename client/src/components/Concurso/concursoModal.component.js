import React, { useState, useEffect } from "react";
import Modal from "react-bootstrap/Modal"
import Form from "react-bootstrap/Form"
import Button from "react-bootstrap/Modal"
import Datetime from 'react-datetime';

const ConcursoModal = ({ concursoData, show, onHide }) => {

    return (
        <Modal
            show={show}
            onHide={onHide}
            size="lg"
            aria-labelledby="contained-modal-title-vcenter"
            centered
        >
            <Modal.Header closeButton>
                <Modal.Title id="contained-modal-title-vcenter">
                    {Object.entries(concursoData).length !== 0 ? "Detalles del concurso" : "Nuevo Concurso"}
                </Modal.Title>
            </Modal.Header>
            <Modal.Body>
                <Form>
                    <Form.Group controlId="formNombre">
                        <Form.Label>Nombre</Form.Label>
                        <Form.Control type="text" value={concursoData.nombre} />
                    </Form.Group>

                    <Form.Group controlId="formRecomendaciones">
                        <Form.Label>Nombre de la página</Form.Label>
                        <Form.Control type="url" value={concursoData.url} />
                    </Form.Group>

                    <Form.Group controlId="formGuion">
                        <Form.Label>Guión</Form.Label>
                        <Form.Control as="textarea" rows={3} value={concursoData.guion} />
                    </Form.Group>

                    <Form.Group controlId="formRecomendaciones">
                        <Form.Label>Recomendaciones</Form.Label>
                        <Form.Control as="textarea" rows={3} value={concursoData.recomendaciones} />
                    </Form.Group>

                    <Form.Group controlId="formRecomendaciones">
                        <Form.Label>Valor</Form.Label>
                        <Form.Control type="number" value={concursoData.value} />
                    </Form.Group>

                    <Form.Group controlId="formFechaInicio">
                        <Form.Label>Fecha de Inicio</Form.Label>
                        <Datetime value={new Date(concursoData.fechaIni)} timeFormat={false} />
                    </Form.Group>

                    <Form.Group controlId="formFechaFin">
                        <Form.Label>Fecha de Finalización</Form.Label>
                        <Datetime value={new Date(concursoData.fechaFin)} timeFormat={false} />
                    </Form.Group>

                    <Form.Group>
                        <Form.File id="formBanner" label="Imagen del banner" />
                    </Form.Group>

                    <Button variant="primary" type="submit">
                        Submit
                    </Button>
                </Form>
            </Modal.Body>
            <Modal.Footer>
                <Button onClick={onHide}>Close</Button>
            </Modal.Footer>
        </Modal>
    );
}

export default ConcursoModal;