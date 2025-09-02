# Simple MySQL Configuration:

```sql
mysql
CREATE DATABASE app_db;
CREATE USER 'appuser'@'localhost' IDENTIFIED BY 'Password';
GRANT ALL PRIVILEGES ON app_db.* TO 'appuser'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```



