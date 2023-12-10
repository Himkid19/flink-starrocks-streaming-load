import os
import argparse
import pydash as _
from dotenv import load_dotenv
from sourceBuilder import SourceBuilder


def get_env_value():
    return {
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


def get_ddl_str(file_name: str):
    current_dir = os.path.abspath(os.path.dirname(__file__))
    return current_dir + "\\ddl\\" + file_name + '.sql'


def build_table(source_key: str, ddl_file_name: str):
    source_map = get_env_value()
    source_config = source_map[source_key]
    connector = SourceBuilder(
        host=source_config['HOST'],
        port=source_config['PORT'],
        user=source_config['USER_NAME'],
        password=source_config['PASSWORD'],
    )
    # connector.query('create database beta')
    ddl = open(get_ddl_str(ddl_file_name)).read()
    result = connector.query(ddl)
    print(f"exec sql result: {result}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    load_dotenv(verbose=True)
    parser.add_argument('--source', type=str, default=None)
    parser.add_argument('--ddl', type=str, default=None)
    args = parser.parse_args()
    build_table(args.source, args.ddl)
    


