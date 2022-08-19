# RASA USAGE

- Setup environment
  - Copy .env-example to .env and change options:
        RASA_URL - the url of rasa-chatbot


- Run project
  - Install dependencies via pipenv
    - `pip install pipenv`
    - `pipenv shell`
    - `pipenv install && pipenv update`


  - Run project with selecting data file index
    - `uvicorn main:app`
  

  - Run project with docker-compose
    - `cd api`
    - `docker-compose build` (can emit if you do not have changes)
    - `docker-compose up`
