
### 构建容器并运行
```shell
docker-compose up -d --build
```
### 调用
```shell
curl -X POST -F "file=@/data/123.png" http://127.0.0.1
```