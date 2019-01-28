# Longitude

A **new** bunch of middleware functions to build applications on top of CARTO.

## Roadmap

A live document for the roadmap is [shared here](https://docs.google.com/document/d/1nO_JLaKFmr5h6MudDklFutv96CfkNjJxfd0xyh1szwM/edit#heading=h.44g51xumzfku)

- [ ] Database model
  - [x] CARTO data source
    - [x] Basic parametrized queries (i.e. templated queries)
    - [ ] Protected parametrized queries (i.e. avoiding injection)
    - [ ] Bind/dynamic parameters in queries (server-side render)
  - [ ] Postgres data source
    - [ ] driver 1
    - [ ] driver 2
  - [ ] Cache
    - [ ] Base cache
      - [x] Put
      - [x] Get
      - [x] Key generation
      - [ ] Flush
      - [ ] Expiration
    - [x] Ram Cache
    - [x] Redis Cache
  - [ ] Documentation
  - [ ] Unit tests
  - [ ] Sample scripts
 
- [ ] Config
 
- [ ] CI PyPi versioning

- [ ] Data manipulation
  - [ ] Carto
    - [ ] DataFrame read/write
    - [ ] COPY
  -[ ] Postgres
    - [ ] DataFrame read/write
    - [ ] COPY
 
- [ ] Validations
  - [ ] Marshmallow
    - [ ] Wrapper (?)
    - [ ] Documentation
 
- [ ] Swagger
  - [ ] Decorators
  - [ ] Flassger (?)
  - [ ] OAuth integration
  - [ ] Postman integration
  - [ ] Documentation
  
- [ ] SQL Alchemy
  - [ ] Model definition
  - [ ] Jenkins integration
  - [ ] Documentation

- [ ] OAuth
  - [ ] Role mapping
  - [ ] Token storage
  - [ ] Documentation
  
  ## As final user...

How to use:
```bash
pip install geographica-longitude
```

Or install from GitHub:
```bash
pip install -e git+https://github.com/GeographicaGS/Longitude#egg=longitude
```

## As developer...

Install pipenv in your development machine if you still do not have it.

Set up Python environment:

```shell
$ cd [path-to-longitude-folder]
$ pipenv install
```

To activate the virtual environment: `$ pipenv shell`. If the environment variables are defined in a `.env` file, they are loaded in this shell.

## Sample scripts

These are intended to be used with real databases (i.e. those in your profile) to check features of the library.

You will probably need to provide credentials/api keys/urls/username/... Check each script and it will be explained there.

## Testing and coverage 

The [```pytest-cov```](https://pytest-cov.readthedocs.io/en/latest/) plugin is being used. Coverage configuration is at ```.coveragerc``` (including output folder).

You can run something like: ```pytest --cov-report=html --cov=core core``` and the results will go in the defined html folder.

There is a bash script called ```generate_core_coverage.sh``` that runs the coverage analysis and shows the report in your browser.

## Upload a new version to PyPi

You need to be part of *Geographica's development team* to be able to accomplish this task.

Start docker
```
docker-compose run --rm python bash
```

Install needed dependencies
```
pip install -r requirements.txt
```

Set version at ```setup.py```

Upload:
```
python setup.py sdist
twine upload dist/geographica-longitude-<yourversion>.tar.gz
```
