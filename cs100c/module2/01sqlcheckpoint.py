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
#you use... bacticks!!! for things like table names & attributes!!!
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
