#MORE SQL

#1. well, let me just start these over

#SELECT DISTINCT e.`first name`, e.`last name`, o.`ship city`
#FROM `orders` o, `employees` e, `customers` c
#WHERE e.`id` = o.`employee id` and `Ship State/Province` = 'CA';
"""
+------------+-----------+-------------+
| first name | last name | ship city   |
+------------+-----------+-------------+
| Andrew     | Cencini   | Los Angelas |
| Mariya     | Sergienko | Los Angelas |
+------------+-----------+-------------+
"""
#2. 
#SELECT DISTINCT c.`first name`, c.`last name`, o.`ship city`
#FROM `orders` o, `employees` e, `customers` c
#WHERE c.`id` = o.`customer id` and `Ship State/Province` = 'CA';
"""
+------------+-----------+-------------+
| first name | last name | ship city   |
+------------+-----------+-------------+
| Thomas     | Axen      | Los Angelas |
+------------+-----------+-------------+
"""
#i still just get this guy

#3.
#SELECT DISTINCT e.`first name`, e.`last name`, c.`first name`, c.`last name`, o.`ship city`
#FROM `orders` o, `employees` e, `customers` c
#WHERE `Ship State/Province` = 'CA';

#oh, i just saw some examples, this version is a lot better
#SELECT e.`first name`, e.`last name`, o.`ship city`
#FROM (select *
#   from orders
#   where `ship state/province` = 'CA') o, employees e
#WHERE p.category = 'sauces'
"""
+------------+----------------+---------------+------------------+-------------+
| first name | last name      | first name    | last name        | ship city   |
+------------+----------------+---------------+------------------+-------------+
| Nancy      | Freehafer      | Anna          | Bedecs           | Los Angelas |
| Andrew     | Cencini        | Anna          | Bedecs           | Los Angelas |
| Jan        | Kotas          | Anna          | Bedecs           | Los Angelas |
| Mariya     | Sergienko      | Anna          | Bedecs           | Los Angelas |
...
"""
#this is the one that has a lot. that seems right!
#now what about this concat thing???
