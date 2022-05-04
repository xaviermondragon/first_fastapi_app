'''
uvicorn app.main:app
uvicorn app.main:app --reload
'''

# Access the database via psql (psql is a terminal-based front-end to PostgreSQL)
'''
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
(1 row)

web_dev=# \q
'''

# Init Aerich
'''
docker-compose exec web aerich init -t app.db.TORTOISE_ORM
'''

# Create the first migration
'''
docker-compose exec web aerich init-db
'''

# Run the tests
'''
docker-compose exec web python -m pytest
'''

# Apply the schema to the database in its final state rather than applying the migrations via Aerich
'''
docker-compose exec web python app/db.py
'''

# Apply schema migration using Aerich
'''
docker-compose exec web aerich upgrade
'''