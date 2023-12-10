CREATE TABLE token_info (
     chain STRING,
     token_symbol STRING,
     token_address STRING,
     PRIMARY KEY(chain, token_address) NOT ENFORCED
     ) WITH (
     'connector' = 'mysql-cdc',
     'hostname' = '172.29.128.1', -- 内网 ip
     'port' = '3306',
     'username' = 'root',
     'password' = 'a123456',
     'database-name' = 'test_cdc',
     'table-name' = 'token_info'
);

CREATE TABLE token_info_sr_sink (
    `chain` STRING not null,
    `token_address` STRING not null,
    `token_symbol` STRING not null,
    `insert_time` as PROCTIME(),
    PRIMARY KEY (`chain`, `token_address`) NOT ENFORCED
) WITH (
    'connector' = 'starrocks',
    'jdbc-url' = 'jdbc:mysql://172.24.176.1:9030',
    'load-url' = '172.24.176.1:8030',
    'database-name' = 'test_sink',
    'table-name' = 'token_info_change_log',
    'username' = 'root',
    'password' = '',
    'sink.buffer-flush.interval-ms' = '15000',
    'sink.properties.format' = 'json',
    'sink.properties.strip_outer_array' = 'true',
    'sink.parallelism' = '1',
    'sink.max-retries' = '10'
);

insert into token_info_sr_sink (
    select

    from token_info
)