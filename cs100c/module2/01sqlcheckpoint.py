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

#checkpoint

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
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
|                                                   0 |
+-----------------------------------------------------+
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
| Northwind Traders Beer                   | 10.50         | 14.00      |
| Northwind Traders Crab Meat              | 13.80         | 18.40      |
| Northwind Traders Clam Chowder           | 7.24          | 9.65       |
| Northwind Traders Chocolate              | 9.56          | 12.75      |
| Northwind Traders Long Grain Rice        | 5.25          | 7.00       |
| Northwind Traders Ravioli                | 14.63         | 19.50      |
| Northwind Traders Tomato Sauce           | 12.75         | 17.00      |
| Northwind Traders Almonds                | 7.50          | 10.00      |
| Northwind Traders Mustard                | 9.75          | 13.00      |
| Northwind Traders Dried Plums            | 3.00          | 3.50       |
| Northwind Traders Green Tea              | 2.00          | 2.99       |
| Northwind Traders Granola                | 2.00          | 4.00       |
| Northwind Traders Potato Chips           | 0.50          | 1.80       |
| Northwind Traders Brownie Mix            | 9.00          | 12.49      |
| Northwind Traders Cake Mix               | 10.50         | 15.99      |
| Northwind Traders Tea                    | 2.00          | 4.00       |
| Northwind Traders Pears                  | 1.00          | 1.30       |
| Northwind Traders Peaches                | 1.00          | 1.50       |
| Northwind Traders Pineapple              | 1.00          | 1.80       |
| Northwind Traders Cherry Pie Filling     | 1.00          | 2.00       |
| Northwind Traders Green Beans            | 1.00          | 1.20       |
| Northwind Traders Corn                   | 1.00          | 1.20       |
| Northwind Traders Peas                   | 1.00          | 1.50       |
| Northwind Traders Tuna Fish              | 0.50          | 2.00       |
| Northwind Traders Smoked Salmon          | 2.00          | 4.00       |
| Northwind Traders Hot Cereal             | 3.00          | 5.00       |
| Northwind Traders Vegetable Soup         | 1.00          | 1.89       |
| Northwind Traders Chicken Soup           | 1.00          | 1.95       |
| Northwind Traders Chai                   | 13.50         | 18.00      |
| Northwind Traders Syrup                  | 7.50          | 10.00      |
| Northwind Traders Chocolate Biscuits Mix | 6.90          | 9.20       |
| Northwind Traders Scones                 | 7.50          | 10.00      |
| Northwind Traders Beer                   | 10.50         | 14.00      |
| Northwind Traders Crab Meat              | 13.80         | 18.40      |
| Northwind Traders Clam Chowder           | 7.24          | 9.65       |
| Northwind Traders Chocolate              | 9.56          | 12.75      |
| Northwind Traders Long Grain Rice        | 5.25          | 7.00       |
| Northwind Traders Ravioli                | 14.63         | 19.50      |
| Northwind Traders Tomato Sauce           | 12.75         | 17.00      |
| Northwind Traders Almonds                | 7.50          | 10.00      |
| Northwind Traders Mustard                | 9.75          | 13.00      |
| Northwind Traders Dried Plums            | 3.00          | 3.50       |
| Northwind Traders Green Tea              | 2.00          | 2.99       |
| Northwind Traders Granola                | 2.00          | 4.00       |
| Northwind Traders Potato Chips           | 0.50          | 1.80       |
| Northwind Traders Brownie Mix            | 9.00          | 12.49      |
| Northwind Traders Cake Mix               | 10.50         | 15.99      |
| Northwind Traders Tea                    | 2.00          | 4.00       |
| Northwind Traders Pears                  | 1.00          | 1.30       |
| Northwind Traders Peaches                | 1.00          | 1.50       |
| Northwind Traders Pineapple              | 1.00          | 1.80       |
| Northwind Traders Cherry Pie Filling     | 1.00          | 2.00       |
| Northwind Traders Green Beans            | 1.00          | 1.20       |
| Northwind Traders Corn                   | 1.00          | 1.20       |
| Northwind Traders Peas                   | 1.00          | 1.50       |
| Northwind Traders Tuna Fish              | 0.50          | 2.00       |
| Northwind Traders Smoked Salmon          | 2.00          | 4.00       |
| Northwind Traders Hot Cereal             | 3.00          | 5.00       |
| Northwind Traders Vegetable Soup         | 1.00          | 1.89       |
| Northwind Traders Chicken Soup           | 1.00          | 1.95       |
| Northwind Traders Chai                   | 13.50         | 18.00      |
| Northwind Traders Syrup                  | 7.50          | 10.00      |
| Northwind Traders Chocolate Biscuits Mix | 6.90          | 9.20       |
| Northwind Traders Scones                 | 7.50          | 10.00      |
| Northwind Traders Beer                   | 10.50         | 14.00      |
| Northwind Traders Crab Meat              | 13.80         | 18.40      |
| Northwind Traders Clam Chowder           | 7.24          | 9.65       |
| Northwind Traders Chocolate              | 9.56          | 12.75      |
| Northwind Traders Long Grain Rice        | 5.25          | 7.00       |
| Northwind Traders Ravioli                | 14.63         | 19.50      |
| Northwind Traders Tomato Sauce           | 12.75         | 17.00      |
| Northwind Traders Almonds                | 7.50          | 10.00      |
| Northwind Traders Mustard                | 9.75          | 13.00      |
| Northwind Traders Dried Plums            | 3.00          | 3.50       |
| Northwind Traders Green Tea              | 2.00          | 2.99       |
| Northwind Traders Granola                | 2.00          | 4.00       |
| Northwind Traders Potato Chips           | 0.50          | 1.80       |
| Northwind Traders Brownie Mix            | 9.00          | 12.49      |
| Northwind Traders Cake Mix               | 10.50         | 15.99      |
| Northwind Traders Tea                    | 2.00          | 4.00       |
| Northwind Traders Pears                  | 1.00          | 1.30       |
| Northwind Traders Peaches                | 1.00          | 1.50       |
| Northwind Traders Pineapple              | 1.00          | 1.80       |
| Northwind Traders Cherry Pie Filling     | 1.00          | 2.00       |
| Northwind Traders Green Beans            | 1.00          | 1.20       |
| Northwind Traders Corn                   | 1.00          | 1.20       |
| Northwind Traders Peas                   | 1.00          | 1.50       |
| Northwind Traders Tuna Fish              | 0.50          | 2.00       |
| Northwind Traders Smoked Salmon          | 2.00          | 4.00       |
| Northwind Traders Hot Cereal             | 3.00          | 5.00       |
| Northwind Traders Vegetable Soup         | 1.00          | 1.89       |
| Northwind Traders Chicken Soup           | 1.00          | 1.95       |
| Northwind Traders Chai                   | 13.50         | 18.00      |
| Northwind Traders Syrup                  | 7.50          | 10.00      |
| Northwind Traders Chocolate Biscuits Mix | 6.90          | 9.20       |
| Northwind Traders Scones                 | 7.50          | 10.00      |
| Northwind Traders Beer                   | 10.50         | 14.00      |
| Northwind Traders Crab Meat              | 13.80         | 18.40      |
| Northwind Traders Clam Chowder           | 7.24          | 9.65       |
| Northwind Traders Chocolate              | 9.56          | 12.75      |
| Northwind Traders Long Grain Rice        | 5.25          | 7.00       |
| Northwind Traders Ravioli                | 14.63         | 19.50      |
| Northwind Traders Tomato Sauce           | 12.75         | 17.00      |
| Northwind Traders Almonds                | 7.50          | 10.00      |
| Northwind Traders Mustard                | 9.75          | 13.00      |
| Northwind Traders Dried Plums            | 3.00          | 3.50       |
| Northwind Traders Green Tea              | 2.00          | 2.99       |
| Northwind Traders Granola                | 2.00          | 4.00       |
| Northwind Traders Potato Chips           | 0.50          | 1.80       |
| Northwind Traders Brownie Mix            | 9.00          | 12.49      |
| Northwind Traders Cake Mix               | 10.50         | 15.99      |
| Northwind Traders Tea                    | 2.00          | 4.00       |
| Northwind Traders Pears                  | 1.00          | 1.30       |
| Northwind Traders Peaches                | 1.00          | 1.50       |
| Northwind Traders Pineapple              | 1.00          | 1.80       |
| Northwind Traders Cherry Pie Filling     | 1.00          | 2.00       |
| Northwind Traders Green Beans            | 1.00          | 1.20       |
| Northwind Traders Corn                   | 1.00          | 1.20       |
| Northwind Traders Peas                   | 1.00          | 1.50       |
| Northwind Traders Tuna Fish              | 0.50          | 2.00       |
| Northwind Traders Smoked Salmon          | 2.00          | 4.00       |
| Northwind Traders Hot Cereal             | 3.00          | 5.00       |
| Northwind Traders Vegetable Soup         | 1.00          | 1.89       |
| Northwind Traders Chicken Soup           | 1.00          | 1.95       |
| Northwind Traders Chai                   | 13.50         | 18.00      |
| Northwind Traders Syrup                  | 7.50          | 10.00      |
| Northwind Traders Chocolate Biscuits Mix | 6.90          | 9.20       |
| Northwind Traders Scones                 | 7.50          | 10.00      |
| Northwind Traders Beer                   | 10.50         | 14.00      |
| Northwind Traders Crab Meat              | 13.80         | 18.40      |
| Northwind Traders Clam Chowder           | 7.24          | 9.65       |
| Northwind Traders Chocolate              | 9.56          | 12.75      |
| Northwind Traders Long Grain Rice        | 5.25          | 7.00       |
| Northwind Traders Ravioli                | 14.63         | 19.50      |
| Northwind Traders Tomato Sauce           | 12.75         | 17.00      |
| Northwind Traders Almonds                | 7.50          | 10.00      |
| Northwind Traders Mustard                | 9.75          | 13.00      |
| Northwind Traders Dried Plums            | 3.00          | 3.50       |
| Northwind Traders Green Tea              | 2.00          | 2.99       |
| Northwind Traders Granola                | 2.00          | 4.00       |
| Northwind Traders Potato Chips           | 0.50          | 1.80       |
| Northwind Traders Brownie Mix            | 9.00          | 12.49      |
| Northwind Traders Cake Mix               | 10.50         | 15.99      |
| Northwind Traders Tea                    | 2.00          | 4.00       |
| Northwind Traders Pears                  | 1.00          | 1.30       |
| Northwind Traders Peaches                | 1.00          | 1.50       |
| Northwind Traders Pineapple              | 1.00          | 1.80       |
| Northwind Traders Cherry Pie Filling     | 1.00          | 2.00       |
| Northwind Traders Green Beans            | 1.00          | 1.20       |
| Northwind Traders Corn                   | 1.00          | 1.20       |
| Northwind Traders Peas                   | 1.00          | 1.50       |
| Northwind Traders Tuna Fish              | 0.50          | 2.00       |
| Northwind Traders Smoked Salmon          | 2.00          | 4.00       |
| Northwind Traders Hot Cereal             | 3.00          | 5.00       |
| Northwind Traders Vegetable Soup         | 1.00          | 1.89       |
| Northwind Traders Chicken Soup           | 1.00          | 1.95       |
| Northwind Traders Chai                   | 13.50         | 18.00      |
| Northwind Traders Syrup                  | 7.50          | 10.00      |
| Northwind Traders Chocolate Biscuits Mix | 6.90          | 9.20       |
| Northwind Traders Scones                 | 7.50          | 10.00      |
| Northwind Traders Beer                   | 10.50         | 14.00      |
| Northwind Traders Crab Meat              | 13.80         | 18.40      |
| Northwind Traders Clam Chowder           | 7.24          | 9.65       |
| Northwind Traders Chocolate              | 9.56          | 12.75      |
| Northwind Traders Long Grain Rice        | 5.25          | 7.00       |
| Northwind Traders Ravioli                | 14.63         | 19.50      |
| Northwind Traders Tomato Sauce           | 12.75         | 17.00      |
| Northwind Traders Almonds                | 7.50          | 10.00      |
| Northwind Traders Mustard                | 9.75          | 13.00      |
| Northwind Traders Dried Plums            | 3.00          | 3.50       |
| Northwind Traders Green Tea              | 2.00          | 2.99       |
| Northwind Traders Granola                | 2.00          | 4.00       |
| Northwind Traders Potato Chips           | 0.50          | 1.80       |
| Northwind Traders Brownie Mix            | 9.00          | 12.49      |
| Northwind Traders Cake Mix               | 10.50         | 15.99      |
| Northwind Traders Tea                    | 2.00          | 4.00       |
| Northwind Traders Pears                  | 1.00          | 1.30       |
| Northwind Traders Peaches                | 1.00          | 1.50       |
| Northwind Traders Pineapple              | 1.00          | 1.80       |
| Northwind Traders Cherry Pie Filling     | 1.00          | 2.00       |
| Northwind Traders Green Beans            | 1.00          | 1.20       |
| Northwind Traders Corn                   | 1.00          | 1.20       |
| Northwind Traders Peas                   | 1.00          | 1.50       |
| Northwind Traders Tuna Fish              | 0.50          | 2.00       |
| Northwind Traders Smoked Salmon          | 2.00          | 4.00       |
| Northwind Traders Hot Cereal             | 3.00          | 5.00       |
| Northwind Traders Vegetable Soup         | 1.00          | 1.89       |
| Northwind Traders Chicken Soup           | 1.00          | 1.95       |
| Northwind Traders Chai                   | 13.50         | 18.00      |
| Northwind Traders Syrup                  | 7.50          | 10.00      |
| Northwind Traders Chocolate Biscuits Mix | 6.90          | 9.20       |
| Northwind Traders Scones                 | 7.50          | 10.00      |
| Northwind Traders Beer                   | 10.50         | 14.00      |
| Northwind Traders Crab Meat              | 13.80         | 18.40      |
| Northwind Traders Clam Chowder           | 7.24          | 9.65       |
| Northwind Traders Chocolate              | 9.56          | 12.75      |
| Northwind Traders Long Grain Rice        | 5.25          | 7.00       |
| Northwind Traders Ravioli                | 14.63         | 19.50      |
| Northwind Traders Tomato Sauce           | 12.75         | 17.00      |
| Northwind Traders Almonds                | 7.50          | 10.00      |
| Northwind Traders Mustard                | 9.75          | 13.00      |
| Northwind Traders Dried Plums            | 3.00          | 3.50       |
| Northwind Traders Green Tea              | 2.00          | 2.99       |
| Northwind Traders Granola                | 2.00          | 4.00       |
| Northwind Traders Potato Chips           | 0.50          | 1.80       |
| Northwind Traders Brownie Mix            | 9.00          | 12.49      |
| Northwind Traders Cake Mix               | 10.50         | 15.99      |
| Northwind Traders Tea                    | 2.00          | 4.00       |
| Northwind Traders Pears                  | 1.00          | 1.30       |
| Northwind Traders Peaches                | 1.00          | 1.50       |
| Northwind Traders Pineapple              | 1.00          | 1.80       |
| Northwind Traders Cherry Pie Filling     | 1.00          | 2.00       |
| Northwind Traders Green Beans            | 1.00          | 1.20       |
| Northwind Traders Corn                   | 1.00          | 1.20       |
| Northwind Traders Peas                   | 1.00          | 1.50       |
| Northwind Traders Tuna Fish              | 0.50          | 2.00       |
| Northwind Traders Smoked Salmon          | 2.00          | 4.00       |
| Northwind Traders Hot Cereal             | 3.00          | 5.00       |
| Northwind Traders Vegetable Soup         | 1.00          | 1.89       |
| Northwind Traders Chicken Soup           | 1.00          | 1.95       |
| Northwind Traders Chai                   | 13.50         | 18.00      |
| Northwind Traders Syrup                  | 7.50          | 10.00      |
| Northwind Traders Chocolate Biscuits Mix | 6.90          | 9.20       |
| Northwind Traders Scones                 | 7.50          | 10.00      |
| Northwind Traders Beer                   | 10.50         | 14.00      |
| Northwind Traders Crab Meat              | 13.80         | 18.40      |
| Northwind Traders Clam Chowder           | 7.24          | 9.65       |
| Northwind Traders Chocolate              | 9.56          | 12.75      |
| Northwind Traders Long Grain Rice        | 5.25          | 7.00       |
| Northwind Traders Ravioli                | 14.63         | 19.50      |
| Northwind Traders Tomato Sauce           | 12.75         | 17.00      |
| Northwind Traders Almonds                | 7.50          | 10.00      |
| Northwind Traders Mustard                | 9.75          | 13.00      |
| Northwind Traders Dried Plums            | 3.00          | 3.50       |
| Northwind Traders Green Tea              | 2.00          | 2.99       |
| Northwind Traders Granola                | 2.00          | 4.00       |
| Northwind Traders Potato Chips           | 0.50          | 1.80       |
| Northwind Traders Brownie Mix            | 9.00          | 12.49      |
| Northwind Traders Cake Mix               | 10.50         | 15.99      |
| Northwind Traders Tea                    | 2.00          | 4.00       |
| Northwind Traders Pears                  | 1.00          | 1.30       |
| Northwind Traders Peaches                | 1.00          | 1.50       |
| Northwind Traders Pineapple              | 1.00          | 1.80       |
| Northwind Traders Cherry Pie Filling     | 1.00          | 2.00       |
| Northwind Traders Green Beans            | 1.00          | 1.20       |
| Northwind Traders Corn                   | 1.00          | 1.20       |
| Northwind Traders Peas                   | 1.00          | 1.50       |
| Northwind Traders Tuna Fish              | 0.50          | 2.00       |
| Northwind Traders Smoked Salmon          | 2.00          | 4.00       |
| Northwind Traders Hot Cereal             | 3.00          | 5.00       |
| Northwind Traders Vegetable Soup         | 1.00          | 1.89       |
| Northwind Traders Chicken Soup           | 1.00          | 1.95       |
| Northwind Traders Chai                   | 13.50         | 18.00      |
| Northwind Traders Syrup                  | 7.50          | 10.00      |
| Northwind Traders Chocolate Biscuits Mix | 6.90          | 9.20       |
| Northwind Traders Scones                 | 7.50          | 10.00      |
| Northwind Traders Beer                   | 10.50         | 14.00      |
| Northwind Traders Crab Meat              | 13.80         | 18.40      |
| Northwind Traders Clam Chowder           | 7.24          | 9.65       |
| Northwind Traders Chocolate              | 9.56          | 12.75      |
| Northwind Traders Long Grain Rice        | 5.25          | 7.00       |
| Northwind Traders Ravioli                | 14.63         | 19.50      |
| Northwind Traders Tomato Sauce           | 12.75         | 17.00      |
| Northwind Traders Almonds                | 7.50          | 10.00      |
| Northwind Traders Mustard                | 9.75          | 13.00      |
| Northwind Traders Dried Plums            | 3.00          | 3.50       |
| Northwind Traders Green Tea              | 2.00          | 2.99       |
| Northwind Traders Granola                | 2.00          | 4.00       |
| Northwind Traders Potato Chips           | 0.50          | 1.80       |
| Northwind Traders Brownie Mix            | 9.00          | 12.49      |
| Northwind Traders Cake Mix               | 10.50         | 15.99      |
| Northwind Traders Tea                    | 2.00          | 4.00       |
| Northwind Traders Pears                  | 1.00          | 1.30       |
| Northwind Traders Peaches                | 1.00          | 1.50       |
| Northwind Traders Pineapple              | 1.00          | 1.80       |
| Northwind Traders Cherry Pie Filling     | 1.00          | 2.00       |
| Northwind Traders Green Beans            | 1.00          | 1.20       |
| Northwind Traders Corn                   | 1.00          | 1.20       |
| Northwind Traders Peas                   | 1.00          | 1.50       |
| Northwind Traders Tuna Fish              | 0.50          | 2.00       |
| Northwind Traders Smoked Salmon          | 2.00          | 4.00       |
| Northwind Traders Hot Cereal             | 3.00          | 5.00       |
| Northwind Traders Vegetable Soup         | 1.00          | 1.89       |
| Northwind Traders Chicken Soup           | 1.00          | 1.95       |
| Northwind Traders Chai                   | 13.50         | 18.00      |
| Northwind Traders Syrup                  | 7.50          | 10.00      |
| Northwind Traders Chocolate Biscuits Mix | 6.90          | 9.20       |
| Northwind Traders Scones                 | 7.50          | 10.00      |
| Northwind Traders Beer                   | 10.50         | 14.00      |
| Northwind Traders Crab Meat              | 13.80         | 18.40      |
| Northwind Traders Clam Chowder           | 7.24          | 9.65       |
| Northwind Traders Chocolate              | 9.56          | 12.75      |
| Northwind Traders Long Grain Rice        | 5.25          | 7.00       |
| Northwind Traders Ravioli                | 14.63         | 19.50      |
| Northwind Traders Tomato Sauce           | 12.75         | 17.00      |
| Northwind Traders Almonds                | 7.50          | 10.00      |
| Northwind Traders Mustard                | 9.75          | 13.00      |
| Northwind Traders Dried Plums            | 3.00          | 3.50       |
| Northwind Traders Green Tea              | 2.00          | 2.99       |
| Northwind Traders Granola                | 2.00          | 4.00       |
| Northwind Traders Potato Chips           | 0.50          | 1.80       |
| Northwind Traders Brownie Mix            | 9.00          | 12.49      |
| Northwind Traders Cake Mix               | 10.50         | 15.99      |
| Northwind Traders Tea                    | 2.00          | 4.00       |
| Northwind Traders Pears                  | 1.00          | 1.30       |
| Northwind Traders Peaches                | 1.00          | 1.50       |
| Northwind Traders Pineapple              | 1.00          | 1.80       |
| Northwind Traders Cherry Pie Filling     | 1.00          | 2.00       |
| Northwind Traders Green Beans            | 1.00          | 1.20       |
| Northwind Traders Corn                   | 1.00          | 1.20       |
| Northwind Traders Peas                   | 1.00          | 1.50       |
| Northwind Traders Tuna Fish              | 0.50          | 2.00       |
| Northwind Traders Smoked Salmon          | 2.00          | 4.00       |
| Northwind Traders Hot Cereal             | 3.00          | 5.00       |
| Northwind Traders Vegetable Soup         | 1.00          | 1.89       |
| Northwind Traders Chicken Soup           | 1.00          | 1.95       |
+------------------------------------------+---------------+------------+
"""
#well there, that one's working, but i'm still not sure about funky o'donnell