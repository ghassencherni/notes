import os

db_host = os.environ.get('DB_HOST', default='localhost')
db_name = os.environ.get('DB_NAME', default='notes')
db_user = os.environ.get('DB_USERNAME', default='db_user')
db_password = os.environ.get('DB_PASSWORD', default='db_password')
db_port = os.environ.get('DB_PORT', default='5432')

SQLALCHEMY_TRACK_MODIFICATIONS = False
#SQLALCHEMY_DATABASE_URI = f"postgres://{db_user}:{db_password}@{db_host}:5432/{db_name}"
SQLALCHEMY_DATABASE_URI = f"postgres://{db_user}:{db_password}@{db_host}/{db_name}"
