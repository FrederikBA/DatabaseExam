import Login from "../components/Login"
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faSearch } from "@fortawesome/free-solid-svg-icons";
import { Button, Col, Container, Form, Row } from "react-bootstrap";
const One = () => {
    return (
        <div >

<Container className="mt-5">
      <Row>
        <Col sm={4}>
          <Form className="d-flex">
            <Form.Control
              type="search"
              placeholder="Search"
              className="me-2 rounded-pill"
              aria-label="Search"
            />
            <Button className="rounded-pill" variant="outline-primary">
              Search
            </Button>
          </Form>
        </Col>
      </Row>
    </Container>



</div>
    )
}

export default One