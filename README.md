# geo_fastapi_skeleton

# project structure


## local development
install and activate venv
```shell
python3.12 -m venv venv
```
```shell
source venv/bin/activate
```

install requirements
```shell
make dev
```

run postgres
```shell
docker compose up -d
```

apply changesets
```shell
make migrate
```

run 
```shell
fastapi dev service_api/app.py
```

docs `http://127.0.0.1:8000/docs`
api `http://127.0.0.1:8000`

### run test and flake
```shell
make check
```

### updating libs
update some lib in *.in file and then run

```shell
make compile-versions
```

create changeset
```shell
alembic revision --autogenerate -m comment
```
