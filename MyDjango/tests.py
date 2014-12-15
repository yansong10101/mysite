from django.test import TestCase
import MySQLdb
from mysite.settings import DATABASES as testdb

# Create your tests here.
def db_read():
    u_name = testdb['default']['USER']
    u_password = testdb['default']['PASSWORD']
    u_database = testdb['default']['NAME']
    connection = MySQLdb.connect(host='127.0.0.1', user='yansong', passwd='yansong', db='mydatabase')
    cursor = connection.cursor()
    cursor.execute('select user_name from test')
    data = cursor.fetchall()
    str = ''
    for row in data:
        str += row[0]
    cursor.close()
    connection.close()
    return str