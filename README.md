# Atrato Challenge

## The environment
In this case I used a Pipfile from pipenv to manage the dependencies as 
requested in the challenge. In case pipenv is not installed in the system:

```bash
sudo apt install pipenv # for debian systems to avoid using pip directly
```

If it doesn't matter to use pip directly then:

```bash
pip install pipenv
```

As pipenv creates a virtual environment for the project, to install the dependencies
you need to run:

```bash
pipenv install
```
To enter the virtual environment created by pipenv:

```bash
pipenv shell
```

## The files
The `sql_queries.ipynb` notebook contains the first challenge corresponding 
to the SQL queries. In the notebook you can find the code to create, insert and
query the database as requested. 

Inside `app/` folder there is the `data_processing.py` file which contains the code
related to pandas. As mentioned before, pipenv installs all the dependencies, in 
which pandas is included.

For the basic MLOps questions, I created the markdown document with questions
and answers called `ml_questions.md`.

Finally, the API. All the contents are inside the `app/` folder. The main file
is `main.py` which contains the FastAPI code to create the endpoints. The code is
divided in different files to keep it organized, while the processing file is not
related to the app itself, it is included becuase the documentation requested.

# How to run the API
For this specific case, I created a Dockerfile and a docker-compose.yml file
to make it easier to run the API. Inside the Docker file there is the code to create
the container and install the dependencies using pipenv, so we don't have to
worry about executing pipenv commands.

For the docker-compose file, it creates a network, builds the image and runs the
container exposing the port 8000.

```bash
docker compose up
```

The previous should make it work. Depending on the docker compose version,
probably you will need to use `docker-compose` instead of `docker compose`.
