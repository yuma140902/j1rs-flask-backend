# j1rs-flask-backend

## セットアップ

```sh
pip install -r requirements.txt
```

## 再生成

```sh
docker run --rm -v ${PWD}:/local openapitools/openapi-generator-cli generate -i /local/openapi.yaml -g python-flask -o /local
```

## 起動(Docker)

```sh
docker build -t openapi_server .
docker run -p 8080:8080 openapi_server
```

## 起動

```sh
python3 -m openapi_server
```
