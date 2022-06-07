## Dariger.kz - Recommendation system for choosing a personal doctor

  ### You need to install: 
  + pip install fastapi
  + pip install uvicorn
  + pip install sqlalchemy
  + pip install databases
  + pip install "databases[postgresql]"
  + pip install psycopg2-binary
  + pip install "pydantic[email]"
  + pip install passlib
  + pip install bcrypt
  + pip install jose
  + pip install python-jose

  ### After installing frameworks open project derictory in terminal/shell and write:
  + $env:AA_DATABASE_URL="postgresql://root:root@localhost:32700/dariger"
  + docker-compose up
  + $env:AA_DATABASE_URL="postgresql://root:root@localhost:32700/dariger"
  + python main.py 

  ### If you want to open fastapi docs:
  http://127.0.0.2:8000/docs
  http://127.0.0.2:8000/redoc
