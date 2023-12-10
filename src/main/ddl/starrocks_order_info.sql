CREATE TABLE beta.order_info_records (
    order_id varchar(100) NOT NULL,
    order_type varchar(20) NULL,
    name varchar(20) NULL
)
DUPLICATE KEY(order_id)
DISTRIBUTED BY HASH(order_id);