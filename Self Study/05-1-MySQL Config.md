# Simple MySQL Configuration:


```sh
# Connect to mysql:
mysql --host=localhost --user=username --password dbname
mysql -h localhost -u username -p dbname
# Using URI with Key:
mysqlx://user_name@localhost:33065
mysql://user@localhost:3306?get-server-public-key=true
```
```sql
mysql
CREATE DATABASE app_db;
CREATE USER 'appuser'@'localhost' IDENTIFIED BY 'Password';
GRANT ALL PRIVILEGES ON app_db.* TO 'appuser'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```



