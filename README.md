# HBnB Evolution - Part 2: Database Integration and Security Enhancements

## Description

The second phase of the HBnB Evolution project focuses on integrating a relational database using SQLAlchemy and enhancing the application's security with JWT authentication. This phase aims to make the application more scalable and secure, while improving user experience with robust data management.

## Features

- Integration of SQLAlchemy to handle database operations.
- Implementation of secure authentication with JWT.
- Dynamic database configuration, allowing switching from SQLite in development to PostgreSQL in production.
- Database migration management with Alembic.
- Role-based access control to restrict actions to authenticated users or administrators.
- Use of Docker Compose to orchestrate the application's services.

## Technologies Used

- **Python 3.10.12**: Main programming language.
- **Flask**: Framework to handle the RESTful API.
- **SQLAlchemy**: ORM to interact with the relational database.
- **PostgreSQL**: Relational database used in production.
- **SQLite**: Database used for development.
- **Flask-JWT-Extended**: Extension to handle JWT authentication.
- **Alembic**: Database migration management tool.
- **Docker & Docker Compose**: Containerization and orchestration of services.
- **Gunicorn**: WSGI server to deploy the application.
- **SwaggerUI**: API documentation.
- **GitHub Actions**: Continuous integration and deployment.

## Installation

### Prerequisites

- Docker and Docker Compose installed on your machine.

### Installation Steps

1. **Clone the repository**

    ```sh
    git clone https://github.com/jeje-digifab/holbertonschool-hbnb-database.git
    cd holbertonschool-hbnb-database
    ```

2. **Set up environment variables**

    Create a `.env` file at the root of the project with the necessary variables, for example:
    
    ```env
    FLASK_APP=run.py
    FLASK_ENV=development
    DATABASE_URL=postgresql://user:password@db/hbnb_dev
    JWT_SECRET_KEY=your_secret_key
    ```

3. **Build and run the services with Docker Compose**

    ```sh
    docker-compose up --build
    ```

    This will build the necessary Docker images and start the containers for the Flask application, PostgreSQL, and other required services.

## Usage

Once the containers are running, you can access the API at `http://localhost:5000`.

API documentation is available at:

`http://localhost:5000/api/docs`

If needed, replace `http://localhost` with the machine's IP address `http://ip`.

## Running Unit Tests

To run the unit tests, enter the Flask container in interactive mode:

```sh
docker exec -it <container-id> sh
```

Then, run the tests:
```sh
python3 -m unittest discover tests
```

## Usage

Once the container is running, you can access the API at `http://localhost`.

API documentation is available here:

`http://localhost/api/docs`

If needed, replace `http://localhost` with the machine's IP address `http://ip`

## Contributors

- **Néia Santos Nascimento** (https://github.com/Neia2)
- **Nadège Luthier** (https://github.com/)
- **Benjamin Jacob** (https://github.com/)
- **Jérôme Romand** (https://github.com/jeje-digifab)
