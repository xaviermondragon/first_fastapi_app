# Preparation
Switch to project folder
```
sudo apt install python3.10-venv
python3.10 -m venv env
source env/bin/activate
pip3.10 install -r requirements.txt
deactivate
```

# Run the server
`
uvicorn app.main:app
`
# Run the server wit auto-reload
`
uvicorn app.main:app --reload
`

# Create docker images and start the containers
`
docker-compose up -d --build
`


# Access the database via psql (psql is a terminal-based front-end to PostgreSQL)
```
docker-compose exec web-db psql -U postgres

psql (14.1)
Type "help" for help.

postgres=# \c web_dev
You are now connected to database "web_dev" as user "postgres".

web_dev=# \dt
            List of relations
 Schema |    Name     | Type  |  Owner
--------+-------------+-------+----------
 public | textsummary | table | postgres
(1 row

web_dev=# \q
```

# Some routes to try out:
- http://localhost:8004/ping
- http://localhost:8004/openapi.json
- http://localhost:8004/docs



# Init Aerich
`
docker-compose exec web aerich init -t app.db.TORTOISE_ORM
`

# Create the first migration
`
docker-compose exec web aerich init-db
`

# Apply the schema to the database in its final state rather than applying the migrations via Aerich
`
docker-compose exec web python app/db.py
`

# Apply schema migration using Aerich
`
docker-compose exec web aerich upgrade
`

# Pytest Commands
## normal run
`
docker-compose exec web python -m pytest
`

## Run the tests with coverage
`
docker-compose exec web python -m pytest --cov="." --cov-report html
`
#### The coverage report can be found in [/project/htmlcov/index.html](./project/htmlcov/index.html)

## Get a coverage report
`
docker-compose exec web python -m pytest --cov="."
`

## disable warnings
`docker-compose exec web python -m pytest -p no:warnings`

## run only the last failed tests
`docker-compose exec web python -m pytest --lf`

## run only the tests with names that match the string expression
`docker-compose exec web python -m pytest -k "summary and not test_read_summary"`

## stop the test session after the first failure
`docker-compose exec web python -m pytest -x`

## enter PDB after first failure then end the test session
`docker-compose exec web python -m pytest -x --pdb`

## stop the test run after two failures
`docker-compose exec web python -m pytest --maxfail=2`

## show local variables in tracebacks
`docker-compose exec web python -m pytest -l`

## list the 2 slowest tests
`docker-compose exec web python -m pytest --durations=2`

# Code Quality
## Code linting with flake
```
docker-compose exec web black . --check
docker-compose exec web black . --diff
docker-compose exec web black .
```

## Sort all our imports alphabetically and automatically separate them into sections
```
docker-compose exec web isort . --check-only
docker-compose exec web isort . --diff
docker-compose exec web isort .
```

# Code Formatting


# Deployment
## Create a new app
```
$ heroku create
Creating app... done, ⬢ floating-mesa-11641
https://floating-mesa-11641.herokuapp.com/ | https://git.heroku.com/floating-mesa-11641.git
```

## Log in to the Heroku Container Registry
```
$ heroku container:login
```

## Provision a new Postgres database with the hobby-dev plan:
```
$ heroku addons:create heroku-postgresql:hobby-dev --app floating-mesa-11641
```

## Build the production image and tag it
```
$ docker build -f project/Dockerfile.prod -t registry.heroku.com/floating-mesa-11641/web ./project
```

## To test locally, spin up the container
```
$ docker run --name fastapi-tdd -e PORT=8765 -e DATABASE_URL=sqlite://sqlite.db -p 5003:8765 registry.heroku.com/floating-mesa-11641/web:latest
```

## Bring down the container once done:
```
docker rm fastapi-tdd -f
```

## Push the image to the registry:
```
$ docker push registry.heroku.com/floating-mesa-11641/web:latest
```

## Release the image:
```
$ heroku container:release web --app floating-mesa-11641
```

## You should be able to view the app at http://floating-mesa-11641.herokuapp.com/ping

## Apply the migrations:
```
$ heroku run aerich upgrade --app floating-mesa-11641
```