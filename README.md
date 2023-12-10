* flink-starrocks-streaming-load
** 项目背景
** 依赖
> docker

** quick start
1. 进入项目目录 `cd flink-starrocks-streaming-load` 
2. docker-compose up --build -d
3. 在环境文件.env配置对应的服务参数
4. 
5. `python .\src\main\tableBuliler.py --source ${} --ddl`
6. docker-compose exec jobmanager 
