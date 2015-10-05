#!/bin/bash
USER='admin'
PASSWORD='HhhmdDK0VUxN'
HOST='192.168.99.100'
PORT='3306'
DB='CHECK_IN'

mysql -u$USER -p$PASSWORD -h $HOST -P$PORT < `dirname $0`/CREATE_DB.sql
mysql -u$USER -p$PASSWORD -h $HOST -P$PORT $DB < `dirname $0`/MOCK_DATA_SET_1.sql
mysql -u$USER -p$PASSWORD -h $HOST -P$PORT $DB < `dirname $0`/MOCK_DATA_SET_2.sql
