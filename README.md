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