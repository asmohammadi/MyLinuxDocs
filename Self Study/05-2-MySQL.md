# MySQL


```sh
apt-get install mysql.server # Installing MySQL Server
service mysql start # Starting MySQL service
mysql  # Go into MySQL 
mysql -u UserName # Go into MySQL with other Users
```

```sql
SHOW DATABASES; => Show all MySQL databases on the server (End command with ;)
USE mysql;  => Selecting a database
SHOW TABLES; => Show all tables of a database

CREATE DATABASE itpro_db; => Create a database

CREATE TABLE forum (id INT(20), forum CHAR(20), video CHAR(20));
    id, forum, video = Columns Name
    INT, CHAR = Column's Type
    20 = Size of the Column

SELECT * FROM forum; => Show entries of database "forum"
INSERT INTO forum (id,forum,video) VALUES ('1','network','500'); => Insert data into database table

SELECT id FROM forum; => Select a column's data from a table
SELECT id,video FROM forum; => Select 2 column's data from a table 

SELECT * From forum WHERE forum = 'linux'; => Select from a table named "forum" Where the column's data is equal to "Linux"

SELECT * From forum WHERE forum != 'linux'; => Select from a table named "forum" Where the column's data is not equal to "Linux"

SELECT * From forum WHERE forum LIKE 'l%'; => Select from a table named "forum" Where the column's data is like "L%"

SELECT * From forum WHERE forum LIKE '%i%'; => Select from a table named "forum" Where the column's data is like "%i%"

SELECT * From forum WHERE forum LIKE '%i%' AND id > 3; => Select from a table named "forum" Where the column's data is like "%i%" AND id in bigger than 3.

SELECT * From forum LIMIT 3; => Select from a table named "forum" and limit the result to 3.

SELECT * From forum ORDER BY id DESC; => Select from a table named "forum" and order by column "id" Descending.

SELECT * From users GROUP BY record; => Select from a table named "users" and group by column "record".

SELECT *count(*).record From users GROUP BY record; => Select from a table named "users" and count duplicate items.

UPDATE users SET user='unity' WHERE user='uity'; => Replace the value with new value

DELETE FROM users WHERE user='adeli'; => Delete a row with the value of an item.

SELECT * FROM forum JOIN users; => Join two tables

SELECT * FROM forum JOIN users ON forum.video = users.record; => Join two tables on specific columns
```





