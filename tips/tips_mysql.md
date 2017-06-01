# MySQL Tips

## Connection
 * mysql -h <host> -u <user> -p -D <dbname> - P <port(4303)>
 * /etc/my.cnf or /etc/mysql/my.cnf or $HOME/.my.cnf
 
## DDL

### Centos 7 has replaced MySQL with MariaDB
 * As root
 * shutdown the mariadb server
    systemctl stop mariadb

 * Initialize the system dictionary
   mysql_install_db --user=mysql
 
 * To recover the root password
    **start the server in safe mode
      mysqld_safe --skip-grant-tables

    **mysql -u root mysql
      update user set password=PASSWORD("<password>") where user='root';
      flush privileges;
      stop the mysqld_safe process
      
 * systemctl start mariadb
 * /usr/bin/mysql_secure_installation
 * mysql -u root -p mysql (enter root password)
 * create user lifecycle identified by '<password>';


 * show tables;
 * describe <tablename>;
 * select user from mysql.user;
 * Wildcard is %.

 * create user 'lifecycle'@'localhost' identifed by 'PASSWORD';
 * grant all privileges on lifecycle.* to 'lifecycle'@'localhost' \
   identified by 'PASSWORD';
 * grant all privileges on lifecycle.* to 'lifecycle'@'%' \
   identified by 'PASSWORD';
 * create database lifecycle default character set UTF8;

 * use lifecycle;
 * CREATE TABLE hostinfo (
      hostname    varchar(128) not null,
      hostgroup   varchar(128) not null
   );

   *Note group is a reserved word*

 * to load the data into the table and ignore the header

   load data local infile '/tmp/host.csv' into table hostinfo
    fields terminated by ',' ignore 1 lines;

    *Note local and full path are extremely important*


## DML
 * select count(*) from tablename;
