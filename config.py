import os


# You need to replace the next values with the appropriate values for your configuration
basedir = os.path.abspath(os.path.dirname(__file__))
DEBUG = True
PORT = 9994
HOST = "0.0.0.0"
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
#SQLALCHEMY_DATABASE_URI = "postgresql://{DB_USER}:{DB_PASS}@{DB_ADDR}/{DB_NAME}".format(DB_USER="test2", DB_PASS="froz21", DB_ADDR="127.0.0.1", DB_NAME="ayni")
#SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
#PAGINATION_PAGE_SIZE = 5
PAGINATION_PAGE_ARGUMENT_NAME = 'page'
SECRET_KEY = 'loconfieso'
"""
"""

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:holi123@localhost:3306/ayni'
SQLALCHEMY_POOL_SIZE = 5
SQLALCHEMY_POOL_TIMEOUT = 30
SQLALCHEMY_POOL_RECYCLE = 31
SQLALCHEMY_TRACK_MODIFICATIONS  = False