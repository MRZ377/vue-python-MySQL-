import pymysql,os
from dotenv import load_dotenv

load_dotenv()

dbconfig = {
    'host' : os.getenv('DB_HOST'),
    'port' : os.getenv('DB_PORT'),
    'user' : os.getenv('DB_USER'),
    'password' : os.getenv('DB_PASSWORD'),
    'database' : os.getenv('DB_NAME'),
    'charset' : os.getenv('DB_CHARSET'),
    'cursorclass' : pymysql.cursors.DictCursor
}