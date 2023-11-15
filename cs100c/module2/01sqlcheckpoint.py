#well, look, i have to make some kind of file! i need to sleep on this hard!!!
#so i got the file to kind of work by converting it to ansi with notepad++
#anyway, so now, it's complaining about my syntax
#and why do people always write it in multiple lines? am i doing this right???
#well, i got to a point where it returned an empty set and now idk
#SELECT * FROM Customers WHERE 'Job Title' = 'Owner';

#reminder on how to get there, in case you forget
#cd bin
#mariadb -u root -p
#source C:\database\change.sql

#now, looking at the file opening... there are a LOT of errors, so that might be part of the problem
#idk tho. can i ask about this?


#oh, i got it to work with student
#apparently the arrows are it just asking for a semicolon, so that's kind of nice

#haha, this is what I get when I try to select 'first name' from customers

"""
+------------+
| First Name |
+------------+
| First Name |
| First Name |
| First Name |
| First Name |
| First Name |
| First Name |
| First Name |
| First Name |
| First Name |
| First Name |
| First Name |
| First Name |
| First Name |
| First Name |
| First Name |
| First Name |
| First Name |
+------------+
"""

#also, how do you deal with... things that have spaces in the names?
#you use... back quotes!!! for things like table names & attributes!!!
#you also use double quotes for quotations in sql

#BASIC SQL

#1. look at this, i had to select distinct
#select distinct `first name` from customers where `job title` = 'owner';
"""
+---------------+
| first name    |
+---------------+
| Anna          |
| Antonio       |
| Martin        |
| Ming-Yang     |
| Jean Philippe |
| Jonas         |
+---------------+
"""
#2. select distinct `first name`, `last name`, `company` from customers where `job title` = 'owner';
#something's going on with my files!!! look, i've still got funky o'donnell in there somewhere!!!
"""
+---------------+------------------+-----------+
| first name    | last name        | company   |
+---------------+------------------+-----------+
| Anna          | Bedecs           | Company A |
| Antonio       | Gratacos Solsona | Company B |
| Martin        | OÆDonnell        | Company E |
| Martin        | O'Donnell        | Company E |
| Ming-Yang     | Xie              | Company G |
| Jean Philippe | Bagel            | Company Q |
| Jonas         | Hasselberg       | Company X |
+---------------+------------------+-----------+
"""
#i don't get it!!! i only see this o'donnell guy once in the file i am using
#am i going to have to come in and ask about this again???
#i swear, this sql stuff, like, i have no idea how even to ask the internet about it!!!

#3. oh great, i was just going to do this last one, and it is being weird too!!!
#select `product name` and `standard cost` and `list price` from products where `list price` < 20;
"""
+-----------------------------------------------------+
| `product name` and `standard cost` and `list price` |
+-----------------------------------------------------+
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
...
"""
#seriously???
#ok, well, let me just have lunch first, and then...
#well, i feel like i should experiment more with solutions to these problems, right???
#i'll see if i can get anywhere today

#oh bother!!! i keep forgetting and putting 'and' between attributes
"""
+------------------------------------------+---------------+------------+
| product name                             | standard cost | list price |
+------------------------------------------+---------------+------------+
| Northwind Traders Chai                   | 13.50         | 18.00      |
| Northwind Traders Syrup                  | 7.50          | 10.00      |
| Northwind Traders Chocolate Biscuits Mix | 6.90          | 9.20       |
| Northwind Traders Scones                 | 7.50          | 10.00      |
...
"""
#so it's select `product name`, `standard cost`, `list price` from products where `list price` < 20;
#well there, that one's working, but i'm still not sure about funky o'donnell. oh well

#MORE SQL

#1. well... i finally got it to the point where it gave me an empty set (sign of progress???)
#for a while there i was using 'for' instead of 'from', but i finally fixed that!!!
#SELECT e.`First Name`, e.`Last Name`, o.`Ship City`
#FROM `employees` e, `orders` o
#WHERE o.`employee id` = e.`id` and o.`ship city` = 'california'
#oh, i had to abbreviate california!! AND use state/province instead of city
#SELECT e.`First Name`, e.`Last Name`, o.`Ship State/Province`
#FROM `Employees` e, `Orders` o
#WHERE o.`Employee ID` = e.`ID` and o.`Ship State/Province` = 'CA';
"""
+------------+-----------+---------------------+
| First Name | Last Name | Ship State/Province |
+------------+-----------+---------------------+
| Mariya     | Sergienko | CA                  |
| Mariya     | Sergienko | CA                  |
| Mariya     | Sergienko | CA                  |
| Mariya     | Sergienko | CA                  |
| Mariya     | Sergienko | CA                  |
| Mariya     | Sergienko | CA                  |
| Mariya     | Sergienko | CA                  |
| Mariya     | Sergienko | CA                  |
| Mariya     | Sergienko | CA                  |
| Mariya     | Sergienko | CA                  |
| Andrew     | Cencini   | CA                  |
| Andrew     | Cencini   | CA                  |
| Andrew     | Cencini   | CA                  |
| Andrew     | Cencini   | CA                  |
| Andrew     | Cencini   | CA                  |
+------------+-----------+---------------------+
"""
#2. 
#SELECT c.`First Name`, c.`Last Name`, o.`Ship State/Province`
#FROM `Customers` c, `Orders` o
#WHERE o.`Customer ID` = c.`ID` and o.`Ship State/Province` = 'CA';
"""
+------------+-----------+---------------------+
| First Name | Last Name | Ship State/Province |
+------------+-----------+---------------------+
| Thomas     | Axen      | CA                  |
| Thomas     | Axen      | CA                  |
| Thomas     | Axen      | CA                  |
| Thomas     | Axen      | CA                  |
...
"""
#the only customer in california...

#3. 
#SELECT e.`First Name`, e.`Last Name`, c.`First Name`, c.`Last Name`, o.`Ship City`
#FROM `Employees` e, `Customers` c, `Orders` o
#WHERE o.`Employee ID` = e.`ID` and o.`Customer ID` = c.`ID` and o.`Ship State/Province` = 'CA';
#well, look at that, this is a lot longer than my first table!
"""
+------------+-----------+------------+-----------+---------------------+
| First Name | Last Name | First Name | Last Name | Ship State/Province |
+------------+-----------+------------+-----------+---------------------+
| Mariya     | Sergienko | Thomas     | Axen      | CA                  |
| Mariya     | Sergienko | Thomas     | Axen      | CA                  |
| Mariya     | Sergienko | Thomas     | Axen      | CA                  |
| Mariya     | Sergienko | Thomas     | Axen      | CA                  |
....................
"""
#file that under 'weird sql questions'...
#oh wait, i'm structuring this wrong, or something!
#SELECT e.`First Name`, e.`Last Name`, c.`First Name`, c.`Last Name`, o.`Ship State/Province`
#FROM `Employees` e, `Customers` c, `Orders` o
#WHERE o.`Employee ID` = e.`ID` and o.`Ship State/Province` = 'CA';
#whoaaa. now i got a totally different table for this one.
"""
+------------+-----------+---------------+------------------+---------------------+
| First Name | Last Name | First Name    | Last Name        | Ship State/Province |
+------------+-----------+---------------+------------------+---------------------+
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Andrew     | Cencini   | Anna          | Bedecs           | CA                  |
| Andrew     | Cencini   | Anna          | Bedecs           | CA                  |
| Andrew     | Cencini   | Anna          | Bedecs           | CA                  |
| Andrew     | Cencini   | Anna          | Bedecs           | CA                  |
| Andrew     | Cencini   | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Andrew     | Cencini   | Antonio       | Gratacos Solsona | CA                  |
| Andrew     | Cencini   | Antonio       | Gratacos Solsona | CA                  |
| Andrew     | Cencini   | Antonio       | Gratacos Solsona | CA                  |
| Andrew     | Cencini   | Antonio       | Gratacos Solsona | CA                  |
| Andrew     | Cencini   | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Andrew     | Cencini   | Thomas        | Axen             | CA                  |
| Andrew     | Cencini   | Thomas        | Axen             | CA                  |
| Andrew     | Cencini   | Thomas        | Axen             | CA                  |
| Andrew     | Cencini   | Thomas        | Axen             | CA                  |
| Andrew     | Cencini   | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Andrew     | Cencini   | Christina     | Lee              | CA                  |
| Andrew     | Cencini   | Christina     | Lee              | CA                  |
| Andrew     | Cencini   | Christina     | Lee              | CA                  |
| Andrew     | Cencini   | Christina     | Lee              | CA                  |
| Andrew     | Cencini   | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Martin        | OÆDonnell        | CA                  |
| Mariya     | Sergienko | Martin        | OÆDonnell        | CA                  |
| Mariya     | Sergienko | Martin        | OÆDonnell        | CA                  |
| Mariya     | Sergienko | Martin        | OÆDonnell        | CA                  |
| Mariya     | Sergienko | Martin        | OÆDonnell        | CA                  |
| Mariya     | Sergienko | Martin        | OÆDonnell        | CA                  |
| Mariya     | Sergienko | Martin        | OÆDonnell        | CA                  |
| Mariya     | Sergienko | Martin        | OÆDonnell        | CA                  |
| Mariya     | Sergienko | Martin        | OÆDonnell        | CA                  |
| Mariya     | Sergienko | Martin        | OÆDonnell        | CA                  |
| Andrew     | Cencini   | Martin        | OÆDonnell        | CA                  |
| Andrew     | Cencini   | Martin        | OÆDonnell        | CA                  |
| Andrew     | Cencini   | Martin        | OÆDonnell        | CA                  |
| Andrew     | Cencini   | Martin        | OÆDonnell        | CA                  |
| Andrew     | Cencini   | Martin        | OÆDonnell        | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Andrew     | Cencini   | Anna          | Bedecs           | CA                  |
| Andrew     | Cencini   | Anna          | Bedecs           | CA                  |
| Andrew     | Cencini   | Anna          | Bedecs           | CA                  |
| Andrew     | Cencini   | Anna          | Bedecs           | CA                  |
| Andrew     | Cencini   | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Andrew     | Cencini   | Antonio       | Gratacos Solsona | CA                  |
| Andrew     | Cencini   | Antonio       | Gratacos Solsona | CA                  |
| Andrew     | Cencini   | Antonio       | Gratacos Solsona | CA                  |
| Andrew     | Cencini   | Antonio       | Gratacos Solsona | CA                  |
| Andrew     | Cencini   | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Andrew     | Cencini   | Thomas        | Axen             | CA                  |
| Andrew     | Cencini   | Thomas        | Axen             | CA                  |
| Andrew     | Cencini   | Thomas        | Axen             | CA                  |
| Andrew     | Cencini   | Thomas        | Axen             | CA                  |
| Andrew     | Cencini   | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Andrew     | Cencini   | Christina     | Lee              | CA                  |
| Andrew     | Cencini   | Christina     | Lee              | CA                  |
| Andrew     | Cencini   | Christina     | Lee              | CA                  |
| Andrew     | Cencini   | Christina     | Lee              | CA                  |
| Andrew     | Cencini   | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Andrew     | Cencini   | Anna          | Bedecs           | CA                  |
| Andrew     | Cencini   | Anna          | Bedecs           | CA                  |
| Andrew     | Cencini   | Anna          | Bedecs           | CA                  |
| Andrew     | Cencini   | Anna          | Bedecs           | CA                  |
| Andrew     | Cencini   | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Andrew     | Cencini   | Antonio       | Gratacos Solsona | CA                  |
| Andrew     | Cencini   | Antonio       | Gratacos Solsona | CA                  |
| Andrew     | Cencini   | Antonio       | Gratacos Solsona | CA                  |
| Andrew     | Cencini   | Antonio       | Gratacos Solsona | CA                  |
| Andrew     | Cencini   | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Andrew     | Cencini   | Thomas        | Axen             | CA                  |
| Andrew     | Cencini   | Thomas        | Axen             | CA                  |
| Andrew     | Cencini   | Thomas        | Axen             | CA                  |
| Andrew     | Cencini   | Thomas        | Axen             | CA                  |
| Andrew     | Cencini   | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Andrew     | Cencini   | Christina     | Lee              | CA                  |
| Andrew     | Cencini   | Christina     | Lee              | CA                  |
| Andrew     | Cencini   | Christina     | Lee              | CA                  |
| Andrew     | Cencini   | Christina     | Lee              | CA                  |
| Andrew     | Cencini   | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Andrew     | Cencini   | Anna          | Bedecs           | CA                  |
| Andrew     | Cencini   | Anna          | Bedecs           | CA                  |
| Andrew     | Cencini   | Anna          | Bedecs           | CA                  |
| Andrew     | Cencini   | Anna          | Bedecs           | CA                  |
| Andrew     | Cencini   | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Andrew     | Cencini   | Antonio       | Gratacos Solsona | CA                  |
| Andrew     | Cencini   | Antonio       | Gratacos Solsona | CA                  |
| Andrew     | Cencini   | Antonio       | Gratacos Solsona | CA                  |
| Andrew     | Cencini   | Antonio       | Gratacos Solsona | CA                  |
| Andrew     | Cencini   | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Andrew     | Cencini   | Thomas        | Axen             | CA                  |
| Andrew     | Cencini   | Thomas        | Axen             | CA                  |
| Andrew     | Cencini   | Thomas        | Axen             | CA                  |
| Andrew     | Cencini   | Thomas        | Axen             | CA                  |
| Andrew     | Cencini   | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Andrew     | Cencini   | Christina     | Lee              | CA                  |
| Andrew     | Cencini   | Christina     | Lee              | CA                  |
| Andrew     | Cencini   | Christina     | Lee              | CA                  |
| Andrew     | Cencini   | Christina     | Lee              | CA                  |
| Andrew     | Cencini   | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Andrew     | Cencini   | Anna          | Bedecs           | CA                  |
| Andrew     | Cencini   | Anna          | Bedecs           | CA                  |
| Andrew     | Cencini   | Anna          | Bedecs           | CA                  |
| Andrew     | Cencini   | Anna          | Bedecs           | CA                  |
| Andrew     | Cencini   | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Andrew     | Cencini   | Antonio       | Gratacos Solsona | CA                  |
| Andrew     | Cencini   | Antonio       | Gratacos Solsona | CA                  |
| Andrew     | Cencini   | Antonio       | Gratacos Solsona | CA                  |
| Andrew     | Cencini   | Antonio       | Gratacos Solsona | CA                  |
| Andrew     | Cencini   | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Andrew     | Cencini   | Thomas        | Axen             | CA                  |
| Andrew     | Cencini   | Thomas        | Axen             | CA                  |
| Andrew     | Cencini   | Thomas        | Axen             | CA                  |
| Andrew     | Cencini   | Thomas        | Axen             | CA                  |
| Andrew     | Cencini   | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Andrew     | Cencini   | Christina     | Lee              | CA                  |
| Andrew     | Cencini   | Christina     | Lee              | CA                  |
| Andrew     | Cencini   | Christina     | Lee              | CA                  |
| Andrew     | Cencini   | Christina     | Lee              | CA                  |
| Andrew     | Cencini   | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Andrew     | Cencini   | Anna          | Bedecs           | CA                  |
| Andrew     | Cencini   | Anna          | Bedecs           | CA                  |
| Andrew     | Cencini   | Anna          | Bedecs           | CA                  |
| Andrew     | Cencini   | Anna          | Bedecs           | CA                  |
| Andrew     | Cencini   | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Andrew     | Cencini   | Antonio       | Gratacos Solsona | CA                  |
| Andrew     | Cencini   | Antonio       | Gratacos Solsona | CA                  |
| Andrew     | Cencini   | Antonio       | Gratacos Solsona | CA                  |
| Andrew     | Cencini   | Antonio       | Gratacos Solsona | CA                  |
| Andrew     | Cencini   | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Andrew     | Cencini   | Thomas        | Axen             | CA                  |
| Andrew     | Cencini   | Thomas        | Axen             | CA                  |
| Andrew     | Cencini   | Thomas        | Axen             | CA                  |
| Andrew     | Cencini   | Thomas        | Axen             | CA                  |
| Andrew     | Cencini   | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Andrew     | Cencini   | Christina     | Lee              | CA                  |
| Andrew     | Cencini   | Christina     | Lee              | CA                  |
| Andrew     | Cencini   | Christina     | Lee              | CA                  |
| Andrew     | Cencini   | Christina     | Lee              | CA                  |
| Andrew     | Cencini   | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Andrew     | Cencini   | Anna          | Bedecs           | CA                  |
| Andrew     | Cencini   | Anna          | Bedecs           | CA                  |
| Andrew     | Cencini   | Anna          | Bedecs           | CA                  |
| Andrew     | Cencini   | Anna          | Bedecs           | CA                  |
| Andrew     | Cencini   | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Andrew     | Cencini   | Antonio       | Gratacos Solsona | CA                  |
| Andrew     | Cencini   | Antonio       | Gratacos Solsona | CA                  |
| Andrew     | Cencini   | Antonio       | Gratacos Solsona | CA                  |
| Andrew     | Cencini   | Antonio       | Gratacos Solsona | CA                  |
| Andrew     | Cencini   | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Andrew     | Cencini   | Thomas        | Axen             | CA                  |
| Andrew     | Cencini   | Thomas        | Axen             | CA                  |
| Andrew     | Cencini   | Thomas        | Axen             | CA                  |
| Andrew     | Cencini   | Thomas        | Axen             | CA                  |
| Andrew     | Cencini   | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Andrew     | Cencini   | Christina     | Lee              | CA                  |
| Andrew     | Cencini   | Christina     | Lee              | CA                  |
| Andrew     | Cencini   | Christina     | Lee              | CA                  |
| Andrew     | Cencini   | Christina     | Lee              | CA                  |
| Andrew     | Cencini   | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Andrew     | Cencini   | Anna          | Bedecs           | CA                  |
| Andrew     | Cencini   | Anna          | Bedecs           | CA                  |
| Andrew     | Cencini   | Anna          | Bedecs           | CA                  |
| Andrew     | Cencini   | Anna          | Bedecs           | CA                  |
| Andrew     | Cencini   | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Andrew     | Cencini   | Antonio       | Gratacos Solsona | CA                  |
| Andrew     | Cencini   | Antonio       | Gratacos Solsona | CA                  |
| Andrew     | Cencini   | Antonio       | Gratacos Solsona | CA                  |
| Andrew     | Cencini   | Antonio       | Gratacos Solsona | CA                  |
| Andrew     | Cencini   | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Andrew     | Cencini   | Thomas        | Axen             | CA                  |
| Andrew     | Cencini   | Thomas        | Axen             | CA                  |
| Andrew     | Cencini   | Thomas        | Axen             | CA                  |
| Andrew     | Cencini   | Thomas        | Axen             | CA                  |
| Andrew     | Cencini   | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Andrew     | Cencini   | Christina     | Lee              | CA                  |
| Andrew     | Cencini   | Christina     | Lee              | CA                  |
| Andrew     | Cencini   | Christina     | Lee              | CA                  |
| Andrew     | Cencini   | Christina     | Lee              | CA                  |
| Andrew     | Cencini   | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Martin        | O'Donnell        | CA                  |
| Mariya     | Sergienko | Martin        | O'Donnell        | CA                  |
| Mariya     | Sergienko | Martin        | O'Donnell        | CA                  |
| Mariya     | Sergienko | Martin        | O'Donnell        | CA                  |
| Mariya     | Sergienko | Martin        | O'Donnell        | CA                  |
| Mariya     | Sergienko | Martin        | O'Donnell        | CA                  |
| Mariya     | Sergienko | Martin        | O'Donnell        | CA                  |
| Mariya     | Sergienko | Martin        | O'Donnell        | CA                  |
| Mariya     | Sergienko | Martin        | O'Donnell        | CA                  |
| Mariya     | Sergienko | Martin        | O'Donnell        | CA                  |
| Andrew     | Cencini   | Martin        | O'Donnell        | CA                  |
| Andrew     | Cencini   | Martin        | O'Donnell        | CA                  |
| Andrew     | Cencini   | Martin        | O'Donnell        | CA                  |
| Andrew     | Cencini   | Martin        | O'Donnell        | CA                  |
| Andrew     | Cencini   | Martin        | O'Donnell        | CA                  |
| Mariya     | Sergienko | Francisco     | Perez-Olaeta     | CA                  |
| Mariya     | Sergienko | Francisco     | Perez-Olaeta     | CA                  |
| Mariya     | Sergienko | Francisco     | Perez-Olaeta     | CA                  |
| Mariya     | Sergienko | Francisco     | Perez-Olaeta     | CA                  |
| Mariya     | Sergienko | Francisco     | Perez-Olaeta     | CA                  |
| Mariya     | Sergienko | Francisco     | Perez-Olaeta     | CA                  |
| Mariya     | Sergienko | Francisco     | Perez-Olaeta     | CA                  |
| Mariya     | Sergienko | Francisco     | Perez-Olaeta     | CA                  |
| Mariya     | Sergienko | Francisco     | Perez-Olaeta     | CA                  |
| Mariya     | Sergienko | Francisco     | Perez-Olaeta     | CA                  |
| Andrew     | Cencini   | Francisco     | Perez-Olaeta     | CA                  |
| Andrew     | Cencini   | Francisco     | Perez-Olaeta     | CA                  |
| Andrew     | Cencini   | Francisco     | Perez-Olaeta     | CA                  |
| Andrew     | Cencini   | Francisco     | Perez-Olaeta     | CA                  |
| Andrew     | Cencini   | Francisco     | Perez-Olaeta     | CA                  |
| Mariya     | Sergienko | Ming-Yang     | Xie              | CA                  |
| Mariya     | Sergienko | Ming-Yang     | Xie              | CA                  |
| Mariya     | Sergienko | Ming-Yang     | Xie              | CA                  |
| Mariya     | Sergienko | Ming-Yang     | Xie              | CA                  |
| Mariya     | Sergienko | Ming-Yang     | Xie              | CA                  |
| Mariya     | Sergienko | Ming-Yang     | Xie              | CA                  |
| Mariya     | Sergienko | Ming-Yang     | Xie              | CA                  |
| Mariya     | Sergienko | Ming-Yang     | Xie              | CA                  |
| Mariya     | Sergienko | Ming-Yang     | Xie              | CA                  |
| Mariya     | Sergienko | Ming-Yang     | Xie              | CA                  |
| Andrew     | Cencini   | Ming-Yang     | Xie              | CA                  |
| Andrew     | Cencini   | Ming-Yang     | Xie              | CA                  |
| Andrew     | Cencini   | Ming-Yang     | Xie              | CA                  |
| Andrew     | Cencini   | Ming-Yang     | Xie              | CA                  |
| Andrew     | Cencini   | Ming-Yang     | Xie              | CA                  |
| Mariya     | Sergienko | Elizabeth     | Andersen         | CA                  |
| Mariya     | Sergienko | Elizabeth     | Andersen         | CA                  |
| Mariya     | Sergienko | Elizabeth     | Andersen         | CA                  |
| Mariya     | Sergienko | Elizabeth     | Andersen         | CA                  |
| Mariya     | Sergienko | Elizabeth     | Andersen         | CA                  |
| Mariya     | Sergienko | Elizabeth     | Andersen         | CA                  |
| Mariya     | Sergienko | Elizabeth     | Andersen         | CA                  |
| Mariya     | Sergienko | Elizabeth     | Andersen         | CA                  |
| Mariya     | Sergienko | Elizabeth     | Andersen         | CA                  |
| Mariya     | Sergienko | Elizabeth     | Andersen         | CA                  |
| Andrew     | Cencini   | Elizabeth     | Andersen         | CA                  |
| Andrew     | Cencini   | Elizabeth     | Andersen         | CA                  |
| Andrew     | Cencini   | Elizabeth     | Andersen         | CA                  |
| Andrew     | Cencini   | Elizabeth     | Andersen         | CA                  |
| Andrew     | Cencini   | Elizabeth     | Andersen         | CA                  |
| Mariya     | Sergienko | Sven          | Mortensen        | CA                  |
| Mariya     | Sergienko | Sven          | Mortensen        | CA                  |
| Mariya     | Sergienko | Sven          | Mortensen        | CA                  |
| Mariya     | Sergienko | Sven          | Mortensen        | CA                  |
| Mariya     | Sergienko | Sven          | Mortensen        | CA                  |
| Mariya     | Sergienko | Sven          | Mortensen        | CA                  |
| Mariya     | Sergienko | Sven          | Mortensen        | CA                  |
| Mariya     | Sergienko | Sven          | Mortensen        | CA                  |
| Mariya     | Sergienko | Sven          | Mortensen        | CA                  |
| Mariya     | Sergienko | Sven          | Mortensen        | CA                  |
| Andrew     | Cencini   | Sven          | Mortensen        | CA                  |
| Andrew     | Cencini   | Sven          | Mortensen        | CA                  |
| Andrew     | Cencini   | Sven          | Mortensen        | CA                  |
| Andrew     | Cencini   | Sven          | Mortensen        | CA                  |
| Andrew     | Cencini   | Sven          | Mortensen        | CA                  |
| Mariya     | Sergienko | Roland        | Wacker           | CA                  |
| Mariya     | Sergienko | Roland        | Wacker           | CA                  |
| Mariya     | Sergienko | Roland        | Wacker           | CA                  |
| Mariya     | Sergienko | Roland        | Wacker           | CA                  |
| Mariya     | Sergienko | Roland        | Wacker           | CA                  |
| Mariya     | Sergienko | Roland        | Wacker           | CA                  |
| Mariya     | Sergienko | Roland        | Wacker           | CA                  |
| Mariya     | Sergienko | Roland        | Wacker           | CA                  |
| Mariya     | Sergienko | Roland        | Wacker           | CA                  |
| Mariya     | Sergienko | Roland        | Wacker           | CA                  |
| Andrew     | Cencini   | Roland        | Wacker           | CA                  |
| Andrew     | Cencini   | Roland        | Wacker           | CA                  |
| Andrew     | Cencini   | Roland        | Wacker           | CA                  |
| Andrew     | Cencini   | Roland        | Wacker           | CA                  |
| Andrew     | Cencini   | Roland        | Wacker           | CA                  |
| Mariya     | Sergienko | Peter         | Krschne          | CA                  |
| Mariya     | Sergienko | Peter         | Krschne          | CA                  |
| Mariya     | Sergienko | Peter         | Krschne          | CA                  |
| Mariya     | Sergienko | Peter         | Krschne          | CA                  |
| Mariya     | Sergienko | Peter         | Krschne          | CA                  |
| Mariya     | Sergienko | Peter         | Krschne          | CA                  |
| Mariya     | Sergienko | Peter         | Krschne          | CA                  |
| Mariya     | Sergienko | Peter         | Krschne          | CA                  |
| Mariya     | Sergienko | Peter         | Krschne          | CA                  |
| Mariya     | Sergienko | Peter         | Krschne          | CA                  |
| Andrew     | Cencini   | Peter         | Krschne          | CA                  |
| Andrew     | Cencini   | Peter         | Krschne          | CA                  |
| Andrew     | Cencini   | Peter         | Krschne          | CA                  |
| Andrew     | Cencini   | Peter         | Krschne          | CA                  |
| Andrew     | Cencini   | Peter         | Krschne          | CA                  |
| Mariya     | Sergienko | John          | Edwards          | CA                  |
| Mariya     | Sergienko | John          | Edwards          | CA                  |
| Mariya     | Sergienko | John          | Edwards          | CA                  |
| Mariya     | Sergienko | John          | Edwards          | CA                  |
| Mariya     | Sergienko | John          | Edwards          | CA                  |
| Mariya     | Sergienko | John          | Edwards          | CA                  |
| Mariya     | Sergienko | John          | Edwards          | CA                  |
| Mariya     | Sergienko | John          | Edwards          | CA                  |
| Mariya     | Sergienko | John          | Edwards          | CA                  |
| Mariya     | Sergienko | John          | Edwards          | CA                  |
| Andrew     | Cencini   | John          | Edwards          | CA                  |
| Andrew     | Cencini   | John          | Edwards          | CA                  |
| Andrew     | Cencini   | John          | Edwards          | CA                  |
| Andrew     | Cencini   | John          | Edwards          | CA                  |
| Andrew     | Cencini   | John          | Edwards          | CA                  |
| Mariya     | Sergienko | Andre         | Ludick           | CA                  |
| Mariya     | Sergienko | Andre         | Ludick           | CA                  |
| Mariya     | Sergienko | Andre         | Ludick           | CA                  |
| Mariya     | Sergienko | Andre         | Ludick           | CA                  |
| Mariya     | Sergienko | Andre         | Ludick           | CA                  |
| Mariya     | Sergienko | Andre         | Ludick           | CA                  |
| Mariya     | Sergienko | Andre         | Ludick           | CA                  |
| Mariya     | Sergienko | Andre         | Ludick           | CA                  |
| Mariya     | Sergienko | Andre         | Ludick           | CA                  |
| Mariya     | Sergienko | Andre         | Ludick           | CA                  |
| Andrew     | Cencini   | Andre         | Ludick           | CA                  |
| Andrew     | Cencini   | Andre         | Ludick           | CA                  |
| Andrew     | Cencini   | Andre         | Ludick           | CA                  |
| Andrew     | Cencini   | Andre         | Ludick           | CA                  |
| Andrew     | Cencini   | Andre         | Ludick           | CA                  |
| Mariya     | Sergienko | Carlos        | Grilo            | CA                  |
| Mariya     | Sergienko | Carlos        | Grilo            | CA                  |
| Mariya     | Sergienko | Carlos        | Grilo            | CA                  |
| Mariya     | Sergienko | Carlos        | Grilo            | CA                  |
| Mariya     | Sergienko | Carlos        | Grilo            | CA                  |
| Mariya     | Sergienko | Carlos        | Grilo            | CA                  |
| Mariya     | Sergienko | Carlos        | Grilo            | CA                  |
| Mariya     | Sergienko | Carlos        | Grilo            | CA                  |
| Mariya     | Sergienko | Carlos        | Grilo            | CA                  |
| Mariya     | Sergienko | Carlos        | Grilo            | CA                  |
| Andrew     | Cencini   | Carlos        | Grilo            | CA                  |
| Andrew     | Cencini   | Carlos        | Grilo            | CA                  |
| Andrew     | Cencini   | Carlos        | Grilo            | CA                  |
| Andrew     | Cencini   | Carlos        | Grilo            | CA                  |
| Andrew     | Cencini   | Carlos        | Grilo            | CA                  |
| Mariya     | Sergienko | Helena        | Kupkova          | CA                  |
| Mariya     | Sergienko | Helena        | Kupkova          | CA                  |
| Mariya     | Sergienko | Helena        | Kupkova          | CA                  |
| Mariya     | Sergienko | Helena        | Kupkova          | CA                  |
| Mariya     | Sergienko | Helena        | Kupkova          | CA                  |
| Mariya     | Sergienko | Helena        | Kupkova          | CA                  |
| Mariya     | Sergienko | Helena        | Kupkova          | CA                  |
| Mariya     | Sergienko | Helena        | Kupkova          | CA                  |
| Mariya     | Sergienko | Helena        | Kupkova          | CA                  |
| Mariya     | Sergienko | Helena        | Kupkova          | CA                  |
| Andrew     | Cencini   | Helena        | Kupkova          | CA                  |
| Andrew     | Cencini   | Helena        | Kupkova          | CA                  |
| Andrew     | Cencini   | Helena        | Kupkova          | CA                  |
| Andrew     | Cencini   | Helena        | Kupkova          | CA                  |
| Andrew     | Cencini   | Helena        | Kupkova          | CA                  |
| Mariya     | Sergienko | Daniel        | Goldschmidt      | CA                  |
| Mariya     | Sergienko | Daniel        | Goldschmidt      | CA                  |
| Mariya     | Sergienko | Daniel        | Goldschmidt      | CA                  |
| Mariya     | Sergienko | Daniel        | Goldschmidt      | CA                  |
| Mariya     | Sergienko | Daniel        | Goldschmidt      | CA                  |
| Mariya     | Sergienko | Daniel        | Goldschmidt      | CA                  |
| Mariya     | Sergienko | Daniel        | Goldschmidt      | CA                  |
| Mariya     | Sergienko | Daniel        | Goldschmidt      | CA                  |
| Mariya     | Sergienko | Daniel        | Goldschmidt      | CA                  |
| Mariya     | Sergienko | Daniel        | Goldschmidt      | CA                  |
| Andrew     | Cencini   | Daniel        | Goldschmidt      | CA                  |
| Andrew     | Cencini   | Daniel        | Goldschmidt      | CA                  |
| Andrew     | Cencini   | Daniel        | Goldschmidt      | CA                  |
| Andrew     | Cencini   | Daniel        | Goldschmidt      | CA                  |
| Andrew     | Cencini   | Daniel        | Goldschmidt      | CA                  |
| Mariya     | Sergienko | Jean Philippe | Bagel            | CA                  |
| Mariya     | Sergienko | Jean Philippe | Bagel            | CA                  |
| Mariya     | Sergienko | Jean Philippe | Bagel            | CA                  |
| Mariya     | Sergienko | Jean Philippe | Bagel            | CA                  |
| Mariya     | Sergienko | Jean Philippe | Bagel            | CA                  |
| Mariya     | Sergienko | Jean Philippe | Bagel            | CA                  |
| Mariya     | Sergienko | Jean Philippe | Bagel            | CA                  |
| Mariya     | Sergienko | Jean Philippe | Bagel            | CA                  |
| Mariya     | Sergienko | Jean Philippe | Bagel            | CA                  |
| Mariya     | Sergienko | Jean Philippe | Bagel            | CA                  |
| Andrew     | Cencini   | Jean Philippe | Bagel            | CA                  |
| Andrew     | Cencini   | Jean Philippe | Bagel            | CA                  |
| Andrew     | Cencini   | Jean Philippe | Bagel            | CA                  |
| Andrew     | Cencini   | Jean Philippe | Bagel            | CA                  |
| Andrew     | Cencini   | Jean Philippe | Bagel            | CA                  |
| Mariya     | Sergienko | Catherine     | Autier Miconi    | CA                  |
| Mariya     | Sergienko | Catherine     | Autier Miconi    | CA                  |
| Mariya     | Sergienko | Catherine     | Autier Miconi    | CA                  |
| Mariya     | Sergienko | Catherine     | Autier Miconi    | CA                  |
| Mariya     | Sergienko | Catherine     | Autier Miconi    | CA                  |
| Mariya     | Sergienko | Catherine     | Autier Miconi    | CA                  |
| Mariya     | Sergienko | Catherine     | Autier Miconi    | CA                  |
| Mariya     | Sergienko | Catherine     | Autier Miconi    | CA                  |
| Mariya     | Sergienko | Catherine     | Autier Miconi    | CA                  |
| Mariya     | Sergienko | Catherine     | Autier Miconi    | CA                  |
| Andrew     | Cencini   | Catherine     | Autier Miconi    | CA                  |
| Andrew     | Cencini   | Catherine     | Autier Miconi    | CA                  |
| Andrew     | Cencini   | Catherine     | Autier Miconi    | CA                  |
| Andrew     | Cencini   | Catherine     | Autier Miconi    | CA                  |
| Andrew     | Cencini   | Catherine     | Autier Miconi    | CA                  |
| Mariya     | Sergienko | Alexander     | Eggerer          | CA                  |
| Mariya     | Sergienko | Alexander     | Eggerer          | CA                  |
| Mariya     | Sergienko | Alexander     | Eggerer          | CA                  |
| Mariya     | Sergienko | Alexander     | Eggerer          | CA                  |
| Mariya     | Sergienko | Alexander     | Eggerer          | CA                  |
| Mariya     | Sergienko | Alexander     | Eggerer          | CA                  |
| Mariya     | Sergienko | Alexander     | Eggerer          | CA                  |
| Mariya     | Sergienko | Alexander     | Eggerer          | CA                  |
| Mariya     | Sergienko | Alexander     | Eggerer          | CA                  |
| Mariya     | Sergienko | Alexander     | Eggerer          | CA                  |
| Andrew     | Cencini   | Alexander     | Eggerer          | CA                  |
| Andrew     | Cencini   | Alexander     | Eggerer          | CA                  |
| Andrew     | Cencini   | Alexander     | Eggerer          | CA                  |
| Andrew     | Cencini   | Alexander     | Eggerer          | CA                  |
| Andrew     | Cencini   | Alexander     | Eggerer          | CA                  |
| Mariya     | Sergienko | George        | Li               | CA                  |
| Mariya     | Sergienko | George        | Li               | CA                  |
| Mariya     | Sergienko | George        | Li               | CA                  |
| Mariya     | Sergienko | George        | Li               | CA                  |
| Mariya     | Sergienko | George        | Li               | CA                  |
| Mariya     | Sergienko | George        | Li               | CA                  |
| Mariya     | Sergienko | George        | Li               | CA                  |
| Mariya     | Sergienko | George        | Li               | CA                  |
| Mariya     | Sergienko | George        | Li               | CA                  |
| Mariya     | Sergienko | George        | Li               | CA                  |
| Andrew     | Cencini   | George        | Li               | CA                  |
| Andrew     | Cencini   | George        | Li               | CA                  |
| Andrew     | Cencini   | George        | Li               | CA                  |
| Andrew     | Cencini   | George        | Li               | CA                  |
| Andrew     | Cencini   | George        | Li               | CA                  |
| Mariya     | Sergienko | Bernard       | Tham             | CA                  |
| Mariya     | Sergienko | Bernard       | Tham             | CA                  |
| Mariya     | Sergienko | Bernard       | Tham             | CA                  |
| Mariya     | Sergienko | Bernard       | Tham             | CA                  |
| Mariya     | Sergienko | Bernard       | Tham             | CA                  |
| Mariya     | Sergienko | Bernard       | Tham             | CA                  |
| Mariya     | Sergienko | Bernard       | Tham             | CA                  |
| Mariya     | Sergienko | Bernard       | Tham             | CA                  |
| Mariya     | Sergienko | Bernard       | Tham             | CA                  |
| Mariya     | Sergienko | Bernard       | Tham             | CA                  |
| Andrew     | Cencini   | Bernard       | Tham             | CA                  |
| Andrew     | Cencini   | Bernard       | Tham             | CA                  |
| Andrew     | Cencini   | Bernard       | Tham             | CA                  |
| Andrew     | Cencini   | Bernard       | Tham             | CA                  |
| Andrew     | Cencini   | Bernard       | Tham             | CA                  |
| Mariya     | Sergienko | Luciana       | Ramos            | CA                  |
| Mariya     | Sergienko | Luciana       | Ramos            | CA                  |
| Mariya     | Sergienko | Luciana       | Ramos            | CA                  |
| Mariya     | Sergienko | Luciana       | Ramos            | CA                  |
| Mariya     | Sergienko | Luciana       | Ramos            | CA                  |
| Mariya     | Sergienko | Luciana       | Ramos            | CA                  |
| Mariya     | Sergienko | Luciana       | Ramos            | CA                  |
| Mariya     | Sergienko | Luciana       | Ramos            | CA                  |
| Mariya     | Sergienko | Luciana       | Ramos            | CA                  |
| Mariya     | Sergienko | Luciana       | Ramos            | CA                  |
| Andrew     | Cencini   | Luciana       | Ramos            | CA                  |
| Andrew     | Cencini   | Luciana       | Ramos            | CA                  |
| Andrew     | Cencini   | Luciana       | Ramos            | CA                  |
| Andrew     | Cencini   | Luciana       | Ramos            | CA                  |
| Andrew     | Cencini   | Luciana       | Ramos            | CA                  |
| Mariya     | Sergienko | Michael       | Entin            | CA                  |
| Mariya     | Sergienko | Michael       | Entin            | CA                  |
| Mariya     | Sergienko | Michael       | Entin            | CA                  |
| Mariya     | Sergienko | Michael       | Entin            | CA                  |
| Mariya     | Sergienko | Michael       | Entin            | CA                  |
| Mariya     | Sergienko | Michael       | Entin            | CA                  |
| Mariya     | Sergienko | Michael       | Entin            | CA                  |
| Mariya     | Sergienko | Michael       | Entin            | CA                  |
| Mariya     | Sergienko | Michael       | Entin            | CA                  |
| Mariya     | Sergienko | Michael       | Entin            | CA                  |
| Andrew     | Cencini   | Michael       | Entin            | CA                  |
| Andrew     | Cencini   | Michael       | Entin            | CA                  |
| Andrew     | Cencini   | Michael       | Entin            | CA                  |
| Andrew     | Cencini   | Michael       | Entin            | CA                  |
| Andrew     | Cencini   | Michael       | Entin            | CA                  |
| Mariya     | Sergienko | Jonas         | Hasselberg       | CA                  |
| Mariya     | Sergienko | Jonas         | Hasselberg       | CA                  |
| Mariya     | Sergienko | Jonas         | Hasselberg       | CA                  |
| Mariya     | Sergienko | Jonas         | Hasselberg       | CA                  |
| Mariya     | Sergienko | Jonas         | Hasselberg       | CA                  |
| Mariya     | Sergienko | Jonas         | Hasselberg       | CA                  |
| Mariya     | Sergienko | Jonas         | Hasselberg       | CA                  |
| Mariya     | Sergienko | Jonas         | Hasselberg       | CA                  |
| Mariya     | Sergienko | Jonas         | Hasselberg       | CA                  |
| Mariya     | Sergienko | Jonas         | Hasselberg       | CA                  |
| Andrew     | Cencini   | Jonas         | Hasselberg       | CA                  |
| Andrew     | Cencini   | Jonas         | Hasselberg       | CA                  |
| Andrew     | Cencini   | Jonas         | Hasselberg       | CA                  |
| Andrew     | Cencini   | Jonas         | Hasselberg       | CA                  |
| Andrew     | Cencini   | Jonas         | Hasselberg       | CA                  |
| Mariya     | Sergienko | John          | Rodman           | CA                  |
| Mariya     | Sergienko | John          | Rodman           | CA                  |
| Mariya     | Sergienko | John          | Rodman           | CA                  |
| Mariya     | Sergienko | John          | Rodman           | CA                  |
| Mariya     | Sergienko | John          | Rodman           | CA                  |
| Mariya     | Sergienko | John          | Rodman           | CA                  |
| Mariya     | Sergienko | John          | Rodman           | CA                  |
| Mariya     | Sergienko | John          | Rodman           | CA                  |
| Mariya     | Sergienko | John          | Rodman           | CA                  |
| Mariya     | Sergienko | John          | Rodman           | CA                  |
| Andrew     | Cencini   | John          | Rodman           | CA                  |
| Andrew     | Cencini   | John          | Rodman           | CA                  |
| Andrew     | Cencini   | John          | Rodman           | CA                  |
| Andrew     | Cencini   | John          | Rodman           | CA                  |
| Andrew     | Cencini   | John          | Rodman           | CA                  |
| Mariya     | Sergienko | Run           | Liu              | CA                  |
| Mariya     | Sergienko | Run           | Liu              | CA                  |
| Mariya     | Sergienko | Run           | Liu              | CA                  |
| Mariya     | Sergienko | Run           | Liu              | CA                  |
| Mariya     | Sergienko | Run           | Liu              | CA                  |
| Mariya     | Sergienko | Run           | Liu              | CA                  |
| Mariya     | Sergienko | Run           | Liu              | CA                  |
| Mariya     | Sergienko | Run           | Liu              | CA                  |
| Mariya     | Sergienko | Run           | Liu              | CA                  |
| Mariya     | Sergienko | Run           | Liu              | CA                  |
| Andrew     | Cencini   | Run           | Liu              | CA                  |
| Andrew     | Cencini   | Run           | Liu              | CA                  |
| Andrew     | Cencini   | Run           | Liu              | CA                  |
| Andrew     | Cencini   | Run           | Liu              | CA                  |
| Andrew     | Cencini   | Run           | Liu              | CA                  |
| Mariya     | Sergienko | Karen         | Toh              | CA                  |
| Mariya     | Sergienko | Karen         | Toh              | CA                  |
| Mariya     | Sergienko | Karen         | Toh              | CA                  |
| Mariya     | Sergienko | Karen         | Toh              | CA                  |
| Mariya     | Sergienko | Karen         | Toh              | CA                  |
| Mariya     | Sergienko | Karen         | Toh              | CA                  |
| Mariya     | Sergienko | Karen         | Toh              | CA                  |
| Mariya     | Sergienko | Karen         | Toh              | CA                  |
| Mariya     | Sergienko | Karen         | Toh              | CA                  |
| Mariya     | Sergienko | Karen         | Toh              | CA                  |
| Andrew     | Cencini   | Karen         | Toh              | CA                  |
| Andrew     | Cencini   | Karen         | Toh              | CA                  |
| Andrew     | Cencini   | Karen         | Toh              | CA                  |
| Andrew     | Cencini   | Karen         | Toh              | CA                  |
| Andrew     | Cencini   | Karen         | Toh              | CA                  |
| Mariya     | Sergienko | Amritansh     | Raghav           | CA                  |
| Mariya     | Sergienko | Amritansh     | Raghav           | CA                  |
| Mariya     | Sergienko | Amritansh     | Raghav           | CA                  |
| Mariya     | Sergienko | Amritansh     | Raghav           | CA                  |
| Mariya     | Sergienko | Amritansh     | Raghav           | CA                  |
| Mariya     | Sergienko | Amritansh     | Raghav           | CA                  |
| Mariya     | Sergienko | Amritansh     | Raghav           | CA                  |
| Mariya     | Sergienko | Amritansh     | Raghav           | CA                  |
| Mariya     | Sergienko | Amritansh     | Raghav           | CA                  |
| Mariya     | Sergienko | Amritansh     | Raghav           | CA                  |
| Andrew     | Cencini   | Amritansh     | Raghav           | CA                  |
| Andrew     | Cencini   | Amritansh     | Raghav           | CA                  |
| Andrew     | Cencini   | Amritansh     | Raghav           | CA                  |
| Andrew     | Cencini   | Amritansh     | Raghav           | CA                  |
| Andrew     | Cencini   | Amritansh     | Raghav           | CA                  |
| Mariya     | Sergienko | Soo Jung      | Lee              | CA                  |
| Mariya     | Sergienko | Soo Jung      | Lee              | CA                  |
| Mariya     | Sergienko | Soo Jung      | Lee              | CA                  |
| Mariya     | Sergienko | Soo Jung      | Lee              | CA                  |
| Mariya     | Sergienko | Soo Jung      | Lee              | CA                  |
| Mariya     | Sergienko | Soo Jung      | Lee              | CA                  |
| Mariya     | Sergienko | Soo Jung      | Lee              | CA                  |
| Mariya     | Sergienko | Soo Jung      | Lee              | CA                  |
| Mariya     | Sergienko | Soo Jung      | Lee              | CA                  |
| Mariya     | Sergienko | Soo Jung      | Lee              | CA                  |
| Andrew     | Cencini   | Soo Jung      | Lee              | CA                  |
| Andrew     | Cencini   | Soo Jung      | Lee              | CA                  |
| Andrew     | Cencini   | Soo Jung      | Lee              | CA                  |
| Andrew     | Cencini   | Soo Jung      | Lee              | CA                  |
| Andrew     | Cencini   | Soo Jung      | Lee              | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Andrew     | Cencini   | Anna          | Bedecs           | CA                  |
| Andrew     | Cencini   | Anna          | Bedecs           | CA                  |
| Andrew     | Cencini   | Anna          | Bedecs           | CA                  |
| Andrew     | Cencini   | Anna          | Bedecs           | CA                  |
| Andrew     | Cencini   | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Andrew     | Cencini   | Antonio       | Gratacos Solsona | CA                  |
| Andrew     | Cencini   | Antonio       | Gratacos Solsona | CA                  |
| Andrew     | Cencini   | Antonio       | Gratacos Solsona | CA                  |
| Andrew     | Cencini   | Antonio       | Gratacos Solsona | CA                  |
| Andrew     | Cencini   | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Andrew     | Cencini   | Thomas        | Axen             | CA                  |
| Andrew     | Cencini   | Thomas        | Axen             | CA                  |
| Andrew     | Cencini   | Thomas        | Axen             | CA                  |
| Andrew     | Cencini   | Thomas        | Axen             | CA                  |
| Andrew     | Cencini   | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Andrew     | Cencini   | Christina     | Lee              | CA                  |
| Andrew     | Cencini   | Christina     | Lee              | CA                  |
| Andrew     | Cencini   | Christina     | Lee              | CA                  |
| Andrew     | Cencini   | Christina     | Lee              | CA                  |
| Andrew     | Cencini   | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Martin        | O'Donnell        | CA                  |
| Mariya     | Sergienko | Martin        | O'Donnell        | CA                  |
| Mariya     | Sergienko | Martin        | O'Donnell        | CA                  |
| Mariya     | Sergienko | Martin        | O'Donnell        | CA                  |
| Mariya     | Sergienko | Martin        | O'Donnell        | CA                  |
| Mariya     | Sergienko | Martin        | O'Donnell        | CA                  |
| Mariya     | Sergienko | Martin        | O'Donnell        | CA                  |
| Mariya     | Sergienko | Martin        | O'Donnell        | CA                  |
| Mariya     | Sergienko | Martin        | O'Donnell        | CA                  |
| Mariya     | Sergienko | Martin        | O'Donnell        | CA                  |
| Andrew     | Cencini   | Martin        | O'Donnell        | CA                  |
| Andrew     | Cencini   | Martin        | O'Donnell        | CA                  |
| Andrew     | Cencini   | Martin        | O'Donnell        | CA                  |
| Andrew     | Cencini   | Martin        | O'Donnell        | CA                  |
| Andrew     | Cencini   | Martin        | O'Donnell        | CA                  |
| Mariya     | Sergienko | Francisco     | Perez-Olaeta     | CA                  |
| Mariya     | Sergienko | Francisco     | Perez-Olaeta     | CA                  |
| Mariya     | Sergienko | Francisco     | Perez-Olaeta     | CA                  |
| Mariya     | Sergienko | Francisco     | Perez-Olaeta     | CA                  |
| Mariya     | Sergienko | Francisco     | Perez-Olaeta     | CA                  |
| Mariya     | Sergienko | Francisco     | Perez-Olaeta     | CA                  |
| Mariya     | Sergienko | Francisco     | Perez-Olaeta     | CA                  |
| Mariya     | Sergienko | Francisco     | Perez-Olaeta     | CA                  |
| Mariya     | Sergienko | Francisco     | Perez-Olaeta     | CA                  |
| Mariya     | Sergienko | Francisco     | Perez-Olaeta     | CA                  |
| Andrew     | Cencini   | Francisco     | Perez-Olaeta     | CA                  |
| Andrew     | Cencini   | Francisco     | Perez-Olaeta     | CA                  |
| Andrew     | Cencini   | Francisco     | Perez-Olaeta     | CA                  |
| Andrew     | Cencini   | Francisco     | Perez-Olaeta     | CA                  |
| Andrew     | Cencini   | Francisco     | Perez-Olaeta     | CA                  |
| Mariya     | Sergienko | Ming-Yang     | Xie              | CA                  |
| Mariya     | Sergienko | Ming-Yang     | Xie              | CA                  |
| Mariya     | Sergienko | Ming-Yang     | Xie              | CA                  |
| Mariya     | Sergienko | Ming-Yang     | Xie              | CA                  |
| Mariya     | Sergienko | Ming-Yang     | Xie              | CA                  |
| Mariya     | Sergienko | Ming-Yang     | Xie              | CA                  |
| Mariya     | Sergienko | Ming-Yang     | Xie              | CA                  |
| Mariya     | Sergienko | Ming-Yang     | Xie              | CA                  |
| Mariya     | Sergienko | Ming-Yang     | Xie              | CA                  |
| Mariya     | Sergienko | Ming-Yang     | Xie              | CA                  |
| Andrew     | Cencini   | Ming-Yang     | Xie              | CA                  |
| Andrew     | Cencini   | Ming-Yang     | Xie              | CA                  |
| Andrew     | Cencini   | Ming-Yang     | Xie              | CA                  |
| Andrew     | Cencini   | Ming-Yang     | Xie              | CA                  |
| Andrew     | Cencini   | Ming-Yang     | Xie              | CA                  |
| Mariya     | Sergienko | Elizabeth     | Andersen         | CA                  |
| Mariya     | Sergienko | Elizabeth     | Andersen         | CA                  |
| Mariya     | Sergienko | Elizabeth     | Andersen         | CA                  |
| Mariya     | Sergienko | Elizabeth     | Andersen         | CA                  |
| Mariya     | Sergienko | Elizabeth     | Andersen         | CA                  |
| Mariya     | Sergienko | Elizabeth     | Andersen         | CA                  |
| Mariya     | Sergienko | Elizabeth     | Andersen         | CA                  |
| Mariya     | Sergienko | Elizabeth     | Andersen         | CA                  |
| Mariya     | Sergienko | Elizabeth     | Andersen         | CA                  |
| Mariya     | Sergienko | Elizabeth     | Andersen         | CA                  |
| Andrew     | Cencini   | Elizabeth     | Andersen         | CA                  |
| Andrew     | Cencini   | Elizabeth     | Andersen         | CA                  |
| Andrew     | Cencini   | Elizabeth     | Andersen         | CA                  |
| Andrew     | Cencini   | Elizabeth     | Andersen         | CA                  |
| Andrew     | Cencini   | Elizabeth     | Andersen         | CA                  |
| Mariya     | Sergienko | Sven          | Mortensen        | CA                  |
| Mariya     | Sergienko | Sven          | Mortensen        | CA                  |
| Mariya     | Sergienko | Sven          | Mortensen        | CA                  |
| Mariya     | Sergienko | Sven          | Mortensen        | CA                  |
| Mariya     | Sergienko | Sven          | Mortensen        | CA                  |
| Mariya     | Sergienko | Sven          | Mortensen        | CA                  |
| Mariya     | Sergienko | Sven          | Mortensen        | CA                  |
| Mariya     | Sergienko | Sven          | Mortensen        | CA                  |
| Mariya     | Sergienko | Sven          | Mortensen        | CA                  |
| Mariya     | Sergienko | Sven          | Mortensen        | CA                  |
| Andrew     | Cencini   | Sven          | Mortensen        | CA                  |
| Andrew     | Cencini   | Sven          | Mortensen        | CA                  |
| Andrew     | Cencini   | Sven          | Mortensen        | CA                  |
| Andrew     | Cencini   | Sven          | Mortensen        | CA                  |
| Andrew     | Cencini   | Sven          | Mortensen        | CA                  |
| Mariya     | Sergienko | Roland        | Wacker           | CA                  |
| Mariya     | Sergienko | Roland        | Wacker           | CA                  |
| Mariya     | Sergienko | Roland        | Wacker           | CA                  |
| Mariya     | Sergienko | Roland        | Wacker           | CA                  |
| Mariya     | Sergienko | Roland        | Wacker           | CA                  |
| Mariya     | Sergienko | Roland        | Wacker           | CA                  |
| Mariya     | Sergienko | Roland        | Wacker           | CA                  |
| Mariya     | Sergienko | Roland        | Wacker           | CA                  |
| Mariya     | Sergienko | Roland        | Wacker           | CA                  |
| Mariya     | Sergienko | Roland        | Wacker           | CA                  |
| Andrew     | Cencini   | Roland        | Wacker           | CA                  |
| Andrew     | Cencini   | Roland        | Wacker           | CA                  |
| Andrew     | Cencini   | Roland        | Wacker           | CA                  |
| Andrew     | Cencini   | Roland        | Wacker           | CA                  |
| Andrew     | Cencini   | Roland        | Wacker           | CA                  |
| Mariya     | Sergienko | Peter         | Krschne          | CA                  |
| Mariya     | Sergienko | Peter         | Krschne          | CA                  |
| Mariya     | Sergienko | Peter         | Krschne          | CA                  |
| Mariya     | Sergienko | Peter         | Krschne          | CA                  |
| Mariya     | Sergienko | Peter         | Krschne          | CA                  |
| Mariya     | Sergienko | Peter         | Krschne          | CA                  |
| Mariya     | Sergienko | Peter         | Krschne          | CA                  |
| Mariya     | Sergienko | Peter         | Krschne          | CA                  |
| Mariya     | Sergienko | Peter         | Krschne          | CA                  |
| Mariya     | Sergienko | Peter         | Krschne          | CA                  |
| Andrew     | Cencini   | Peter         | Krschne          | CA                  |
| Andrew     | Cencini   | Peter         | Krschne          | CA                  |
| Andrew     | Cencini   | Peter         | Krschne          | CA                  |
| Andrew     | Cencini   | Peter         | Krschne          | CA                  |
| Andrew     | Cencini   | Peter         | Krschne          | CA                  |
| Mariya     | Sergienko | John          | Edwards          | CA                  |
| Mariya     | Sergienko | John          | Edwards          | CA                  |
| Mariya     | Sergienko | John          | Edwards          | CA                  |
| Mariya     | Sergienko | John          | Edwards          | CA                  |
| Mariya     | Sergienko | John          | Edwards          | CA                  |
| Mariya     | Sergienko | John          | Edwards          | CA                  |
| Mariya     | Sergienko | John          | Edwards          | CA                  |
| Mariya     | Sergienko | John          | Edwards          | CA                  |
| Mariya     | Sergienko | John          | Edwards          | CA                  |
| Mariya     | Sergienko | John          | Edwards          | CA                  |
| Andrew     | Cencini   | John          | Edwards          | CA                  |
| Andrew     | Cencini   | John          | Edwards          | CA                  |
| Andrew     | Cencini   | John          | Edwards          | CA                  |
| Andrew     | Cencini   | John          | Edwards          | CA                  |
| Andrew     | Cencini   | John          | Edwards          | CA                  |
| Mariya     | Sergienko | Andre         | Ludick           | CA                  |
| Mariya     | Sergienko | Andre         | Ludick           | CA                  |
| Mariya     | Sergienko | Andre         | Ludick           | CA                  |
| Mariya     | Sergienko | Andre         | Ludick           | CA                  |
| Mariya     | Sergienko | Andre         | Ludick           | CA                  |
| Mariya     | Sergienko | Andre         | Ludick           | CA                  |
| Mariya     | Sergienko | Andre         | Ludick           | CA                  |
| Mariya     | Sergienko | Andre         | Ludick           | CA                  |
| Mariya     | Sergienko | Andre         | Ludick           | CA                  |
| Mariya     | Sergienko | Andre         | Ludick           | CA                  |
| Andrew     | Cencini   | Andre         | Ludick           | CA                  |
| Andrew     | Cencini   | Andre         | Ludick           | CA                  |
| Andrew     | Cencini   | Andre         | Ludick           | CA                  |
| Andrew     | Cencini   | Andre         | Ludick           | CA                  |
| Andrew     | Cencini   | Andre         | Ludick           | CA                  |
| Mariya     | Sergienko | Carlos        | Grilo            | CA                  |
| Mariya     | Sergienko | Carlos        | Grilo            | CA                  |
| Mariya     | Sergienko | Carlos        | Grilo            | CA                  |
| Mariya     | Sergienko | Carlos        | Grilo            | CA                  |
| Mariya     | Sergienko | Carlos        | Grilo            | CA                  |
| Mariya     | Sergienko | Carlos        | Grilo            | CA                  |
| Mariya     | Sergienko | Carlos        | Grilo            | CA                  |
| Mariya     | Sergienko | Carlos        | Grilo            | CA                  |
| Mariya     | Sergienko | Carlos        | Grilo            | CA                  |
| Mariya     | Sergienko | Carlos        | Grilo            | CA                  |
| Andrew     | Cencini   | Carlos        | Grilo            | CA                  |
| Andrew     | Cencini   | Carlos        | Grilo            | CA                  |
| Andrew     | Cencini   | Carlos        | Grilo            | CA                  |
| Andrew     | Cencini   | Carlos        | Grilo            | CA                  |
| Andrew     | Cencini   | Carlos        | Grilo            | CA                  |
| Mariya     | Sergienko | Helena        | Kupkova          | CA                  |
| Mariya     | Sergienko | Helena        | Kupkova          | CA                  |
| Mariya     | Sergienko | Helena        | Kupkova          | CA                  |
| Mariya     | Sergienko | Helena        | Kupkova          | CA                  |
| Mariya     | Sergienko | Helena        | Kupkova          | CA                  |
| Mariya     | Sergienko | Helena        | Kupkova          | CA                  |
| Mariya     | Sergienko | Helena        | Kupkova          | CA                  |
| Mariya     | Sergienko | Helena        | Kupkova          | CA                  |
| Mariya     | Sergienko | Helena        | Kupkova          | CA                  |
| Mariya     | Sergienko | Helena        | Kupkova          | CA                  |
| Andrew     | Cencini   | Helena        | Kupkova          | CA                  |
| Andrew     | Cencini   | Helena        | Kupkova          | CA                  |
| Andrew     | Cencini   | Helena        | Kupkova          | CA                  |
| Andrew     | Cencini   | Helena        | Kupkova          | CA                  |
| Andrew     | Cencini   | Helena        | Kupkova          | CA                  |
| Mariya     | Sergienko | Daniel        | Goldschmidt      | CA                  |
| Mariya     | Sergienko | Daniel        | Goldschmidt      | CA                  |
| Mariya     | Sergienko | Daniel        | Goldschmidt      | CA                  |
| Mariya     | Sergienko | Daniel        | Goldschmidt      | CA                  |
| Mariya     | Sergienko | Daniel        | Goldschmidt      | CA                  |
| Mariya     | Sergienko | Daniel        | Goldschmidt      | CA                  |
| Mariya     | Sergienko | Daniel        | Goldschmidt      | CA                  |
| Mariya     | Sergienko | Daniel        | Goldschmidt      | CA                  |
| Mariya     | Sergienko | Daniel        | Goldschmidt      | CA                  |
| Mariya     | Sergienko | Daniel        | Goldschmidt      | CA                  |
| Andrew     | Cencini   | Daniel        | Goldschmidt      | CA                  |
| Andrew     | Cencini   | Daniel        | Goldschmidt      | CA                  |
| Andrew     | Cencini   | Daniel        | Goldschmidt      | CA                  |
| Andrew     | Cencini   | Daniel        | Goldschmidt      | CA                  |
| Andrew     | Cencini   | Daniel        | Goldschmidt      | CA                  |
| Mariya     | Sergienko | Jean Philippe | Bagel            | CA                  |
| Mariya     | Sergienko | Jean Philippe | Bagel            | CA                  |
| Mariya     | Sergienko | Jean Philippe | Bagel            | CA                  |
| Mariya     | Sergienko | Jean Philippe | Bagel            | CA                  |
| Mariya     | Sergienko | Jean Philippe | Bagel            | CA                  |
| Mariya     | Sergienko | Jean Philippe | Bagel            | CA                  |
| Mariya     | Sergienko | Jean Philippe | Bagel            | CA                  |
| Mariya     | Sergienko | Jean Philippe | Bagel            | CA                  |
| Mariya     | Sergienko | Jean Philippe | Bagel            | CA                  |
| Mariya     | Sergienko | Jean Philippe | Bagel            | CA                  |
| Andrew     | Cencini   | Jean Philippe | Bagel            | CA                  |
| Andrew     | Cencini   | Jean Philippe | Bagel            | CA                  |
| Andrew     | Cencini   | Jean Philippe | Bagel            | CA                  |
| Andrew     | Cencini   | Jean Philippe | Bagel            | CA                  |
| Andrew     | Cencini   | Jean Philippe | Bagel            | CA                  |
| Mariya     | Sergienko | Catherine     | Autier Miconi    | CA                  |
| Mariya     | Sergienko | Catherine     | Autier Miconi    | CA                  |
| Mariya     | Sergienko | Catherine     | Autier Miconi    | CA                  |
| Mariya     | Sergienko | Catherine     | Autier Miconi    | CA                  |
| Mariya     | Sergienko | Catherine     | Autier Miconi    | CA                  |
| Mariya     | Sergienko | Catherine     | Autier Miconi    | CA                  |
| Mariya     | Sergienko | Catherine     | Autier Miconi    | CA                  |
| Mariya     | Sergienko | Catherine     | Autier Miconi    | CA                  |
| Mariya     | Sergienko | Catherine     | Autier Miconi    | CA                  |
| Mariya     | Sergienko | Catherine     | Autier Miconi    | CA                  |
| Andrew     | Cencini   | Catherine     | Autier Miconi    | CA                  |
| Andrew     | Cencini   | Catherine     | Autier Miconi    | CA                  |
| Andrew     | Cencini   | Catherine     | Autier Miconi    | CA                  |
| Andrew     | Cencini   | Catherine     | Autier Miconi    | CA                  |
| Andrew     | Cencini   | Catherine     | Autier Miconi    | CA                  |
| Mariya     | Sergienko | Alexander     | Eggerer          | CA                  |
| Mariya     | Sergienko | Alexander     | Eggerer          | CA                  |
| Mariya     | Sergienko | Alexander     | Eggerer          | CA                  |
| Mariya     | Sergienko | Alexander     | Eggerer          | CA                  |
| Mariya     | Sergienko | Alexander     | Eggerer          | CA                  |
| Mariya     | Sergienko | Alexander     | Eggerer          | CA                  |
| Mariya     | Sergienko | Alexander     | Eggerer          | CA                  |
| Mariya     | Sergienko | Alexander     | Eggerer          | CA                  |
| Mariya     | Sergienko | Alexander     | Eggerer          | CA                  |
| Mariya     | Sergienko | Alexander     | Eggerer          | CA                  |
| Andrew     | Cencini   | Alexander     | Eggerer          | CA                  |
| Andrew     | Cencini   | Alexander     | Eggerer          | CA                  |
| Andrew     | Cencini   | Alexander     | Eggerer          | CA                  |
| Andrew     | Cencini   | Alexander     | Eggerer          | CA                  |
| Andrew     | Cencini   | Alexander     | Eggerer          | CA                  |
| Mariya     | Sergienko | George        | Li               | CA                  |
| Mariya     | Sergienko | George        | Li               | CA                  |
| Mariya     | Sergienko | George        | Li               | CA                  |
| Mariya     | Sergienko | George        | Li               | CA                  |
| Mariya     | Sergienko | George        | Li               | CA                  |
| Mariya     | Sergienko | George        | Li               | CA                  |
| Mariya     | Sergienko | George        | Li               | CA                  |
| Mariya     | Sergienko | George        | Li               | CA                  |
| Mariya     | Sergienko | George        | Li               | CA                  |
| Mariya     | Sergienko | George        | Li               | CA                  |
| Andrew     | Cencini   | George        | Li               | CA                  |
| Andrew     | Cencini   | George        | Li               | CA                  |
| Andrew     | Cencini   | George        | Li               | CA                  |
| Andrew     | Cencini   | George        | Li               | CA                  |
| Andrew     | Cencini   | George        | Li               | CA                  |
| Mariya     | Sergienko | Bernard       | Tham             | CA                  |
| Mariya     | Sergienko | Bernard       | Tham             | CA                  |
| Mariya     | Sergienko | Bernard       | Tham             | CA                  |
| Mariya     | Sergienko | Bernard       | Tham             | CA                  |
| Mariya     | Sergienko | Bernard       | Tham             | CA                  |
| Mariya     | Sergienko | Bernard       | Tham             | CA                  |
| Mariya     | Sergienko | Bernard       | Tham             | CA                  |
| Mariya     | Sergienko | Bernard       | Tham             | CA                  |
| Mariya     | Sergienko | Bernard       | Tham             | CA                  |
| Mariya     | Sergienko | Bernard       | Tham             | CA                  |
| Andrew     | Cencini   | Bernard       | Tham             | CA                  |
| Andrew     | Cencini   | Bernard       | Tham             | CA                  |
| Andrew     | Cencini   | Bernard       | Tham             | CA                  |
| Andrew     | Cencini   | Bernard       | Tham             | CA                  |
| Andrew     | Cencini   | Bernard       | Tham             | CA                  |
| Mariya     | Sergienko | Luciana       | Ramos            | CA                  |
| Mariya     | Sergienko | Luciana       | Ramos            | CA                  |
| Mariya     | Sergienko | Luciana       | Ramos            | CA                  |
| Mariya     | Sergienko | Luciana       | Ramos            | CA                  |
| Mariya     | Sergienko | Luciana       | Ramos            | CA                  |
| Mariya     | Sergienko | Luciana       | Ramos            | CA                  |
| Mariya     | Sergienko | Luciana       | Ramos            | CA                  |
| Mariya     | Sergienko | Luciana       | Ramos            | CA                  |
| Mariya     | Sergienko | Luciana       | Ramos            | CA                  |
| Mariya     | Sergienko | Luciana       | Ramos            | CA                  |
| Andrew     | Cencini   | Luciana       | Ramos            | CA                  |
| Andrew     | Cencini   | Luciana       | Ramos            | CA                  |
| Andrew     | Cencini   | Luciana       | Ramos            | CA                  |
| Andrew     | Cencini   | Luciana       | Ramos            | CA                  |
| Andrew     | Cencini   | Luciana       | Ramos            | CA                  |
| Mariya     | Sergienko | Michael       | Entin            | CA                  |
| Mariya     | Sergienko | Michael       | Entin            | CA                  |
| Mariya     | Sergienko | Michael       | Entin            | CA                  |
| Mariya     | Sergienko | Michael       | Entin            | CA                  |
| Mariya     | Sergienko | Michael       | Entin            | CA                  |
| Mariya     | Sergienko | Michael       | Entin            | CA                  |
| Mariya     | Sergienko | Michael       | Entin            | CA                  |
| Mariya     | Sergienko | Michael       | Entin            | CA                  |
| Mariya     | Sergienko | Michael       | Entin            | CA                  |
| Mariya     | Sergienko | Michael       | Entin            | CA                  |
| Andrew     | Cencini   | Michael       | Entin            | CA                  |
| Andrew     | Cencini   | Michael       | Entin            | CA                  |
| Andrew     | Cencini   | Michael       | Entin            | CA                  |
| Andrew     | Cencini   | Michael       | Entin            | CA                  |
| Andrew     | Cencini   | Michael       | Entin            | CA                  |
| Mariya     | Sergienko | Jonas         | Hasselberg       | CA                  |
| Mariya     | Sergienko | Jonas         | Hasselberg       | CA                  |
| Mariya     | Sergienko | Jonas         | Hasselberg       | CA                  |
| Mariya     | Sergienko | Jonas         | Hasselberg       | CA                  |
| Mariya     | Sergienko | Jonas         | Hasselberg       | CA                  |
| Mariya     | Sergienko | Jonas         | Hasselberg       | CA                  |
| Mariya     | Sergienko | Jonas         | Hasselberg       | CA                  |
| Mariya     | Sergienko | Jonas         | Hasselberg       | CA                  |
| Mariya     | Sergienko | Jonas         | Hasselberg       | CA                  |
| Mariya     | Sergienko | Jonas         | Hasselberg       | CA                  |
| Andrew     | Cencini   | Jonas         | Hasselberg       | CA                  |
| Andrew     | Cencini   | Jonas         | Hasselberg       | CA                  |
| Andrew     | Cencini   | Jonas         | Hasselberg       | CA                  |
| Andrew     | Cencini   | Jonas         | Hasselberg       | CA                  |
| Andrew     | Cencini   | Jonas         | Hasselberg       | CA                  |
| Mariya     | Sergienko | John          | Rodman           | CA                  |
| Mariya     | Sergienko | John          | Rodman           | CA                  |
| Mariya     | Sergienko | John          | Rodman           | CA                  |
| Mariya     | Sergienko | John          | Rodman           | CA                  |
| Mariya     | Sergienko | John          | Rodman           | CA                  |
| Mariya     | Sergienko | John          | Rodman           | CA                  |
| Mariya     | Sergienko | John          | Rodman           | CA                  |
| Mariya     | Sergienko | John          | Rodman           | CA                  |
| Mariya     | Sergienko | John          | Rodman           | CA                  |
| Mariya     | Sergienko | John          | Rodman           | CA                  |
| Andrew     | Cencini   | John          | Rodman           | CA                  |
| Andrew     | Cencini   | John          | Rodman           | CA                  |
| Andrew     | Cencini   | John          | Rodman           | CA                  |
| Andrew     | Cencini   | John          | Rodman           | CA                  |
| Andrew     | Cencini   | John          | Rodman           | CA                  |
| Mariya     | Sergienko | Run           | Liu              | CA                  |
| Mariya     | Sergienko | Run           | Liu              | CA                  |
| Mariya     | Sergienko | Run           | Liu              | CA                  |
| Mariya     | Sergienko | Run           | Liu              | CA                  |
| Mariya     | Sergienko | Run           | Liu              | CA                  |
| Mariya     | Sergienko | Run           | Liu              | CA                  |
| Mariya     | Sergienko | Run           | Liu              | CA                  |
| Mariya     | Sergienko | Run           | Liu              | CA                  |
| Mariya     | Sergienko | Run           | Liu              | CA                  |
| Mariya     | Sergienko | Run           | Liu              | CA                  |
| Andrew     | Cencini   | Run           | Liu              | CA                  |
| Andrew     | Cencini   | Run           | Liu              | CA                  |
| Andrew     | Cencini   | Run           | Liu              | CA                  |
| Andrew     | Cencini   | Run           | Liu              | CA                  |
| Andrew     | Cencini   | Run           | Liu              | CA                  |
| Mariya     | Sergienko | Karen         | Toh              | CA                  |
| Mariya     | Sergienko | Karen         | Toh              | CA                  |
| Mariya     | Sergienko | Karen         | Toh              | CA                  |
| Mariya     | Sergienko | Karen         | Toh              | CA                  |
| Mariya     | Sergienko | Karen         | Toh              | CA                  |
| Mariya     | Sergienko | Karen         | Toh              | CA                  |
| Mariya     | Sergienko | Karen         | Toh              | CA                  |
| Mariya     | Sergienko | Karen         | Toh              | CA                  |
| Mariya     | Sergienko | Karen         | Toh              | CA                  |
| Mariya     | Sergienko | Karen         | Toh              | CA                  |
| Andrew     | Cencini   | Karen         | Toh              | CA                  |
| Andrew     | Cencini   | Karen         | Toh              | CA                  |
| Andrew     | Cencini   | Karen         | Toh              | CA                  |
| Andrew     | Cencini   | Karen         | Toh              | CA                  |
| Andrew     | Cencini   | Karen         | Toh              | CA                  |
| Mariya     | Sergienko | Amritansh     | Raghav           | CA                  |
| Mariya     | Sergienko | Amritansh     | Raghav           | CA                  |
| Mariya     | Sergienko | Amritansh     | Raghav           | CA                  |
| Mariya     | Sergienko | Amritansh     | Raghav           | CA                  |
| Mariya     | Sergienko | Amritansh     | Raghav           | CA                  |
| Mariya     | Sergienko | Amritansh     | Raghav           | CA                  |
| Mariya     | Sergienko | Amritansh     | Raghav           | CA                  |
| Mariya     | Sergienko | Amritansh     | Raghav           | CA                  |
| Mariya     | Sergienko | Amritansh     | Raghav           | CA                  |
| Mariya     | Sergienko | Amritansh     | Raghav           | CA                  |
| Andrew     | Cencini   | Amritansh     | Raghav           | CA                  |
| Andrew     | Cencini   | Amritansh     | Raghav           | CA                  |
| Andrew     | Cencini   | Amritansh     | Raghav           | CA                  |
| Andrew     | Cencini   | Amritansh     | Raghav           | CA                  |
| Andrew     | Cencini   | Amritansh     | Raghav           | CA                  |
| Mariya     | Sergienko | Soo Jung      | Lee              | CA                  |
| Mariya     | Sergienko | Soo Jung      | Lee              | CA                  |
| Mariya     | Sergienko | Soo Jung      | Lee              | CA                  |
| Mariya     | Sergienko | Soo Jung      | Lee              | CA                  |
| Mariya     | Sergienko | Soo Jung      | Lee              | CA                  |
| Mariya     | Sergienko | Soo Jung      | Lee              | CA                  |
| Mariya     | Sergienko | Soo Jung      | Lee              | CA                  |
| Mariya     | Sergienko | Soo Jung      | Lee              | CA                  |
| Mariya     | Sergienko | Soo Jung      | Lee              | CA                  |
| Mariya     | Sergienko | Soo Jung      | Lee              | CA                  |
| Andrew     | Cencini   | Soo Jung      | Lee              | CA                  |
| Andrew     | Cencini   | Soo Jung      | Lee              | CA                  |
| Andrew     | Cencini   | Soo Jung      | Lee              | CA                  |
| Andrew     | Cencini   | Soo Jung      | Lee              | CA                  |
| Andrew     | Cencini   | Soo Jung      | Lee              | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Andrew     | Cencini   | Anna          | Bedecs           | CA                  |
| Andrew     | Cencini   | Anna          | Bedecs           | CA                  |
| Andrew     | Cencini   | Anna          | Bedecs           | CA                  |
| Andrew     | Cencini   | Anna          | Bedecs           | CA                  |
| Andrew     | Cencini   | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Andrew     | Cencini   | Antonio       | Gratacos Solsona | CA                  |
| Andrew     | Cencini   | Antonio       | Gratacos Solsona | CA                  |
| Andrew     | Cencini   | Antonio       | Gratacos Solsona | CA                  |
| Andrew     | Cencini   | Antonio       | Gratacos Solsona | CA                  |
| Andrew     | Cencini   | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Andrew     | Cencini   | Thomas        | Axen             | CA                  |
| Andrew     | Cencini   | Thomas        | Axen             | CA                  |
| Andrew     | Cencini   | Thomas        | Axen             | CA                  |
| Andrew     | Cencini   | Thomas        | Axen             | CA                  |
| Andrew     | Cencini   | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Andrew     | Cencini   | Christina     | Lee              | CA                  |
| Andrew     | Cencini   | Christina     | Lee              | CA                  |
| Andrew     | Cencini   | Christina     | Lee              | CA                  |
| Andrew     | Cencini   | Christina     | Lee              | CA                  |
| Andrew     | Cencini   | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Martin        | O'Donnell        | CA                  |
| Mariya     | Sergienko | Martin        | O'Donnell        | CA                  |
| Mariya     | Sergienko | Martin        | O'Donnell        | CA                  |
| Mariya     | Sergienko | Martin        | O'Donnell        | CA                  |
| Mariya     | Sergienko | Martin        | O'Donnell        | CA                  |
| Mariya     | Sergienko | Martin        | O'Donnell        | CA                  |
| Mariya     | Sergienko | Martin        | O'Donnell        | CA                  |
| Mariya     | Sergienko | Martin        | O'Donnell        | CA                  |
| Mariya     | Sergienko | Martin        | O'Donnell        | CA                  |
| Mariya     | Sergienko | Martin        | O'Donnell        | CA                  |
| Andrew     | Cencini   | Martin        | O'Donnell        | CA                  |
| Andrew     | Cencini   | Martin        | O'Donnell        | CA                  |
| Andrew     | Cencini   | Martin        | O'Donnell        | CA                  |
| Andrew     | Cencini   | Martin        | O'Donnell        | CA                  |
| Andrew     | Cencini   | Martin        | O'Donnell        | CA                  |
| Mariya     | Sergienko | Francisco     | Perez-Olaeta     | CA                  |
| Mariya     | Sergienko | Francisco     | Perez-Olaeta     | CA                  |
| Mariya     | Sergienko | Francisco     | Perez-Olaeta     | CA                  |
| Mariya     | Sergienko | Francisco     | Perez-Olaeta     | CA                  |
| Mariya     | Sergienko | Francisco     | Perez-Olaeta     | CA                  |
| Mariya     | Sergienko | Francisco     | Perez-Olaeta     | CA                  |
| Mariya     | Sergienko | Francisco     | Perez-Olaeta     | CA                  |
| Mariya     | Sergienko | Francisco     | Perez-Olaeta     | CA                  |
| Mariya     | Sergienko | Francisco     | Perez-Olaeta     | CA                  |
| Mariya     | Sergienko | Francisco     | Perez-Olaeta     | CA                  |
| Andrew     | Cencini   | Francisco     | Perez-Olaeta     | CA                  |
| Andrew     | Cencini   | Francisco     | Perez-Olaeta     | CA                  |
| Andrew     | Cencini   | Francisco     | Perez-Olaeta     | CA                  |
| Andrew     | Cencini   | Francisco     | Perez-Olaeta     | CA                  |
| Andrew     | Cencini   | Francisco     | Perez-Olaeta     | CA                  |
| Mariya     | Sergienko | Ming-Yang     | Xie              | CA                  |
| Mariya     | Sergienko | Ming-Yang     | Xie              | CA                  |
| Mariya     | Sergienko | Ming-Yang     | Xie              | CA                  |
| Mariya     | Sergienko | Ming-Yang     | Xie              | CA                  |
| Mariya     | Sergienko | Ming-Yang     | Xie              | CA                  |
| Mariya     | Sergienko | Ming-Yang     | Xie              | CA                  |
| Mariya     | Sergienko | Ming-Yang     | Xie              | CA                  |
| Mariya     | Sergienko | Ming-Yang     | Xie              | CA                  |
| Mariya     | Sergienko | Ming-Yang     | Xie              | CA                  |
| Mariya     | Sergienko | Ming-Yang     | Xie              | CA                  |
| Andrew     | Cencini   | Ming-Yang     | Xie              | CA                  |
| Andrew     | Cencini   | Ming-Yang     | Xie              | CA                  |
| Andrew     | Cencini   | Ming-Yang     | Xie              | CA                  |
| Andrew     | Cencini   | Ming-Yang     | Xie              | CA                  |
| Andrew     | Cencini   | Ming-Yang     | Xie              | CA                  |
| Mariya     | Sergienko | Elizabeth     | Andersen         | CA                  |
| Mariya     | Sergienko | Elizabeth     | Andersen         | CA                  |
| Mariya     | Sergienko | Elizabeth     | Andersen         | CA                  |
| Mariya     | Sergienko | Elizabeth     | Andersen         | CA                  |
| Mariya     | Sergienko | Elizabeth     | Andersen         | CA                  |
| Mariya     | Sergienko | Elizabeth     | Andersen         | CA                  |
| Mariya     | Sergienko | Elizabeth     | Andersen         | CA                  |
| Mariya     | Sergienko | Elizabeth     | Andersen         | CA                  |
| Mariya     | Sergienko | Elizabeth     | Andersen         | CA                  |
| Mariya     | Sergienko | Elizabeth     | Andersen         | CA                  |
| Andrew     | Cencini   | Elizabeth     | Andersen         | CA                  |
| Andrew     | Cencini   | Elizabeth     | Andersen         | CA                  |
| Andrew     | Cencini   | Elizabeth     | Andersen         | CA                  |
| Andrew     | Cencini   | Elizabeth     | Andersen         | CA                  |
| Andrew     | Cencini   | Elizabeth     | Andersen         | CA                  |
| Mariya     | Sergienko | Sven          | Mortensen        | CA                  |
| Mariya     | Sergienko | Sven          | Mortensen        | CA                  |
| Mariya     | Sergienko | Sven          | Mortensen        | CA                  |
| Mariya     | Sergienko | Sven          | Mortensen        | CA                  |
| Mariya     | Sergienko | Sven          | Mortensen        | CA                  |
| Mariya     | Sergienko | Sven          | Mortensen        | CA                  |
| Mariya     | Sergienko | Sven          | Mortensen        | CA                  |
| Mariya     | Sergienko | Sven          | Mortensen        | CA                  |
| Mariya     | Sergienko | Sven          | Mortensen        | CA                  |
| Mariya     | Sergienko | Sven          | Mortensen        | CA                  |
| Andrew     | Cencini   | Sven          | Mortensen        | CA                  |
| Andrew     | Cencini   | Sven          | Mortensen        | CA                  |
| Andrew     | Cencini   | Sven          | Mortensen        | CA                  |
| Andrew     | Cencini   | Sven          | Mortensen        | CA                  |
| Andrew     | Cencini   | Sven          | Mortensen        | CA                  |
| Mariya     | Sergienko | Roland        | Wacker           | CA                  |
| Mariya     | Sergienko | Roland        | Wacker           | CA                  |
| Mariya     | Sergienko | Roland        | Wacker           | CA                  |
| Mariya     | Sergienko | Roland        | Wacker           | CA                  |
| Mariya     | Sergienko | Roland        | Wacker           | CA                  |
| Mariya     | Sergienko | Roland        | Wacker           | CA                  |
| Mariya     | Sergienko | Roland        | Wacker           | CA                  |
| Mariya     | Sergienko | Roland        | Wacker           | CA                  |
| Mariya     | Sergienko | Roland        | Wacker           | CA                  |
| Mariya     | Sergienko | Roland        | Wacker           | CA                  |
| Andrew     | Cencini   | Roland        | Wacker           | CA                  |
| Andrew     | Cencini   | Roland        | Wacker           | CA                  |
| Andrew     | Cencini   | Roland        | Wacker           | CA                  |
| Andrew     | Cencini   | Roland        | Wacker           | CA                  |
| Andrew     | Cencini   | Roland        | Wacker           | CA                  |
| Mariya     | Sergienko | Peter         | Krschne          | CA                  |
| Mariya     | Sergienko | Peter         | Krschne          | CA                  |
| Mariya     | Sergienko | Peter         | Krschne          | CA                  |
| Mariya     | Sergienko | Peter         | Krschne          | CA                  |
| Mariya     | Sergienko | Peter         | Krschne          | CA                  |
| Mariya     | Sergienko | Peter         | Krschne          | CA                  |
| Mariya     | Sergienko | Peter         | Krschne          | CA                  |
| Mariya     | Sergienko | Peter         | Krschne          | CA                  |
| Mariya     | Sergienko | Peter         | Krschne          | CA                  |
| Mariya     | Sergienko | Peter         | Krschne          | CA                  |
| Andrew     | Cencini   | Peter         | Krschne          | CA                  |
| Andrew     | Cencini   | Peter         | Krschne          | CA                  |
| Andrew     | Cencini   | Peter         | Krschne          | CA                  |
| Andrew     | Cencini   | Peter         | Krschne          | CA                  |
| Andrew     | Cencini   | Peter         | Krschne          | CA                  |
| Mariya     | Sergienko | John          | Edwards          | CA                  |
| Mariya     | Sergienko | John          | Edwards          | CA                  |
| Mariya     | Sergienko | John          | Edwards          | CA                  |
| Mariya     | Sergienko | John          | Edwards          | CA                  |
| Mariya     | Sergienko | John          | Edwards          | CA                  |
| Mariya     | Sergienko | John          | Edwards          | CA                  |
| Mariya     | Sergienko | John          | Edwards          | CA                  |
| Mariya     | Sergienko | John          | Edwards          | CA                  |
| Mariya     | Sergienko | John          | Edwards          | CA                  |
| Mariya     | Sergienko | John          | Edwards          | CA                  |
| Andrew     | Cencini   | John          | Edwards          | CA                  |
| Andrew     | Cencini   | John          | Edwards          | CA                  |
| Andrew     | Cencini   | John          | Edwards          | CA                  |
| Andrew     | Cencini   | John          | Edwards          | CA                  |
| Andrew     | Cencini   | John          | Edwards          | CA                  |
| Mariya     | Sergienko | Andre         | Ludick           | CA                  |
| Mariya     | Sergienko | Andre         | Ludick           | CA                  |
| Mariya     | Sergienko | Andre         | Ludick           | CA                  |
| Mariya     | Sergienko | Andre         | Ludick           | CA                  |
| Mariya     | Sergienko | Andre         | Ludick           | CA                  |
| Mariya     | Sergienko | Andre         | Ludick           | CA                  |
| Mariya     | Sergienko | Andre         | Ludick           | CA                  |
| Mariya     | Sergienko | Andre         | Ludick           | CA                  |
| Mariya     | Sergienko | Andre         | Ludick           | CA                  |
| Mariya     | Sergienko | Andre         | Ludick           | CA                  |
| Andrew     | Cencini   | Andre         | Ludick           | CA                  |
| Andrew     | Cencini   | Andre         | Ludick           | CA                  |
| Andrew     | Cencini   | Andre         | Ludick           | CA                  |
| Andrew     | Cencini   | Andre         | Ludick           | CA                  |
| Andrew     | Cencini   | Andre         | Ludick           | CA                  |
| Mariya     | Sergienko | Carlos        | Grilo            | CA                  |
| Mariya     | Sergienko | Carlos        | Grilo            | CA                  |
| Mariya     | Sergienko | Carlos        | Grilo            | CA                  |
| Mariya     | Sergienko | Carlos        | Grilo            | CA                  |
| Mariya     | Sergienko | Carlos        | Grilo            | CA                  |
| Mariya     | Sergienko | Carlos        | Grilo            | CA                  |
| Mariya     | Sergienko | Carlos        | Grilo            | CA                  |
| Mariya     | Sergienko | Carlos        | Grilo            | CA                  |
| Mariya     | Sergienko | Carlos        | Grilo            | CA                  |
| Mariya     | Sergienko | Carlos        | Grilo            | CA                  |
| Andrew     | Cencini   | Carlos        | Grilo            | CA                  |
| Andrew     | Cencini   | Carlos        | Grilo            | CA                  |
| Andrew     | Cencini   | Carlos        | Grilo            | CA                  |
| Andrew     | Cencini   | Carlos        | Grilo            | CA                  |
| Andrew     | Cencini   | Carlos        | Grilo            | CA                  |
| Mariya     | Sergienko | Helena        | Kupkova          | CA                  |
| Mariya     | Sergienko | Helena        | Kupkova          | CA                  |
| Mariya     | Sergienko | Helena        | Kupkova          | CA                  |
| Mariya     | Sergienko | Helena        | Kupkova          | CA                  |
| Mariya     | Sergienko | Helena        | Kupkova          | CA                  |
| Mariya     | Sergienko | Helena        | Kupkova          | CA                  |
| Mariya     | Sergienko | Helena        | Kupkova          | CA                  |
| Mariya     | Sergienko | Helena        | Kupkova          | CA                  |
| Mariya     | Sergienko | Helena        | Kupkova          | CA                  |
| Mariya     | Sergienko | Helena        | Kupkova          | CA                  |
| Andrew     | Cencini   | Helena        | Kupkova          | CA                  |
| Andrew     | Cencini   | Helena        | Kupkova          | CA                  |
| Andrew     | Cencini   | Helena        | Kupkova          | CA                  |
| Andrew     | Cencini   | Helena        | Kupkova          | CA                  |
| Andrew     | Cencini   | Helena        | Kupkova          | CA                  |
| Mariya     | Sergienko | Daniel        | Goldschmidt      | CA                  |
| Mariya     | Sergienko | Daniel        | Goldschmidt      | CA                  |
| Mariya     | Sergienko | Daniel        | Goldschmidt      | CA                  |
| Mariya     | Sergienko | Daniel        | Goldschmidt      | CA                  |
| Mariya     | Sergienko | Daniel        | Goldschmidt      | CA                  |
| Mariya     | Sergienko | Daniel        | Goldschmidt      | CA                  |
| Mariya     | Sergienko | Daniel        | Goldschmidt      | CA                  |
| Mariya     | Sergienko | Daniel        | Goldschmidt      | CA                  |
| Mariya     | Sergienko | Daniel        | Goldschmidt      | CA                  |
| Mariya     | Sergienko | Daniel        | Goldschmidt      | CA                  |
| Andrew     | Cencini   | Daniel        | Goldschmidt      | CA                  |
| Andrew     | Cencini   | Daniel        | Goldschmidt      | CA                  |
| Andrew     | Cencini   | Daniel        | Goldschmidt      | CA                  |
| Andrew     | Cencini   | Daniel        | Goldschmidt      | CA                  |
| Andrew     | Cencini   | Daniel        | Goldschmidt      | CA                  |
| Mariya     | Sergienko | Jean Philippe | Bagel            | CA                  |
| Mariya     | Sergienko | Jean Philippe | Bagel            | CA                  |
| Mariya     | Sergienko | Jean Philippe | Bagel            | CA                  |
| Mariya     | Sergienko | Jean Philippe | Bagel            | CA                  |
| Mariya     | Sergienko | Jean Philippe | Bagel            | CA                  |
| Mariya     | Sergienko | Jean Philippe | Bagel            | CA                  |
| Mariya     | Sergienko | Jean Philippe | Bagel            | CA                  |
| Mariya     | Sergienko | Jean Philippe | Bagel            | CA                  |
| Mariya     | Sergienko | Jean Philippe | Bagel            | CA                  |
| Mariya     | Sergienko | Jean Philippe | Bagel            | CA                  |
| Andrew     | Cencini   | Jean Philippe | Bagel            | CA                  |
| Andrew     | Cencini   | Jean Philippe | Bagel            | CA                  |
| Andrew     | Cencini   | Jean Philippe | Bagel            | CA                  |
| Andrew     | Cencini   | Jean Philippe | Bagel            | CA                  |
| Andrew     | Cencini   | Jean Philippe | Bagel            | CA                  |
| Mariya     | Sergienko | Catherine     | Autier Miconi    | CA                  |
| Mariya     | Sergienko | Catherine     | Autier Miconi    | CA                  |
| Mariya     | Sergienko | Catherine     | Autier Miconi    | CA                  |
| Mariya     | Sergienko | Catherine     | Autier Miconi    | CA                  |
| Mariya     | Sergienko | Catherine     | Autier Miconi    | CA                  |
| Mariya     | Sergienko | Catherine     | Autier Miconi    | CA                  |
| Mariya     | Sergienko | Catherine     | Autier Miconi    | CA                  |
| Mariya     | Sergienko | Catherine     | Autier Miconi    | CA                  |
| Mariya     | Sergienko | Catherine     | Autier Miconi    | CA                  |
| Mariya     | Sergienko | Catherine     | Autier Miconi    | CA                  |
| Andrew     | Cencini   | Catherine     | Autier Miconi    | CA                  |
| Andrew     | Cencini   | Catherine     | Autier Miconi    | CA                  |
| Andrew     | Cencini   | Catherine     | Autier Miconi    | CA                  |
| Andrew     | Cencini   | Catherine     | Autier Miconi    | CA                  |
| Andrew     | Cencini   | Catherine     | Autier Miconi    | CA                  |
| Mariya     | Sergienko | Alexander     | Eggerer          | CA                  |
| Mariya     | Sergienko | Alexander     | Eggerer          | CA                  |
| Mariya     | Sergienko | Alexander     | Eggerer          | CA                  |
| Mariya     | Sergienko | Alexander     | Eggerer          | CA                  |
| Mariya     | Sergienko | Alexander     | Eggerer          | CA                  |
| Mariya     | Sergienko | Alexander     | Eggerer          | CA                  |
| Mariya     | Sergienko | Alexander     | Eggerer          | CA                  |
| Mariya     | Sergienko | Alexander     | Eggerer          | CA                  |
| Mariya     | Sergienko | Alexander     | Eggerer          | CA                  |
| Mariya     | Sergienko | Alexander     | Eggerer          | CA                  |
| Andrew     | Cencini   | Alexander     | Eggerer          | CA                  |
| Andrew     | Cencini   | Alexander     | Eggerer          | CA                  |
| Andrew     | Cencini   | Alexander     | Eggerer          | CA                  |
| Andrew     | Cencini   | Alexander     | Eggerer          | CA                  |
| Andrew     | Cencini   | Alexander     | Eggerer          | CA                  |
| Mariya     | Sergienko | George        | Li               | CA                  |
| Mariya     | Sergienko | George        | Li               | CA                  |
| Mariya     | Sergienko | George        | Li               | CA                  |
| Mariya     | Sergienko | George        | Li               | CA                  |
| Mariya     | Sergienko | George        | Li               | CA                  |
| Mariya     | Sergienko | George        | Li               | CA                  |
| Mariya     | Sergienko | George        | Li               | CA                  |
| Mariya     | Sergienko | George        | Li               | CA                  |
| Mariya     | Sergienko | George        | Li               | CA                  |
| Mariya     | Sergienko | George        | Li               | CA                  |
| Andrew     | Cencini   | George        | Li               | CA                  |
| Andrew     | Cencini   | George        | Li               | CA                  |
| Andrew     | Cencini   | George        | Li               | CA                  |
| Andrew     | Cencini   | George        | Li               | CA                  |
| Andrew     | Cencini   | George        | Li               | CA                  |
| Mariya     | Sergienko | Bernard       | Tham             | CA                  |
| Mariya     | Sergienko | Bernard       | Tham             | CA                  |
| Mariya     | Sergienko | Bernard       | Tham             | CA                  |
| Mariya     | Sergienko | Bernard       | Tham             | CA                  |
| Mariya     | Sergienko | Bernard       | Tham             | CA                  |
| Mariya     | Sergienko | Bernard       | Tham             | CA                  |
| Mariya     | Sergienko | Bernard       | Tham             | CA                  |
| Mariya     | Sergienko | Bernard       | Tham             | CA                  |
| Mariya     | Sergienko | Bernard       | Tham             | CA                  |
| Mariya     | Sergienko | Bernard       | Tham             | CA                  |
| Andrew     | Cencini   | Bernard       | Tham             | CA                  |
| Andrew     | Cencini   | Bernard       | Tham             | CA                  |
| Andrew     | Cencini   | Bernard       | Tham             | CA                  |
| Andrew     | Cencini   | Bernard       | Tham             | CA                  |
| Andrew     | Cencini   | Bernard       | Tham             | CA                  |
| Mariya     | Sergienko | Luciana       | Ramos            | CA                  |
| Mariya     | Sergienko | Luciana       | Ramos            | CA                  |
| Mariya     | Sergienko | Luciana       | Ramos            | CA                  |
| Mariya     | Sergienko | Luciana       | Ramos            | CA                  |
| Mariya     | Sergienko | Luciana       | Ramos            | CA                  |
| Mariya     | Sergienko | Luciana       | Ramos            | CA                  |
| Mariya     | Sergienko | Luciana       | Ramos            | CA                  |
| Mariya     | Sergienko | Luciana       | Ramos            | CA                  |
| Mariya     | Sergienko | Luciana       | Ramos            | CA                  |
| Mariya     | Sergienko | Luciana       | Ramos            | CA                  |
| Andrew     | Cencini   | Luciana       | Ramos            | CA                  |
| Andrew     | Cencini   | Luciana       | Ramos            | CA                  |
| Andrew     | Cencini   | Luciana       | Ramos            | CA                  |
| Andrew     | Cencini   | Luciana       | Ramos            | CA                  |
| Andrew     | Cencini   | Luciana       | Ramos            | CA                  |
| Mariya     | Sergienko | Michael       | Entin            | CA                  |
| Mariya     | Sergienko | Michael       | Entin            | CA                  |
| Mariya     | Sergienko | Michael       | Entin            | CA                  |
| Mariya     | Sergienko | Michael       | Entin            | CA                  |
| Mariya     | Sergienko | Michael       | Entin            | CA                  |
| Mariya     | Sergienko | Michael       | Entin            | CA                  |
| Mariya     | Sergienko | Michael       | Entin            | CA                  |
| Mariya     | Sergienko | Michael       | Entin            | CA                  |
| Mariya     | Sergienko | Michael       | Entin            | CA                  |
| Mariya     | Sergienko | Michael       | Entin            | CA                  |
| Andrew     | Cencini   | Michael       | Entin            | CA                  |
| Andrew     | Cencini   | Michael       | Entin            | CA                  |
| Andrew     | Cencini   | Michael       | Entin            | CA                  |
| Andrew     | Cencini   | Michael       | Entin            | CA                  |
| Andrew     | Cencini   | Michael       | Entin            | CA                  |
| Mariya     | Sergienko | Jonas         | Hasselberg       | CA                  |
| Mariya     | Sergienko | Jonas         | Hasselberg       | CA                  |
| Mariya     | Sergienko | Jonas         | Hasselberg       | CA                  |
| Mariya     | Sergienko | Jonas         | Hasselberg       | CA                  |
| Mariya     | Sergienko | Jonas         | Hasselberg       | CA                  |
| Mariya     | Sergienko | Jonas         | Hasselberg       | CA                  |
| Mariya     | Sergienko | Jonas         | Hasselberg       | CA                  |
| Mariya     | Sergienko | Jonas         | Hasselberg       | CA                  |
| Mariya     | Sergienko | Jonas         | Hasselberg       | CA                  |
| Mariya     | Sergienko | Jonas         | Hasselberg       | CA                  |
| Andrew     | Cencini   | Jonas         | Hasselberg       | CA                  |
| Andrew     | Cencini   | Jonas         | Hasselberg       | CA                  |
| Andrew     | Cencini   | Jonas         | Hasselberg       | CA                  |
| Andrew     | Cencini   | Jonas         | Hasselberg       | CA                  |
| Andrew     | Cencini   | Jonas         | Hasselberg       | CA                  |
| Mariya     | Sergienko | John          | Rodman           | CA                  |
| Mariya     | Sergienko | John          | Rodman           | CA                  |
| Mariya     | Sergienko | John          | Rodman           | CA                  |
| Mariya     | Sergienko | John          | Rodman           | CA                  |
| Mariya     | Sergienko | John          | Rodman           | CA                  |
| Mariya     | Sergienko | John          | Rodman           | CA                  |
| Mariya     | Sergienko | John          | Rodman           | CA                  |
| Mariya     | Sergienko | John          | Rodman           | CA                  |
| Mariya     | Sergienko | John          | Rodman           | CA                  |
| Mariya     | Sergienko | John          | Rodman           | CA                  |
| Andrew     | Cencini   | John          | Rodman           | CA                  |
| Andrew     | Cencini   | John          | Rodman           | CA                  |
| Andrew     | Cencini   | John          | Rodman           | CA                  |
| Andrew     | Cencini   | John          | Rodman           | CA                  |
| Andrew     | Cencini   | John          | Rodman           | CA                  |
| Mariya     | Sergienko | Run           | Liu              | CA                  |
| Mariya     | Sergienko | Run           | Liu              | CA                  |
| Mariya     | Sergienko | Run           | Liu              | CA                  |
| Mariya     | Sergienko | Run           | Liu              | CA                  |
| Mariya     | Sergienko | Run           | Liu              | CA                  |
| Mariya     | Sergienko | Run           | Liu              | CA                  |
| Mariya     | Sergienko | Run           | Liu              | CA                  |
| Mariya     | Sergienko | Run           | Liu              | CA                  |
| Mariya     | Sergienko | Run           | Liu              | CA                  |
| Mariya     | Sergienko | Run           | Liu              | CA                  |
| Andrew     | Cencini   | Run           | Liu              | CA                  |
| Andrew     | Cencini   | Run           | Liu              | CA                  |
| Andrew     | Cencini   | Run           | Liu              | CA                  |
| Andrew     | Cencini   | Run           | Liu              | CA                  |
| Andrew     | Cencini   | Run           | Liu              | CA                  |
| Mariya     | Sergienko | Karen         | Toh              | CA                  |
| Mariya     | Sergienko | Karen         | Toh              | CA                  |
| Mariya     | Sergienko | Karen         | Toh              | CA                  |
| Mariya     | Sergienko | Karen         | Toh              | CA                  |
| Mariya     | Sergienko | Karen         | Toh              | CA                  |
| Mariya     | Sergienko | Karen         | Toh              | CA                  |
| Mariya     | Sergienko | Karen         | Toh              | CA                  |
| Mariya     | Sergienko | Karen         | Toh              | CA                  |
| Mariya     | Sergienko | Karen         | Toh              | CA                  |
| Mariya     | Sergienko | Karen         | Toh              | CA                  |
| Andrew     | Cencini   | Karen         | Toh              | CA                  |
| Andrew     | Cencini   | Karen         | Toh              | CA                  |
| Andrew     | Cencini   | Karen         | Toh              | CA                  |
| Andrew     | Cencini   | Karen         | Toh              | CA                  |
| Andrew     | Cencini   | Karen         | Toh              | CA                  |
| Mariya     | Sergienko | Amritansh     | Raghav           | CA                  |
| Mariya     | Sergienko | Amritansh     | Raghav           | CA                  |
| Mariya     | Sergienko | Amritansh     | Raghav           | CA                  |
| Mariya     | Sergienko | Amritansh     | Raghav           | CA                  |
| Mariya     | Sergienko | Amritansh     | Raghav           | CA                  |
| Mariya     | Sergienko | Amritansh     | Raghav           | CA                  |
| Mariya     | Sergienko | Amritansh     | Raghav           | CA                  |
| Mariya     | Sergienko | Amritansh     | Raghav           | CA                  |
| Mariya     | Sergienko | Amritansh     | Raghav           | CA                  |
| Mariya     | Sergienko | Amritansh     | Raghav           | CA                  |
| Andrew     | Cencini   | Amritansh     | Raghav           | CA                  |
| Andrew     | Cencini   | Amritansh     | Raghav           | CA                  |
| Andrew     | Cencini   | Amritansh     | Raghav           | CA                  |
| Andrew     | Cencini   | Amritansh     | Raghav           | CA                  |
| Andrew     | Cencini   | Amritansh     | Raghav           | CA                  |
| Mariya     | Sergienko | Soo Jung      | Lee              | CA                  |
| Mariya     | Sergienko | Soo Jung      | Lee              | CA                  |
| Mariya     | Sergienko | Soo Jung      | Lee              | CA                  |
| Mariya     | Sergienko | Soo Jung      | Lee              | CA                  |
| Mariya     | Sergienko | Soo Jung      | Lee              | CA                  |
| Mariya     | Sergienko | Soo Jung      | Lee              | CA                  |
| Mariya     | Sergienko | Soo Jung      | Lee              | CA                  |
| Mariya     | Sergienko | Soo Jung      | Lee              | CA                  |
| Mariya     | Sergienko | Soo Jung      | Lee              | CA                  |
| Mariya     | Sergienko | Soo Jung      | Lee              | CA                  |
| Andrew     | Cencini   | Soo Jung      | Lee              | CA                  |
| Andrew     | Cencini   | Soo Jung      | Lee              | CA                  |
| Andrew     | Cencini   | Soo Jung      | Lee              | CA                  |
| Andrew     | Cencini   | Soo Jung      | Lee              | CA                  |
| Andrew     | Cencini   | Soo Jung      | Lee              | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Andrew     | Cencini   | Anna          | Bedecs           | CA                  |
| Andrew     | Cencini   | Anna          | Bedecs           | CA                  |
| Andrew     | Cencini   | Anna          | Bedecs           | CA                  |
| Andrew     | Cencini   | Anna          | Bedecs           | CA                  |
| Andrew     | Cencini   | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Andrew     | Cencini   | Antonio       | Gratacos Solsona | CA                  |
| Andrew     | Cencini   | Antonio       | Gratacos Solsona | CA                  |
| Andrew     | Cencini   | Antonio       | Gratacos Solsona | CA                  |
| Andrew     | Cencini   | Antonio       | Gratacos Solsona | CA                  |
| Andrew     | Cencini   | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Andrew     | Cencini   | Thomas        | Axen             | CA                  |
| Andrew     | Cencini   | Thomas        | Axen             | CA                  |
| Andrew     | Cencini   | Thomas        | Axen             | CA                  |
| Andrew     | Cencini   | Thomas        | Axen             | CA                  |
| Andrew     | Cencini   | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Andrew     | Cencini   | Christina     | Lee              | CA                  |
| Andrew     | Cencini   | Christina     | Lee              | CA                  |
| Andrew     | Cencini   | Christina     | Lee              | CA                  |
| Andrew     | Cencini   | Christina     | Lee              | CA                  |
| Andrew     | Cencini   | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Martin        | O'Donnell        | CA                  |
| Mariya     | Sergienko | Martin        | O'Donnell        | CA                  |
| Mariya     | Sergienko | Martin        | O'Donnell        | CA                  |
| Mariya     | Sergienko | Martin        | O'Donnell        | CA                  |
| Mariya     | Sergienko | Martin        | O'Donnell        | CA                  |
| Mariya     | Sergienko | Martin        | O'Donnell        | CA                  |
| Mariya     | Sergienko | Martin        | O'Donnell        | CA                  |
| Mariya     | Sergienko | Martin        | O'Donnell        | CA                  |
| Mariya     | Sergienko | Martin        | O'Donnell        | CA                  |
| Mariya     | Sergienko | Martin        | O'Donnell        | CA                  |
| Andrew     | Cencini   | Martin        | O'Donnell        | CA                  |
| Andrew     | Cencini   | Martin        | O'Donnell        | CA                  |
| Andrew     | Cencini   | Martin        | O'Donnell        | CA                  |
| Andrew     | Cencini   | Martin        | O'Donnell        | CA                  |
| Andrew     | Cencini   | Martin        | O'Donnell        | CA                  |
| Mariya     | Sergienko | Francisco     | Perez-Olaeta     | CA                  |
| Mariya     | Sergienko | Francisco     | Perez-Olaeta     | CA                  |
| Mariya     | Sergienko | Francisco     | Perez-Olaeta     | CA                  |
| Mariya     | Sergienko | Francisco     | Perez-Olaeta     | CA                  |
| Mariya     | Sergienko | Francisco     | Perez-Olaeta     | CA                  |
| Mariya     | Sergienko | Francisco     | Perez-Olaeta     | CA                  |
| Mariya     | Sergienko | Francisco     | Perez-Olaeta     | CA                  |
| Mariya     | Sergienko | Francisco     | Perez-Olaeta     | CA                  |
| Mariya     | Sergienko | Francisco     | Perez-Olaeta     | CA                  |
| Mariya     | Sergienko | Francisco     | Perez-Olaeta     | CA                  |
| Andrew     | Cencini   | Francisco     | Perez-Olaeta     | CA                  |
| Andrew     | Cencini   | Francisco     | Perez-Olaeta     | CA                  |
| Andrew     | Cencini   | Francisco     | Perez-Olaeta     | CA                  |
| Andrew     | Cencini   | Francisco     | Perez-Olaeta     | CA                  |
| Andrew     | Cencini   | Francisco     | Perez-Olaeta     | CA                  |
| Mariya     | Sergienko | Ming-Yang     | Xie              | CA                  |
| Mariya     | Sergienko | Ming-Yang     | Xie              | CA                  |
| Mariya     | Sergienko | Ming-Yang     | Xie              | CA                  |
| Mariya     | Sergienko | Ming-Yang     | Xie              | CA                  |
| Mariya     | Sergienko | Ming-Yang     | Xie              | CA                  |
| Mariya     | Sergienko | Ming-Yang     | Xie              | CA                  |
| Mariya     | Sergienko | Ming-Yang     | Xie              | CA                  |
| Mariya     | Sergienko | Ming-Yang     | Xie              | CA                  |
| Mariya     | Sergienko | Ming-Yang     | Xie              | CA                  |
| Mariya     | Sergienko | Ming-Yang     | Xie              | CA                  |
| Andrew     | Cencini   | Ming-Yang     | Xie              | CA                  |
| Andrew     | Cencini   | Ming-Yang     | Xie              | CA                  |
| Andrew     | Cencini   | Ming-Yang     | Xie              | CA                  |
| Andrew     | Cencini   | Ming-Yang     | Xie              | CA                  |
| Andrew     | Cencini   | Ming-Yang     | Xie              | CA                  |
| Mariya     | Sergienko | Elizabeth     | Andersen         | CA                  |
| Mariya     | Sergienko | Elizabeth     | Andersen         | CA                  |
| Mariya     | Sergienko | Elizabeth     | Andersen         | CA                  |
| Mariya     | Sergienko | Elizabeth     | Andersen         | CA                  |
| Mariya     | Sergienko | Elizabeth     | Andersen         | CA                  |
| Mariya     | Sergienko | Elizabeth     | Andersen         | CA                  |
| Mariya     | Sergienko | Elizabeth     | Andersen         | CA                  |
| Mariya     | Sergienko | Elizabeth     | Andersen         | CA                  |
| Mariya     | Sergienko | Elizabeth     | Andersen         | CA                  |
| Mariya     | Sergienko | Elizabeth     | Andersen         | CA                  |
| Andrew     | Cencini   | Elizabeth     | Andersen         | CA                  |
| Andrew     | Cencini   | Elizabeth     | Andersen         | CA                  |
| Andrew     | Cencini   | Elizabeth     | Andersen         | CA                  |
| Andrew     | Cencini   | Elizabeth     | Andersen         | CA                  |
| Andrew     | Cencini   | Elizabeth     | Andersen         | CA                  |
| Mariya     | Sergienko | Sven          | Mortensen        | CA                  |
| Mariya     | Sergienko | Sven          | Mortensen        | CA                  |
| Mariya     | Sergienko | Sven          | Mortensen        | CA                  |
| Mariya     | Sergienko | Sven          | Mortensen        | CA                  |
| Mariya     | Sergienko | Sven          | Mortensen        | CA                  |
| Mariya     | Sergienko | Sven          | Mortensen        | CA                  |
| Mariya     | Sergienko | Sven          | Mortensen        | CA                  |
| Mariya     | Sergienko | Sven          | Mortensen        | CA                  |
| Mariya     | Sergienko | Sven          | Mortensen        | CA                  |
| Mariya     | Sergienko | Sven          | Mortensen        | CA                  |
| Andrew     | Cencini   | Sven          | Mortensen        | CA                  |
| Andrew     | Cencini   | Sven          | Mortensen        | CA                  |
| Andrew     | Cencini   | Sven          | Mortensen        | CA                  |
| Andrew     | Cencini   | Sven          | Mortensen        | CA                  |
| Andrew     | Cencini   | Sven          | Mortensen        | CA                  |
| Mariya     | Sergienko | Roland        | Wacker           | CA                  |
| Mariya     | Sergienko | Roland        | Wacker           | CA                  |
| Mariya     | Sergienko | Roland        | Wacker           | CA                  |
| Mariya     | Sergienko | Roland        | Wacker           | CA                  |
| Mariya     | Sergienko | Roland        | Wacker           | CA                  |
| Mariya     | Sergienko | Roland        | Wacker           | CA                  |
| Mariya     | Sergienko | Roland        | Wacker           | CA                  |
| Mariya     | Sergienko | Roland        | Wacker           | CA                  |
| Mariya     | Sergienko | Roland        | Wacker           | CA                  |
| Mariya     | Sergienko | Roland        | Wacker           | CA                  |
| Andrew     | Cencini   | Roland        | Wacker           | CA                  |
| Andrew     | Cencini   | Roland        | Wacker           | CA                  |
| Andrew     | Cencini   | Roland        | Wacker           | CA                  |
| Andrew     | Cencini   | Roland        | Wacker           | CA                  |
| Andrew     | Cencini   | Roland        | Wacker           | CA                  |
| Mariya     | Sergienko | Peter         | Krschne          | CA                  |
| Mariya     | Sergienko | Peter         | Krschne          | CA                  |
| Mariya     | Sergienko | Peter         | Krschne          | CA                  |
| Mariya     | Sergienko | Peter         | Krschne          | CA                  |
| Mariya     | Sergienko | Peter         | Krschne          | CA                  |
| Mariya     | Sergienko | Peter         | Krschne          | CA                  |
| Mariya     | Sergienko | Peter         | Krschne          | CA                  |
| Mariya     | Sergienko | Peter         | Krschne          | CA                  |
| Mariya     | Sergienko | Peter         | Krschne          | CA                  |
| Mariya     | Sergienko | Peter         | Krschne          | CA                  |
| Andrew     | Cencini   | Peter         | Krschne          | CA                  |
| Andrew     | Cencini   | Peter         | Krschne          | CA                  |
| Andrew     | Cencini   | Peter         | Krschne          | CA                  |
| Andrew     | Cencini   | Peter         | Krschne          | CA                  |
| Andrew     | Cencini   | Peter         | Krschne          | CA                  |
| Mariya     | Sergienko | John          | Edwards          | CA                  |
| Mariya     | Sergienko | John          | Edwards          | CA                  |
| Mariya     | Sergienko | John          | Edwards          | CA                  |
| Mariya     | Sergienko | John          | Edwards          | CA                  |
| Mariya     | Sergienko | John          | Edwards          | CA                  |
| Mariya     | Sergienko | John          | Edwards          | CA                  |
| Mariya     | Sergienko | John          | Edwards          | CA                  |
| Mariya     | Sergienko | John          | Edwards          | CA                  |
| Mariya     | Sergienko | John          | Edwards          | CA                  |
| Mariya     | Sergienko | John          | Edwards          | CA                  |
| Andrew     | Cencini   | John          | Edwards          | CA                  |
| Andrew     | Cencini   | John          | Edwards          | CA                  |
| Andrew     | Cencini   | John          | Edwards          | CA                  |
| Andrew     | Cencini   | John          | Edwards          | CA                  |
| Andrew     | Cencini   | John          | Edwards          | CA                  |
| Mariya     | Sergienko | Andre         | Ludick           | CA                  |
| Mariya     | Sergienko | Andre         | Ludick           | CA                  |
| Mariya     | Sergienko | Andre         | Ludick           | CA                  |
| Mariya     | Sergienko | Andre         | Ludick           | CA                  |
| Mariya     | Sergienko | Andre         | Ludick           | CA                  |
| Mariya     | Sergienko | Andre         | Ludick           | CA                  |
| Mariya     | Sergienko | Andre         | Ludick           | CA                  |
| Mariya     | Sergienko | Andre         | Ludick           | CA                  |
| Mariya     | Sergienko | Andre         | Ludick           | CA                  |
| Mariya     | Sergienko | Andre         | Ludick           | CA                  |
| Andrew     | Cencini   | Andre         | Ludick           | CA                  |
| Andrew     | Cencini   | Andre         | Ludick           | CA                  |
| Andrew     | Cencini   | Andre         | Ludick           | CA                  |
| Andrew     | Cencini   | Andre         | Ludick           | CA                  |
| Andrew     | Cencini   | Andre         | Ludick           | CA                  |
| Mariya     | Sergienko | Carlos        | Grilo            | CA                  |
| Mariya     | Sergienko | Carlos        | Grilo            | CA                  |
| Mariya     | Sergienko | Carlos        | Grilo            | CA                  |
| Mariya     | Sergienko | Carlos        | Grilo            | CA                  |
| Mariya     | Sergienko | Carlos        | Grilo            | CA                  |
| Mariya     | Sergienko | Carlos        | Grilo            | CA                  |
| Mariya     | Sergienko | Carlos        | Grilo            | CA                  |
| Mariya     | Sergienko | Carlos        | Grilo            | CA                  |
| Mariya     | Sergienko | Carlos        | Grilo            | CA                  |
| Mariya     | Sergienko | Carlos        | Grilo            | CA                  |
| Andrew     | Cencini   | Carlos        | Grilo            | CA                  |
| Andrew     | Cencini   | Carlos        | Grilo            | CA                  |
| Andrew     | Cencini   | Carlos        | Grilo            | CA                  |
| Andrew     | Cencini   | Carlos        | Grilo            | CA                  |
| Andrew     | Cencini   | Carlos        | Grilo            | CA                  |
| Mariya     | Sergienko | Helena        | Kupkova          | CA                  |
| Mariya     | Sergienko | Helena        | Kupkova          | CA                  |
| Mariya     | Sergienko | Helena        | Kupkova          | CA                  |
| Mariya     | Sergienko | Helena        | Kupkova          | CA                  |
| Mariya     | Sergienko | Helena        | Kupkova          | CA                  |
| Mariya     | Sergienko | Helena        | Kupkova          | CA                  |
| Mariya     | Sergienko | Helena        | Kupkova          | CA                  |
| Mariya     | Sergienko | Helena        | Kupkova          | CA                  |
| Mariya     | Sergienko | Helena        | Kupkova          | CA                  |
| Mariya     | Sergienko | Helena        | Kupkova          | CA                  |
| Andrew     | Cencini   | Helena        | Kupkova          | CA                  |
| Andrew     | Cencini   | Helena        | Kupkova          | CA                  |
| Andrew     | Cencini   | Helena        | Kupkova          | CA                  |
| Andrew     | Cencini   | Helena        | Kupkova          | CA                  |
| Andrew     | Cencini   | Helena        | Kupkova          | CA                  |
| Mariya     | Sergienko | Daniel        | Goldschmidt      | CA                  |
| Mariya     | Sergienko | Daniel        | Goldschmidt      | CA                  |
| Mariya     | Sergienko | Daniel        | Goldschmidt      | CA                  |
| Mariya     | Sergienko | Daniel        | Goldschmidt      | CA                  |
| Mariya     | Sergienko | Daniel        | Goldschmidt      | CA                  |
| Mariya     | Sergienko | Daniel        | Goldschmidt      | CA                  |
| Mariya     | Sergienko | Daniel        | Goldschmidt      | CA                  |
| Mariya     | Sergienko | Daniel        | Goldschmidt      | CA                  |
| Mariya     | Sergienko | Daniel        | Goldschmidt      | CA                  |
| Mariya     | Sergienko | Daniel        | Goldschmidt      | CA                  |
| Andrew     | Cencini   | Daniel        | Goldschmidt      | CA                  |
| Andrew     | Cencini   | Daniel        | Goldschmidt      | CA                  |
| Andrew     | Cencini   | Daniel        | Goldschmidt      | CA                  |
| Andrew     | Cencini   | Daniel        | Goldschmidt      | CA                  |
| Andrew     | Cencini   | Daniel        | Goldschmidt      | CA                  |
| Mariya     | Sergienko | Jean Philippe | Bagel            | CA                  |
| Mariya     | Sergienko | Jean Philippe | Bagel            | CA                  |
| Mariya     | Sergienko | Jean Philippe | Bagel            | CA                  |
| Mariya     | Sergienko | Jean Philippe | Bagel            | CA                  |
| Mariya     | Sergienko | Jean Philippe | Bagel            | CA                  |
| Mariya     | Sergienko | Jean Philippe | Bagel            | CA                  |
| Mariya     | Sergienko | Jean Philippe | Bagel            | CA                  |
| Mariya     | Sergienko | Jean Philippe | Bagel            | CA                  |
| Mariya     | Sergienko | Jean Philippe | Bagel            | CA                  |
| Mariya     | Sergienko | Jean Philippe | Bagel            | CA                  |
| Andrew     | Cencini   | Jean Philippe | Bagel            | CA                  |
| Andrew     | Cencini   | Jean Philippe | Bagel            | CA                  |
| Andrew     | Cencini   | Jean Philippe | Bagel            | CA                  |
| Andrew     | Cencini   | Jean Philippe | Bagel            | CA                  |
| Andrew     | Cencini   | Jean Philippe | Bagel            | CA                  |
| Mariya     | Sergienko | Catherine     | Autier Miconi    | CA                  |
| Mariya     | Sergienko | Catherine     | Autier Miconi    | CA                  |
| Mariya     | Sergienko | Catherine     | Autier Miconi    | CA                  |
| Mariya     | Sergienko | Catherine     | Autier Miconi    | CA                  |
| Mariya     | Sergienko | Catherine     | Autier Miconi    | CA                  |
| Mariya     | Sergienko | Catherine     | Autier Miconi    | CA                  |
| Mariya     | Sergienko | Catherine     | Autier Miconi    | CA                  |
| Mariya     | Sergienko | Catherine     | Autier Miconi    | CA                  |
| Mariya     | Sergienko | Catherine     | Autier Miconi    | CA                  |
| Mariya     | Sergienko | Catherine     | Autier Miconi    | CA                  |
| Andrew     | Cencini   | Catherine     | Autier Miconi    | CA                  |
| Andrew     | Cencini   | Catherine     | Autier Miconi    | CA                  |
| Andrew     | Cencini   | Catherine     | Autier Miconi    | CA                  |
| Andrew     | Cencini   | Catherine     | Autier Miconi    | CA                  |
| Andrew     | Cencini   | Catherine     | Autier Miconi    | CA                  |
| Mariya     | Sergienko | Alexander     | Eggerer          | CA                  |
| Mariya     | Sergienko | Alexander     | Eggerer          | CA                  |
| Mariya     | Sergienko | Alexander     | Eggerer          | CA                  |
| Mariya     | Sergienko | Alexander     | Eggerer          | CA                  |
| Mariya     | Sergienko | Alexander     | Eggerer          | CA                  |
| Mariya     | Sergienko | Alexander     | Eggerer          | CA                  |
| Mariya     | Sergienko | Alexander     | Eggerer          | CA                  |
| Mariya     | Sergienko | Alexander     | Eggerer          | CA                  |
| Mariya     | Sergienko | Alexander     | Eggerer          | CA                  |
| Mariya     | Sergienko | Alexander     | Eggerer          | CA                  |
| Andrew     | Cencini   | Alexander     | Eggerer          | CA                  |
| Andrew     | Cencini   | Alexander     | Eggerer          | CA                  |
| Andrew     | Cencini   | Alexander     | Eggerer          | CA                  |
| Andrew     | Cencini   | Alexander     | Eggerer          | CA                  |
| Andrew     | Cencini   | Alexander     | Eggerer          | CA                  |
| Mariya     | Sergienko | George        | Li               | CA                  |
| Mariya     | Sergienko | George        | Li               | CA                  |
| Mariya     | Sergienko | George        | Li               | CA                  |
| Mariya     | Sergienko | George        | Li               | CA                  |
| Mariya     | Sergienko | George        | Li               | CA                  |
| Mariya     | Sergienko | George        | Li               | CA                  |
| Mariya     | Sergienko | George        | Li               | CA                  |
| Mariya     | Sergienko | George        | Li               | CA                  |
| Mariya     | Sergienko | George        | Li               | CA                  |
| Mariya     | Sergienko | George        | Li               | CA                  |
| Andrew     | Cencini   | George        | Li               | CA                  |
| Andrew     | Cencini   | George        | Li               | CA                  |
| Andrew     | Cencini   | George        | Li               | CA                  |
| Andrew     | Cencini   | George        | Li               | CA                  |
| Andrew     | Cencini   | George        | Li               | CA                  |
| Mariya     | Sergienko | Bernard       | Tham             | CA                  |
| Mariya     | Sergienko | Bernard       | Tham             | CA                  |
| Mariya     | Sergienko | Bernard       | Tham             | CA                  |
| Mariya     | Sergienko | Bernard       | Tham             | CA                  |
| Mariya     | Sergienko | Bernard       | Tham             | CA                  |
| Mariya     | Sergienko | Bernard       | Tham             | CA                  |
| Mariya     | Sergienko | Bernard       | Tham             | CA                  |
| Mariya     | Sergienko | Bernard       | Tham             | CA                  |
| Mariya     | Sergienko | Bernard       | Tham             | CA                  |
| Mariya     | Sergienko | Bernard       | Tham             | CA                  |
| Andrew     | Cencini   | Bernard       | Tham             | CA                  |
| Andrew     | Cencini   | Bernard       | Tham             | CA                  |
| Andrew     | Cencini   | Bernard       | Tham             | CA                  |
| Andrew     | Cencini   | Bernard       | Tham             | CA                  |
| Andrew     | Cencini   | Bernard       | Tham             | CA                  |
| Mariya     | Sergienko | Luciana       | Ramos            | CA                  |
| Mariya     | Sergienko | Luciana       | Ramos            | CA                  |
| Mariya     | Sergienko | Luciana       | Ramos            | CA                  |
| Mariya     | Sergienko | Luciana       | Ramos            | CA                  |
| Mariya     | Sergienko | Luciana       | Ramos            | CA                  |
| Mariya     | Sergienko | Luciana       | Ramos            | CA                  |
| Mariya     | Sergienko | Luciana       | Ramos            | CA                  |
| Mariya     | Sergienko | Luciana       | Ramos            | CA                  |
| Mariya     | Sergienko | Luciana       | Ramos            | CA                  |
| Mariya     | Sergienko | Luciana       | Ramos            | CA                  |
| Andrew     | Cencini   | Luciana       | Ramos            | CA                  |
| Andrew     | Cencini   | Luciana       | Ramos            | CA                  |
| Andrew     | Cencini   | Luciana       | Ramos            | CA                  |
| Andrew     | Cencini   | Luciana       | Ramos            | CA                  |
| Andrew     | Cencini   | Luciana       | Ramos            | CA                  |
| Mariya     | Sergienko | Michael       | Entin            | CA                  |
| Mariya     | Sergienko | Michael       | Entin            | CA                  |
| Mariya     | Sergienko | Michael       | Entin            | CA                  |
| Mariya     | Sergienko | Michael       | Entin            | CA                  |
| Mariya     | Sergienko | Michael       | Entin            | CA                  |
| Mariya     | Sergienko | Michael       | Entin            | CA                  |
| Mariya     | Sergienko | Michael       | Entin            | CA                  |
| Mariya     | Sergienko | Michael       | Entin            | CA                  |
| Mariya     | Sergienko | Michael       | Entin            | CA                  |
| Mariya     | Sergienko | Michael       | Entin            | CA                  |
| Andrew     | Cencini   | Michael       | Entin            | CA                  |
| Andrew     | Cencini   | Michael       | Entin            | CA                  |
| Andrew     | Cencini   | Michael       | Entin            | CA                  |
| Andrew     | Cencini   | Michael       | Entin            | CA                  |
| Andrew     | Cencini   | Michael       | Entin            | CA                  |
| Mariya     | Sergienko | Jonas         | Hasselberg       | CA                  |
| Mariya     | Sergienko | Jonas         | Hasselberg       | CA                  |
| Mariya     | Sergienko | Jonas         | Hasselberg       | CA                  |
| Mariya     | Sergienko | Jonas         | Hasselberg       | CA                  |
| Mariya     | Sergienko | Jonas         | Hasselberg       | CA                  |
| Mariya     | Sergienko | Jonas         | Hasselberg       | CA                  |
| Mariya     | Sergienko | Jonas         | Hasselberg       | CA                  |
| Mariya     | Sergienko | Jonas         | Hasselberg       | CA                  |
| Mariya     | Sergienko | Jonas         | Hasselberg       | CA                  |
| Mariya     | Sergienko | Jonas         | Hasselberg       | CA                  |
| Andrew     | Cencini   | Jonas         | Hasselberg       | CA                  |
| Andrew     | Cencini   | Jonas         | Hasselberg       | CA                  |
| Andrew     | Cencini   | Jonas         | Hasselberg       | CA                  |
| Andrew     | Cencini   | Jonas         | Hasselberg       | CA                  |
| Andrew     | Cencini   | Jonas         | Hasselberg       | CA                  |
| Mariya     | Sergienko | John          | Rodman           | CA                  |
| Mariya     | Sergienko | John          | Rodman           | CA                  |
| Mariya     | Sergienko | John          | Rodman           | CA                  |
| Mariya     | Sergienko | John          | Rodman           | CA                  |
| Mariya     | Sergienko | John          | Rodman           | CA                  |
| Mariya     | Sergienko | John          | Rodman           | CA                  |
| Mariya     | Sergienko | John          | Rodman           | CA                  |
| Mariya     | Sergienko | John          | Rodman           | CA                  |
| Mariya     | Sergienko | John          | Rodman           | CA                  |
| Mariya     | Sergienko | John          | Rodman           | CA                  |
| Andrew     | Cencini   | John          | Rodman           | CA                  |
| Andrew     | Cencini   | John          | Rodman           | CA                  |
| Andrew     | Cencini   | John          | Rodman           | CA                  |
| Andrew     | Cencini   | John          | Rodman           | CA                  |
| Andrew     | Cencini   | John          | Rodman           | CA                  |
| Mariya     | Sergienko | Run           | Liu              | CA                  |
| Mariya     | Sergienko | Run           | Liu              | CA                  |
| Mariya     | Sergienko | Run           | Liu              | CA                  |
| Mariya     | Sergienko | Run           | Liu              | CA                  |
| Mariya     | Sergienko | Run           | Liu              | CA                  |
| Mariya     | Sergienko | Run           | Liu              | CA                  |
| Mariya     | Sergienko | Run           | Liu              | CA                  |
| Mariya     | Sergienko | Run           | Liu              | CA                  |
| Mariya     | Sergienko | Run           | Liu              | CA                  |
| Mariya     | Sergienko | Run           | Liu              | CA                  |
| Andrew     | Cencini   | Run           | Liu              | CA                  |
| Andrew     | Cencini   | Run           | Liu              | CA                  |
| Andrew     | Cencini   | Run           | Liu              | CA                  |
| Andrew     | Cencini   | Run           | Liu              | CA                  |
| Andrew     | Cencini   | Run           | Liu              | CA                  |
| Mariya     | Sergienko | Karen         | Toh              | CA                  |
| Mariya     | Sergienko | Karen         | Toh              | CA                  |
| Mariya     | Sergienko | Karen         | Toh              | CA                  |
| Mariya     | Sergienko | Karen         | Toh              | CA                  |
| Mariya     | Sergienko | Karen         | Toh              | CA                  |
| Mariya     | Sergienko | Karen         | Toh              | CA                  |
| Mariya     | Sergienko | Karen         | Toh              | CA                  |
| Mariya     | Sergienko | Karen         | Toh              | CA                  |
| Mariya     | Sergienko | Karen         | Toh              | CA                  |
| Mariya     | Sergienko | Karen         | Toh              | CA                  |
| Andrew     | Cencini   | Karen         | Toh              | CA                  |
| Andrew     | Cencini   | Karen         | Toh              | CA                  |
| Andrew     | Cencini   | Karen         | Toh              | CA                  |
| Andrew     | Cencini   | Karen         | Toh              | CA                  |
| Andrew     | Cencini   | Karen         | Toh              | CA                  |
| Mariya     | Sergienko | Amritansh     | Raghav           | CA                  |
| Mariya     | Sergienko | Amritansh     | Raghav           | CA                  |
| Mariya     | Sergienko | Amritansh     | Raghav           | CA                  |
| Mariya     | Sergienko | Amritansh     | Raghav           | CA                  |
| Mariya     | Sergienko | Amritansh     | Raghav           | CA                  |
| Mariya     | Sergienko | Amritansh     | Raghav           | CA                  |
| Mariya     | Sergienko | Amritansh     | Raghav           | CA                  |
| Mariya     | Sergienko | Amritansh     | Raghav           | CA                  |
| Mariya     | Sergienko | Amritansh     | Raghav           | CA                  |
| Mariya     | Sergienko | Amritansh     | Raghav           | CA                  |
| Andrew     | Cencini   | Amritansh     | Raghav           | CA                  |
| Andrew     | Cencini   | Amritansh     | Raghav           | CA                  |
| Andrew     | Cencini   | Amritansh     | Raghav           | CA                  |
| Andrew     | Cencini   | Amritansh     | Raghav           | CA                  |
| Andrew     | Cencini   | Amritansh     | Raghav           | CA                  |
| Mariya     | Sergienko | Soo Jung      | Lee              | CA                  |
| Mariya     | Sergienko | Soo Jung      | Lee              | CA                  |
| Mariya     | Sergienko | Soo Jung      | Lee              | CA                  |
| Mariya     | Sergienko | Soo Jung      | Lee              | CA                  |
| Mariya     | Sergienko | Soo Jung      | Lee              | CA                  |
| Mariya     | Sergienko | Soo Jung      | Lee              | CA                  |
| Mariya     | Sergienko | Soo Jung      | Lee              | CA                  |
| Mariya     | Sergienko | Soo Jung      | Lee              | CA                  |
| Mariya     | Sergienko | Soo Jung      | Lee              | CA                  |
| Mariya     | Sergienko | Soo Jung      | Lee              | CA                  |
| Andrew     | Cencini   | Soo Jung      | Lee              | CA                  |
| Andrew     | Cencini   | Soo Jung      | Lee              | CA                  |
| Andrew     | Cencini   | Soo Jung      | Lee              | CA                  |
| Andrew     | Cencini   | Soo Jung      | Lee              | CA                  |
| Andrew     | Cencini   | Soo Jung      | Lee              | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Anna          | Bedecs           | CA                  |
| Andrew     | Cencini   | Anna          | Bedecs           | CA                  |
| Andrew     | Cencini   | Anna          | Bedecs           | CA                  |
| Andrew     | Cencini   | Anna          | Bedecs           | CA                  |
| Andrew     | Cencini   | Anna          | Bedecs           | CA                  |
| Andrew     | Cencini   | Anna          | Bedecs           | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Antonio       | Gratacos Solsona | CA                  |
| Andrew     | Cencini   | Antonio       | Gratacos Solsona | CA                  |
| Andrew     | Cencini   | Antonio       | Gratacos Solsona | CA                  |
| Andrew     | Cencini   | Antonio       | Gratacos Solsona | CA                  |
| Andrew     | Cencini   | Antonio       | Gratacos Solsona | CA                  |
| Andrew     | Cencini   | Antonio       | Gratacos Solsona | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Thomas        | Axen             | CA                  |
| Andrew     | Cencini   | Thomas        | Axen             | CA                  |
| Andrew     | Cencini   | Thomas        | Axen             | CA                  |
| Andrew     | Cencini   | Thomas        | Axen             | CA                  |
| Andrew     | Cencini   | Thomas        | Axen             | CA                  |
| Andrew     | Cencini   | Thomas        | Axen             | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Christina     | Lee              | CA                  |
| Andrew     | Cencini   | Christina     | Lee              | CA                  |
| Andrew     | Cencini   | Christina     | Lee              | CA                  |
| Andrew     | Cencini   | Christina     | Lee              | CA                  |
| Andrew     | Cencini   | Christina     | Lee              | CA                  |
| Andrew     | Cencini   | Christina     | Lee              | CA                  |
| Mariya     | Sergienko | Martin        | O'Donnell        | CA                  |
| Mariya     | Sergienko | Martin        | O'Donnell        | CA                  |
| Mariya     | Sergienko | Martin        | O'Donnell        | CA                  |
| Mariya     | Sergienko | Martin        | O'Donnell        | CA                  |
| Mariya     | Sergienko | Martin        | O'Donnell        | CA                  |
| Mariya     | Sergienko | Martin        | O'Donnell        | CA                  |
| Mariya     | Sergienko | Martin        | O'Donnell        | CA                  |
| Mariya     | Sergienko | Martin        | O'Donnell        | CA                  |
| Mariya     | Sergienko | Martin        | O'Donnell        | CA                  |
| Mariya     | Sergienko | Martin        | O'Donnell        | CA                  |
| Andrew     | Cencini   | Martin        | O'Donnell        | CA                  |
| Andrew     | Cencini   | Martin        | O'Donnell        | CA                  |
| Andrew     | Cencini   | Martin        | O'Donnell        | CA                  |
| Andrew     | Cencini   | Martin        | O'Donnell        | CA                  |
| Andrew     | Cencini   | Martin        | O'Donnell        | CA                  |
| Mariya     | Sergienko | Francisco     | Perez-Olaeta     | CA                  |
| Mariya     | Sergienko | Francisco     | Perez-Olaeta     | CA                  |
| Mariya     | Sergienko | Francisco     | Perez-Olaeta     | CA                  |
| Mariya     | Sergienko | Francisco     | Perez-Olaeta     | CA                  |
| Mariya     | Sergienko | Francisco     | Perez-Olaeta     | CA                  |
| Mariya     | Sergienko | Francisco     | Perez-Olaeta     | CA                  |
| Mariya     | Sergienko | Francisco     | Perez-Olaeta     | CA                  |
| Mariya     | Sergienko | Francisco     | Perez-Olaeta     | CA                  |
| Mariya     | Sergienko | Francisco     | Perez-Olaeta     | CA                  |
| Mariya     | Sergienko | Francisco     | Perez-Olaeta     | CA                  |
| Andrew     | Cencini   | Francisco     | Perez-Olaeta     | CA                  |
| Andrew     | Cencini   | Francisco     | Perez-Olaeta     | CA                  |
| Andrew     | Cencini   | Francisco     | Perez-Olaeta     | CA                  |
| Andrew     | Cencini   | Francisco     | Perez-Olaeta     | CA                  |
| Andrew     | Cencini   | Francisco     | Perez-Olaeta     | CA                  |
| Mariya     | Sergienko | Ming-Yang     | Xie              | CA                  |
| Mariya     | Sergienko | Ming-Yang     | Xie              | CA                  |
| Mariya     | Sergienko | Ming-Yang     | Xie              | CA                  |
| Mariya     | Sergienko | Ming-Yang     | Xie              | CA                  |
| Mariya     | Sergienko | Ming-Yang     | Xie              | CA                  |
| Mariya     | Sergienko | Ming-Yang     | Xie              | CA                  |
| Mariya     | Sergienko | Ming-Yang     | Xie              | CA                  |
| Mariya     | Sergienko | Ming-Yang     | Xie              | CA                  |
| Mariya     | Sergienko | Ming-Yang     | Xie              | CA                  |
| Mariya     | Sergienko | Ming-Yang     | Xie              | CA                  |
| Andrew     | Cencini   | Ming-Yang     | Xie              | CA                  |
| Andrew     | Cencini   | Ming-Yang     | Xie              | CA                  |
| Andrew     | Cencini   | Ming-Yang     | Xie              | CA                  |
| Andrew     | Cencini   | Ming-Yang     | Xie              | CA                  |
| Andrew     | Cencini   | Ming-Yang     | Xie              | CA                  |
| Mariya     | Sergienko | Elizabeth     | Andersen         | CA                  |
| Mariya     | Sergienko | Elizabeth     | Andersen         | CA                  |
| Mariya     | Sergienko | Elizabeth     | Andersen         | CA                  |
| Mariya     | Sergienko | Elizabeth     | Andersen         | CA                  |
| Mariya     | Sergienko | Elizabeth     | Andersen         | CA                  |
| Mariya     | Sergienko | Elizabeth     | Andersen         | CA                  |
| Mariya     | Sergienko | Elizabeth     | Andersen         | CA                  |
| Mariya     | Sergienko | Elizabeth     | Andersen         | CA                  |
| Mariya     | Sergienko | Elizabeth     | Andersen         | CA                  |
| Mariya     | Sergienko | Elizabeth     | Andersen         | CA                  |
| Andrew     | Cencini   | Elizabeth     | Andersen         | CA                  |
| Andrew     | Cencini   | Elizabeth     | Andersen         | CA                  |
| Andrew     | Cencini   | Elizabeth     | Andersen         | CA                  |
| Andrew     | Cencini   | Elizabeth     | Andersen         | CA                  |
| Andrew     | Cencini   | Elizabeth     | Andersen         | CA                  |
| Mariya     | Sergienko | Sven          | Mortensen        | CA                  |
| Mariya     | Sergienko | Sven          | Mortensen        | CA                  |
| Mariya     | Sergienko | Sven          | Mortensen        | CA                  |
| Mariya     | Sergienko | Sven          | Mortensen        | CA                  |
| Mariya     | Sergienko | Sven          | Mortensen        | CA                  |
| Mariya     | Sergienko | Sven          | Mortensen        | CA                  |
| Mariya     | Sergienko | Sven          | Mortensen        | CA                  |
| Mariya     | Sergienko | Sven          | Mortensen        | CA                  |
| Mariya     | Sergienko | Sven          | Mortensen        | CA                  |
| Mariya     | Sergienko | Sven          | Mortensen        | CA                  |
| Andrew     | Cencini   | Sven          | Mortensen        | CA                  |
| Andrew     | Cencini   | Sven          | Mortensen        | CA                  |
| Andrew     | Cencini   | Sven          | Mortensen        | CA                  |
| Andrew     | Cencini   | Sven          | Mortensen        | CA                  |
| Andrew     | Cencini   | Sven          | Mortensen        | CA                  |
| Mariya     | Sergienko | Roland        | Wacker           | CA                  |
| Mariya     | Sergienko | Roland        | Wacker           | CA                  |
| Mariya     | Sergienko | Roland        | Wacker           | CA                  |
| Mariya     | Sergienko | Roland        | Wacker           | CA                  |
| Mariya     | Sergienko | Roland        | Wacker           | CA                  |
| Mariya     | Sergienko | Roland        | Wacker           | CA                  |
| Mariya     | Sergienko | Roland        | Wacker           | CA                  |
| Mariya     | Sergienko | Roland        | Wacker           | CA                  |
| Mariya     | Sergienko | Roland        | Wacker           | CA                  |
| Mariya     | Sergienko | Roland        | Wacker           | CA                  |
| Andrew     | Cencini   | Roland        | Wacker           | CA                  |
| Andrew     | Cencini   | Roland        | Wacker           | CA                  |
| Andrew     | Cencini   | Roland        | Wacker           | CA                  |
| Andrew     | Cencini   | Roland        | Wacker           | CA                  |
| Andrew     | Cencini   | Roland        | Wacker           | CA                  |
| Mariya     | Sergienko | Peter         | Krschne          | CA                  |
| Mariya     | Sergienko | Peter         | Krschne          | CA                  |
| Mariya     | Sergienko | Peter         | Krschne          | CA                  |
| Mariya     | Sergienko | Peter         | Krschne          | CA                  |
| Mariya     | Sergienko | Peter         | Krschne          | CA                  |
| Mariya     | Sergienko | Peter         | Krschne          | CA                  |
| Mariya     | Sergienko | Peter         | Krschne          | CA                  |
| Mariya     | Sergienko | Peter         | Krschne          | CA                  |
| Mariya     | Sergienko | Peter         | Krschne          | CA                  |
| Mariya     | Sergienko | Peter         | Krschne          | CA                  |
| Andrew     | Cencini   | Peter         | Krschne          | CA                  |
| Andrew     | Cencini   | Peter         | Krschne          | CA                  |
| Andrew     | Cencini   | Peter         | Krschne          | CA                  |
| Andrew     | Cencini   | Peter         | Krschne          | CA                  |
| Andrew     | Cencini   | Peter         | Krschne          | CA                  |
| Mariya     | Sergienko | John          | Edwards          | CA                  |
| Mariya     | Sergienko | John          | Edwards          | CA                  |
| Mariya     | Sergienko | John          | Edwards          | CA                  |
| Mariya     | Sergienko | John          | Edwards          | CA                  |
| Mariya     | Sergienko | John          | Edwards          | CA                  |
| Mariya     | Sergienko | John          | Edwards          | CA                  |
| Mariya     | Sergienko | John          | Edwards          | CA                  |
| Mariya     | Sergienko | John          | Edwards          | CA                  |
| Mariya     | Sergienko | John          | Edwards          | CA                  |
| Mariya     | Sergienko | John          | Edwards          | CA                  |
| Andrew     | Cencini   | John          | Edwards          | CA                  |
| Andrew     | Cencini   | John          | Edwards          | CA                  |
| Andrew     | Cencini   | John          | Edwards          | CA                  |
| Andrew     | Cencini   | John          | Edwards          | CA                  |
| Andrew     | Cencini   | John          | Edwards          | CA                  |
| Mariya     | Sergienko | Andre         | Ludick           | CA                  |
| Mariya     | Sergienko | Andre         | Ludick           | CA                  |
| Mariya     | Sergienko | Andre         | Ludick           | CA                  |
| Mariya     | Sergienko | Andre         | Ludick           | CA                  |
| Mariya     | Sergienko | Andre         | Ludick           | CA                  |
| Mariya     | Sergienko | Andre         | Ludick           | CA                  |
| Mariya     | Sergienko | Andre         | Ludick           | CA                  |
| Mariya     | Sergienko | Andre         | Ludick           | CA                  |
| Mariya     | Sergienko | Andre         | Ludick           | CA                  |
| Mariya     | Sergienko | Andre         | Ludick           | CA                  |
| Andrew     | Cencini   | Andre         | Ludick           | CA                  |
| Andrew     | Cencini   | Andre         | Ludick           | CA                  |
| Andrew     | Cencini   | Andre         | Ludick           | CA                  |
| Andrew     | Cencini   | Andre         | Ludick           | CA                  |
| Andrew     | Cencini   | Andre         | Ludick           | CA                  |
| Mariya     | Sergienko | Carlos        | Grilo            | CA                  |
| Mariya     | Sergienko | Carlos        | Grilo            | CA                  |
| Mariya     | Sergienko | Carlos        | Grilo            | CA                  |
| Mariya     | Sergienko | Carlos        | Grilo            | CA                  |
| Mariya     | Sergienko | Carlos        | Grilo            | CA                  |
| Mariya     | Sergienko | Carlos        | Grilo            | CA                  |
| Mariya     | Sergienko | Carlos        | Grilo            | CA                  |
| Mariya     | Sergienko | Carlos        | Grilo            | CA                  |
| Mariya     | Sergienko | Carlos        | Grilo            | CA                  |
| Mariya     | Sergienko | Carlos        | Grilo            | CA                  |
| Andrew     | Cencini   | Carlos        | Grilo            | CA                  |
| Andrew     | Cencini   | Carlos        | Grilo            | CA                  |
| Andrew     | Cencini   | Carlos        | Grilo            | CA                  |
| Andrew     | Cencini   | Carlos        | Grilo            | CA                  |
| Andrew     | Cencini   | Carlos        | Grilo            | CA                  |
| Mariya     | Sergienko | Helena        | Kupkova          | CA                  |
| Mariya     | Sergienko | Helena        | Kupkova          | CA                  |
| Mariya     | Sergienko | Helena        | Kupkova          | CA                  |
| Mariya     | Sergienko | Helena        | Kupkova          | CA                  |
| Mariya     | Sergienko | Helena        | Kupkova          | CA                  |
| Mariya     | Sergienko | Helena        | Kupkova          | CA                  |
| Mariya     | Sergienko | Helena        | Kupkova          | CA                  |
| Mariya     | Sergienko | Helena        | Kupkova          | CA                  |
| Mariya     | Sergienko | Helena        | Kupkova          | CA                  |
| Mariya     | Sergienko | Helena        | Kupkova          | CA                  |
| Andrew     | Cencini   | Helena        | Kupkova          | CA                  |
| Andrew     | Cencini   | Helena        | Kupkova          | CA                  |
| Andrew     | Cencini   | Helena        | Kupkova          | CA                  |
| Andrew     | Cencini   | Helena        | Kupkova          | CA                  |
| Andrew     | Cencini   | Helena        | Kupkova          | CA                  |
| Mariya     | Sergienko | Daniel        | Goldschmidt      | CA                  |
| Mariya     | Sergienko | Daniel        | Goldschmidt      | CA                  |
| Mariya     | Sergienko | Daniel        | Goldschmidt      | CA                  |
| Mariya     | Sergienko | Daniel        | Goldschmidt      | CA                  |
| Mariya     | Sergienko | Daniel        | Goldschmidt      | CA                  |
| Mariya     | Sergienko | Daniel        | Goldschmidt      | CA                  |
| Mariya     | Sergienko | Daniel        | Goldschmidt      | CA                  |
| Mariya     | Sergienko | Daniel        | Goldschmidt      | CA                  |
| Mariya     | Sergienko | Daniel        | Goldschmidt      | CA                  |
| Mariya     | Sergienko | Daniel        | Goldschmidt      | CA                  |
| Andrew     | Cencini   | Daniel        | Goldschmidt      | CA                  |
| Andrew     | Cencini   | Daniel        | Goldschmidt      | CA                  |
| Andrew     | Cencini   | Daniel        | Goldschmidt      | CA                  |
| Andrew     | Cencini   | Daniel        | Goldschmidt      | CA                  |
| Andrew     | Cencini   | Daniel        | Goldschmidt      | CA                  |
| Mariya     | Sergienko | Jean Philippe | Bagel            | CA                  |
| Mariya     | Sergienko | Jean Philippe | Bagel            | CA                  |
| Mariya     | Sergienko | Jean Philippe | Bagel            | CA                  |
| Mariya     | Sergienko | Jean Philippe | Bagel            | CA                  |
| Mariya     | Sergienko | Jean Philippe | Bagel            | CA                  |
| Mariya     | Sergienko | Jean Philippe | Bagel            | CA                  |
| Mariya     | Sergienko | Jean Philippe | Bagel            | CA                  |
| Mariya     | Sergienko | Jean Philippe | Bagel            | CA                  |
| Mariya     | Sergienko | Jean Philippe | Bagel            | CA                  |
| Mariya     | Sergienko | Jean Philippe | Bagel            | CA                  |
| Andrew     | Cencini   | Jean Philippe | Bagel            | CA                  |
| Andrew     | Cencini   | Jean Philippe | Bagel            | CA                  |
| Andrew     | Cencini   | Jean Philippe | Bagel            | CA                  |
| Andrew     | Cencini   | Jean Philippe | Bagel            | CA                  |
| Andrew     | Cencini   | Jean Philippe | Bagel            | CA                  |
| Mariya     | Sergienko | Catherine     | Autier Miconi    | CA                  |
| Mariya     | Sergienko | Catherine     | Autier Miconi    | CA                  |
| Mariya     | Sergienko | Catherine     | Autier Miconi    | CA                  |
| Mariya     | Sergienko | Catherine     | Autier Miconi    | CA                  |
| Mariya     | Sergienko | Catherine     | Autier Miconi    | CA                  |
| Mariya     | Sergienko | Catherine     | Autier Miconi    | CA                  |
| Mariya     | Sergienko | Catherine     | Autier Miconi    | CA                  |
| Mariya     | Sergienko | Catherine     | Autier Miconi    | CA                  |
| Mariya     | Sergienko | Catherine     | Autier Miconi    | CA                  |
| Mariya     | Sergienko | Catherine     | Autier Miconi    | CA                  |
| Andrew     | Cencini   | Catherine     | Autier Miconi    | CA                  |
| Andrew     | Cencini   | Catherine     | Autier Miconi    | CA                  |
| Andrew     | Cencini   | Catherine     | Autier Miconi    | CA                  |
| Andrew     | Cencini   | Catherine     | Autier Miconi    | CA                  |
| Andrew     | Cencini   | Catherine     | Autier Miconi    | CA                  |
| Mariya     | Sergienko | Alexander     | Eggerer          | CA                  |
| Mariya     | Sergienko | Alexander     | Eggerer          | CA                  |
| Mariya     | Sergienko | Alexander     | Eggerer          | CA                  |
| Mariya     | Sergienko | Alexander     | Eggerer          | CA                  |
| Mariya     | Sergienko | Alexander     | Eggerer          | CA                  |
| Mariya     | Sergienko | Alexander     | Eggerer          | CA                  |
| Mariya     | Sergienko | Alexander     | Eggerer          | CA                  |
| Mariya     | Sergienko | Alexander     | Eggerer          | CA                  |
| Mariya     | Sergienko | Alexander     | Eggerer          | CA                  |
| Mariya     | Sergienko | Alexander     | Eggerer          | CA                  |
| Andrew     | Cencini   | Alexander     | Eggerer          | CA                  |
| Andrew     | Cencini   | Alexander     | Eggerer          | CA                  |
| Andrew     | Cencini   | Alexander     | Eggerer          | CA                  |
| Andrew     | Cencini   | Alexander     | Eggerer          | CA                  |
| Andrew     | Cencini   | Alexander     | Eggerer          | CA                  |
| Mariya     | Sergienko | George        | Li               | CA                  |
| Mariya     | Sergienko | George        | Li               | CA                  |
| Mariya     | Sergienko | George        | Li               | CA                  |
| Mariya     | Sergienko | George        | Li               | CA                  |
| Mariya     | Sergienko | George        | Li               | CA                  |
| Mariya     | Sergienko | George        | Li               | CA                  |
| Mariya     | Sergienko | George        | Li               | CA                  |
| Mariya     | Sergienko | George        | Li               | CA                  |
| Mariya     | Sergienko | George        | Li               | CA                  |
| Mariya     | Sergienko | George        | Li               | CA                  |
| Andrew     | Cencini   | George        | Li               | CA                  |
| Andrew     | Cencini   | George        | Li               | CA                  |
| Andrew     | Cencini   | George        | Li               | CA                  |
| Andrew     | Cencini   | George        | Li               | CA                  |
| Andrew     | Cencini   | George        | Li               | CA                  |
| Mariya     | Sergienko | Bernard       | Tham             | CA                  |
| Mariya     | Sergienko | Bernard       | Tham             | CA                  |
| Mariya     | Sergienko | Bernard       | Tham             | CA                  |
| Mariya     | Sergienko | Bernard       | Tham             | CA                  |
| Mariya     | Sergienko | Bernard       | Tham             | CA                  |
| Mariya     | Sergienko | Bernard       | Tham             | CA                  |
| Mariya     | Sergienko | Bernard       | Tham             | CA                  |
| Mariya     | Sergienko | Bernard       | Tham             | CA                  |
| Mariya     | Sergienko | Bernard       | Tham             | CA                  |
| Mariya     | Sergienko | Bernard       | Tham             | CA                  |
| Andrew     | Cencini   | Bernard       | Tham             | CA                  |
| Andrew     | Cencini   | Bernard       | Tham             | CA                  |
| Andrew     | Cencini   | Bernard       | Tham             | CA                  |
| Andrew     | Cencini   | Bernard       | Tham             | CA                  |
| Andrew     | Cencini   | Bernard       | Tham             | CA                  |
| Mariya     | Sergienko | Luciana       | Ramos            | CA                  |
| Mariya     | Sergienko | Luciana       | Ramos            | CA                  |
| Mariya     | Sergienko | Luciana       | Ramos            | CA                  |
| Mariya     | Sergienko | Luciana       | Ramos            | CA                  |
| Mariya     | Sergienko | Luciana       | Ramos            | CA                  |
| Mariya     | Sergienko | Luciana       | Ramos            | CA                  |
| Mariya     | Sergienko | Luciana       | Ramos            | CA                  |
| Mariya     | Sergienko | Luciana       | Ramos            | CA                  |
| Mariya     | Sergienko | Luciana       | Ramos            | CA                  |
| Mariya     | Sergienko | Luciana       | Ramos            | CA                  |
| Andrew     | Cencini   | Luciana       | Ramos            | CA                  |
| Andrew     | Cencini   | Luciana       | Ramos            | CA                  |
| Andrew     | Cencini   | Luciana       | Ramos            | CA                  |
| Andrew     | Cencini   | Luciana       | Ramos            | CA                  |
| Andrew     | Cencini   | Luciana       | Ramos            | CA                  |
| Mariya     | Sergienko | Michael       | Entin            | CA                  |
| Mariya     | Sergienko | Michael       | Entin            | CA                  |
| Mariya     | Sergienko | Michael       | Entin            | CA                  |
| Mariya     | Sergienko | Michael       | Entin            | CA                  |
| Mariya     | Sergienko | Michael       | Entin            | CA                  |
| Mariya     | Sergienko | Michael       | Entin            | CA                  |
| Mariya     | Sergienko | Michael       | Entin            | CA                  |
| Mariya     | Sergienko | Michael       | Entin            | CA                  |
| Mariya     | Sergienko | Michael       | Entin            | CA                  |
| Mariya     | Sergienko | Michael       | Entin            | CA                  |
| Andrew     | Cencini   | Michael       | Entin            | CA                  |
| Andrew     | Cencini   | Michael       | Entin            | CA                  |
| Andrew     | Cencini   | Michael       | Entin            | CA                  |
| Andrew     | Cencini   | Michael       | Entin            | CA                  |
| Andrew     | Cencini   | Michael       | Entin            | CA                  |
| Mariya     | Sergienko | Jonas         | Hasselberg       | CA                  |
| Mariya     | Sergienko | Jonas         | Hasselberg       | CA                  |
| Mariya     | Sergienko | Jonas         | Hasselberg       | CA                  |
| Mariya     | Sergienko | Jonas         | Hasselberg       | CA                  |
| Mariya     | Sergienko | Jonas         | Hasselberg       | CA                  |
| Mariya     | Sergienko | Jonas         | Hasselberg       | CA                  |
| Mariya     | Sergienko | Jonas         | Hasselberg       | CA                  |
| Mariya     | Sergienko | Jonas         | Hasselberg       | CA                  |
| Mariya     | Sergienko | Jonas         | Hasselberg       | CA                  |
| Mariya     | Sergienko | Jonas         | Hasselberg       | CA                  |
| Andrew     | Cencini   | Jonas         | Hasselberg       | CA                  |
| Andrew     | Cencini   | Jonas         | Hasselberg       | CA                  |
| Andrew     | Cencini   | Jonas         | Hasselberg       | CA                  |
| Andrew     | Cencini   | Jonas         | Hasselberg       | CA                  |
| Andrew     | Cencini   | Jonas         | Hasselberg       | CA                  |
| Mariya     | Sergienko | John          | Rodman           | CA                  |
| Mariya     | Sergienko | John          | Rodman           | CA                  |
| Mariya     | Sergienko | John          | Rodman           | CA                  |
| Mariya     | Sergienko | John          | Rodman           | CA                  |
| Mariya     | Sergienko | John          | Rodman           | CA                  |
| Mariya     | Sergienko | John          | Rodman           | CA                  |
| Mariya     | Sergienko | John          | Rodman           | CA                  |
| Mariya     | Sergienko | John          | Rodman           | CA                  |
| Mariya     | Sergienko | John          | Rodman           | CA                  |
| Mariya     | Sergienko | John          | Rodman           | CA                  |
| Andrew     | Cencini   | John          | Rodman           | CA                  |
| Andrew     | Cencini   | John          | Rodman           | CA                  |
| Andrew     | Cencini   | John          | Rodman           | CA                  |
| Andrew     | Cencini   | John          | Rodman           | CA                  |
| Andrew     | Cencini   | John          | Rodman           | CA                  |
| Mariya     | Sergienko | Run           | Liu              | CA                  |
| Mariya     | Sergienko | Run           | Liu              | CA                  |
| Mariya     | Sergienko | Run           | Liu              | CA                  |
| Mariya     | Sergienko | Run           | Liu              | CA                  |
| Mariya     | Sergienko | Run           | Liu              | CA                  |
| Mariya     | Sergienko | Run           | Liu              | CA                  |
| Mariya     | Sergienko | Run           | Liu              | CA                  |
| Mariya     | Sergienko | Run           | Liu              | CA                  |
| Mariya     | Sergienko | Run           | Liu              | CA                  |
| Mariya     | Sergienko | Run           | Liu              | CA                  |
| Andrew     | Cencini   | Run           | Liu              | CA                  |
| Andrew     | Cencini   | Run           | Liu              | CA                  |
| Andrew     | Cencini   | Run           | Liu              | CA                  |
| Andrew     | Cencini   | Run           | Liu              | CA                  |
| Andrew     | Cencini   | Run           | Liu              | CA                  |
| Mariya     | Sergienko | Karen         | Toh              | CA                  |
| Mariya     | Sergienko | Karen         | Toh              | CA                  |
| Mariya     | Sergienko | Karen         | Toh              | CA                  |
| Mariya     | Sergienko | Karen         | Toh              | CA                  |
| Mariya     | Sergienko | Karen         | Toh              | CA                  |
| Mariya     | Sergienko | Karen         | Toh              | CA                  |
| Mariya     | Sergienko | Karen         | Toh              | CA                  |
| Mariya     | Sergienko | Karen         | Toh              | CA                  |
| Mariya     | Sergienko | Karen         | Toh              | CA                  |
| Mariya     | Sergienko | Karen         | Toh              | CA                  |
| Andrew     | Cencini   | Karen         | Toh              | CA                  |
| Andrew     | Cencini   | Karen         | Toh              | CA                  |
| Andrew     | Cencini   | Karen         | Toh              | CA                  |
| Andrew     | Cencini   | Karen         | Toh              | CA                  |
| Andrew     | Cencini   | Karen         | Toh              | CA                  |
| Mariya     | Sergienko | Amritansh     | Raghav           | CA                  |
| Mariya     | Sergienko | Amritansh     | Raghav           | CA                  |
| Mariya     | Sergienko | Amritansh     | Raghav           | CA                  |
| Mariya     | Sergienko | Amritansh     | Raghav           | CA                  |
| Mariya     | Sergienko | Amritansh     | Raghav           | CA                  |
| Mariya     | Sergienko | Amritansh     | Raghav           | CA                  |
| Mariya     | Sergienko | Amritansh     | Raghav           | CA                  |
| Mariya     | Sergienko | Amritansh     | Raghav           | CA                  |
| Mariya     | Sergienko | Amritansh     | Raghav           | CA                  |
| Mariya     | Sergienko | Amritansh     | Raghav           | CA                  |
| Andrew     | Cencini   | Amritansh     | Raghav           | CA                  |
| Andrew     | Cencini   | Amritansh     | Raghav           | CA                  |
| Andrew     | Cencini   | Amritansh     | Raghav           | CA                  |
| Andrew     | Cencini   | Amritansh     | Raghav           | CA                  |
| Andrew     | Cencini   | Amritansh     | Raghav           | CA                  |
| Mariya     | Sergienko | Soo Jung      | Lee              | CA                  |
| Mariya     | Sergienko | Soo Jung      | Lee              | CA                  |
| Mariya     | Sergienko | Soo Jung      | Lee              | CA                  |
| Mariya     | Sergienko | Soo Jung      | Lee              | CA                  |
| Mariya     | Sergienko | Soo Jung      | Lee              | CA                  |
| Mariya     | Sergienko | Soo Jung      | Lee              | CA                  |
| Mariya     | Sergienko | Soo Jung      | Lee              | CA                  |
| Mariya     | Sergienko | Soo Jung      | Lee              | CA                  |
| Mariya     | Sergienko | Soo Jung      | Lee              | CA                  |
| Mariya     | Sergienko | Soo Jung      | Lee              | CA                  |
| Andrew     | Cencini   | Soo Jung      | Lee              | CA                  |
| Andrew     | Cencini   | Soo Jung      | Lee              | CA                  |
| Andrew     | Cencini   | Soo Jung      | Lee              | CA                  |
| Andrew     | Cencini   | Soo Jung      | Lee              | CA                  |
| Andrew     | Cencini   | Soo Jung      | Lee              | CA                  |
+------------+-----------+---------------+------------------+---------------------+
"""
#what am i actually doing???

#i counted orders and employees and customers... and yeah, there are more orders.
#that seems normal... so why are so few showing up on the first one???


