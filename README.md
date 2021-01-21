# Review Service

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

* Docker version 19+

### Installing

Build first the image:

```bash
docker-compose build # --no-cache to force dependencies installation
```

To run the webserver (go to 127.0.0.1:8080):

```bash
docker-compose up # -d for detached
```

## Running the tests

To run the tests with flake8:

```bash
docker-compose run --entrypoint '/usr/bin/env' --rm review_service bash scripts/run-tests.sh
```

See `pytest --help` for more options.

## Generate migration scripts

To generate migration scripts:

```bash
docker-compose run --entrypoint '/usr/bin/env' review_service bash scripts/generate-migrations.sh "Add review table"
```

## Deployment

The instructions in the next subsection [Configuration](#configuration) will explain how to configure a Review Service instance to have it on a live system.

### Configuration

Specify each parameter using `-e`, `--env`, and `--env-file` flags to set simple (non-array) environment variables to `docker run`. For example,

```bash
$ docker run -e MYVAR1 --env MYVAR2=foo \
    --env-file ./env.list \
    skolens/provider_service:<version>
```

The following tables list the configurable parameters and their default values.

|             Parameter               |            Description             |                    Default                |
|-------------------------------------|------------------------------------|-------------------------------------------|
| `DATABASE_NAME`                     | The name of the database to use          | ``                                  |
| `DATABASE_USER`                     | The username to use when connecting to the database | ``                       |
| `DATABASE_PASSWORD`                 | The password to use when connecting to the database | ``                       |
| `DATABASE_HOST`                     | The host to use when connecting to the database | ``                           |
| `DATABASE_PORT`                     | The port to use when connecting to the database | ``                           |
| `JWT_PUBLIC_KEY_RSA`                | The public RSA KEY                       | ``                                  |

## Versioning

[SemVer](http://semver.org/)
