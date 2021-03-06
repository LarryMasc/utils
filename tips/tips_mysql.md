# MySQL Tips

## Setup MySQL on Ubuntu (Tested with 18.04 (Bionic))
* Review tips_build_new_system.md to build from Source
* Create /etc/my.cnf
```text
[client]
socket=/u/mysql/5.7.28/run/mysqld.sock

[mysqld]
socket=/u/mysql/5.7.28/run/mysqld.sock
```    
* As root run 
```text
mysqld \
    --initialize \
    --user=mysql \
    --datadir=/db/mysql/data
# MySQL default password is in ~root/.mysql_secret
        
cd /u/mysql/5.7.28/support-files
./mysql.server start
./mysql.server status
./mysql.server stop

cp mysql.server /usr/local/bin
cd /etc/systemd/system

cat > mysql.service
[Unit]
Description=MySQL Database Daemon
After=network.target

[Service]
ExecStart=/usr/local/bin/mysql.server start
ExecStop=/usr/local/bin/mysql.server stop
Type=forking

[Install]
WantedBy=default.target

chmod 644 mysql.service
systemctl daemon-reload
systemctl enable mysql.service

```
    
## MariaDB installation
 * cd /etc/yum.repos.d
 * vi mariadb.repo   
[mariadb]  
name = Mariadb  
baseurl = http://yum.mariadb.org/10.1/centos7-amd64  
gpgkey = https://yum.mariadb.org/RPM-GPG-KEY-MariaDB  
gpgcheck=1

### Install and start the services
 * yum install MariaDB-server MariaDB-client -y  
 * systemctl start mariadb 
 * systemctl enable mariadb  
 * systemctl status mariadb  

### Secure the installation
 * mysql_secure_installation
 * Determine defaults  
    * mysqld --print-defaults
 * Root login to setup users and databases
    * mysql -u root -p mysql
 
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
        * start the server in safe mode
            * mysqld_safe --skip-grant-tables
            * mysql -u root mysql
            * update user set password=PASSWORD("<password>") where user='root';
            * flush privileges;
            * stop the mysqld_safe process
        * systemctl start mariadb
        * /usr/bin/mysql_secure_installation
        * mysql -u root -p mysql (enter root password)
        * alter user 'root'@'localhost' identified by '<password>';
        * create user lifecycle IDENTIFIED BY '<password>';
    
    * Directories are in /var/lib/mysql*. Move them aside to and reinstall mysql.

 * show tables;
 * describe <tablename>;
 * select user from mysql.user;
 * Wildcard is %.

 * create user 'lifecycle'@'localhost' IDENTIFIED BY 'PASSWORD';
 * create database lifecycle default character set UTF8;
 * grant all privileges on lifecycle.* to 'lifecycle'@'localhost' \
   IDENTIFIED BY 'PASSWORD';
 * grant all privileges on lifecycle.* to 'lifecycle'@'%' \
   IDENTIFIED BY 'PASSWORD';

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

## mysql_config_editor
 * Not available on Mariadb. Use it to encrypt passwords

## .my.cnf entries to support multiple DBs
[pager options](http://kedar.nitty-witty.com/blog/5-useful-mysql-command-options-pager-prompt-rehash-tee-system)  
example .my.cnf
 * The client section is common to all DBs
 [client]  
 port=3306
 prompt='(\d)'
 
 * For specific MySQL DB entries
 
 **[mysqldb1]**  
  user=(user1)  
  password=(password)  
  database=(db1)  
  host=(host1)
 
 **[mysqldb2]**  
 user=(user2)  
 password=(password2)  
 database=(db2)  
 host=(host1)  
 
 * To connect to db1  
```
# Add alias in .profile
alias mysql="/usr/bin/mysql --defaults-file=$HOME/.my.cnf"
alias db1="mysql --defaults-group-suffix=db1"
 ```
 

## DML
 * select count(*) from tablename;

## Administration
 * select @@hostname;
 * show processlist;
 * show grants for lifecycle;
 * show grants for root@'localhost';
 * show engine innodb status;
 * SELECT @@GLOBAL.secure_file_priv;
 
## Tuning
 * key_buffer_size
 * https://dev.mysql.com/doc/refman/5.7/en/innodb-configuration.html

## Backup and Recovery
### Preparing for Backups
#### Enable [Binary Logs](https://dev.mysql.com/doc/refman/8.0/en/binary-log.html) for Point-in-time / Incremental backups
 * Determine of Binary Logging is on
 ```
 # Login as root in MYSQL Server
 show binary logs; # Will show the current binary log
 show master status;
 ```
 * [apparmor setting](https://stackoverflow.com/questions/2783313/how-can-i-get-around-mysql-errcode-13-with-select-into-outfile)
 ```
 # Update /etc/apparmor.d/usr.sbin.mysqld
 # Add to data dir section

 /u/admin/bkup/ r,
 /u/admin/bkup/** rwk,
 ```
 
 * vi /etc/mysql/mysqld.conf.d/mysqld.cnf
 ```
 innodb_file_per_table = ON
 symbolic-links = 0
 bind-address = 0.0.0.0
 key_buffer_size = 16M
 innodb_buffer_pool_size = 1G (50% RAM)
 innodb_buffer_pool_instances = 4 (# of CPUs)
 max_allowed_packet = 500M
 query_cache_limit = 126M
 query_cache_size =1024M
 thread_stack = 
 thread_cache_size = 
 secure-file-priv = ""
 server-id               = 1
 log_bin                 = /var/log/mysql/mysql-bin.log
 max_binlog_size         = 100M
 
 ```

 * By default the MySQL datafiles are in /var/lib/mysql  
 * Use the 'mysqldump' utility to do the backups  
   **D=`date +'%m%%d%Y_%H%M%S** # Sets D=ddmmyyyy_hrminsec
   **mysqldump --databases -u lifecyle -p lifecycle > mysql_backup_${D}.sql** # This will dump the entire DB.
   
 * This generates the SQL file for recovery using the 'mysql' client  
   **mysql < mysql_bacup_20170709_190432.sql**
  
## Load data from a CSV file into MySQL
* load historical data into a MySQL table  
* Ensure you convert STR to DATE  
* The 'ignore 1 lines' ensures that the header line is skipped  

load data local infile '/home/lmascare/misc/mysql/goog.csv'  
into table goog  
fields terminated by ',' ignore 1 lines  
(@date, open, high, low, close, volume)  
set date = str_to_date(@date,'%d-%b-%y');  
