import os


SourceMap = {
    'mysql':  {
        "HOST": os.getenv('MYSQL_HOST'),
        "PORT": os.getenv('MYSQL_PORT'),
        "USER_NAME": os.getenv('MYSQL_USER'),
        "PASSWORD": os.getenv('MYSQL_PASSWORD'),
    },
    'starrocks': {
        "HOST": os.getenv('STARROCKS_HOST'),
        "PORT": os.getenv('STARROCKS_PORT'),
        "USER_NAME": os.getenv('STARROCKS_USER'),
        "PASSWORD": os.getenv('STARROCKS_USER_PASSWORD'),
    }
}
