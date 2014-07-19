"""Here are your instructions:

Populate your database with "animal" and "food" tables using the tablepop and addfood programs that you wrote during the
lesson (this step will not be necessary if you have not modified the tables since you created them in the lesson).

 Write a program that verifies that every animal eats at least one food.

Your Comment:
All the animals except the newly added one will be fed if you run the addfood.py after the tablepop.py but before 
food_verify.py. """

##################################################################################################################################################

import mysql.connector
from database import login_info
List_animals = []
List_fed = []

db = mysql.connector.Connect(**login_info)
cursor = db.cursor()


cursor.execute("select id from animal")
for id in cursor.fetchall():
    List_animals.append(id[0])    

cursor.execute("select anid from food")
for anid in cursor.fetchall():
    if anid[0] not in List_fed:
        List_fed.append(anid[0])

for x in List_animals:
    if x not in List_fed:
        print ("Animal with ID # %s has not received any food." %x)
        
for value in List_fed:
    if value in List_animals:
        List_animals.remove(value)
    if len(List_animals)==0:
        print ("All animals have eaten at least one food")
