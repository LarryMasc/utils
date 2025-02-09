# Snowflake Tips

###Snowflake data and Metadata
#### Stored in Snowflake Storage 
#### Snowflake Datawarehouse. Access and Processes data

## pradeepetl.github.io ##

```
Setup a snowflake trial account
- https://signup.snowflake.com/
- https://docs.snowflake.com/

 - Business Critical
 - AWS
     - us-east-1

 - Create a DB
    create database demo_db;
- Create table
    create table emp (
     firstname  string,
     lastname   string,
     email     string,
     streetadress  string,
     city          string,
     start_date    date
);
```
### Shared Disk Architecture
 - Compute Nodes share the same disk
 - Scalability
 - Data Consistency
 - Bottleneck in Shared Disk communications
 - 

### Shared nothing Architecture
 - Each compute node has its own disk
 - Data storage and compute are tightly coupled. You cannot increase storage w/o increasing compute and vide versa
 - Issue with Storage / Compute failure of 1 node requries data to be "shuffled" to another node.
 - Performance is heavily dependant on how data is distributed across the node in the system
 - Software upgrades

Snowflake separate Compute and Storage into separate components and bound together by Cloud Services layer. With this the
compute and data storage layers can be independently scaled.
Cloud Services layer has the following services
 - Authentication and Access control
 - Infrastructure Manager
 - Query Optimizer
 - Transaction Manager
 - Security
 - Metadata Manager

 - 
