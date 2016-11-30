--SQL语句学习笔记--  /* */
mysql -u root -p

show databases;

use database;

CREATE TABLE teacher(id int auto_increment primary key not null,name varchar(30));
CREATE TABLE person  
                         -> (  
                         -> id INT(8) NOT NULL AUTO_INCREMENT PRIMARY KEY,  
                         -> name varchar(16) default 'nobody',  
                         -> birthday char(19),  
                         -> )ENGINE=InnoDB DEFAULT CHARSET=utf8 /* 创建数据表,字符集设定为utf8,可插入中文 */  
                         -> ;  
DROP TABLE  tbl_name;/* 删除表 */

show tables;

select * from table_name;

SELECT DISTINCT column_name,column_name FROM table_name;

SELECT column_name,column_name FROM table_name WHERE column_name operator value;
SELECT * FROM Websites WHERE country='CN';/*注意where子句中的运算符*/
SELECT * FROM Websites WHERE alexa > 15 AND (country='CN' OR country='USA');

SELECT column_name,column_name FROM table_name ORDER BY column_name,column_name ASC|DESC;

INSERT INTO table_name (column1,column2,column3,...) VALUES (value1,value2,value3,...);
INSERT INTO Websites (name, url, alexa, country) VALUES ('百度','https://www.baidu.com/','4','CN');

UPDATE table_name SET column1=value1,column2=value2,... WHERE some_column=some_value;
UPDATE Websites SET alexa='5000', country='USA' WHERE name='菜鸟教程';

DELETE FROM table_name WHERE some_column=some_value;
DELETE FROM Websites WHERE name='百度' AND country='CN';
DELETE FROM table_name;
or
DELETE * FROM table_name;