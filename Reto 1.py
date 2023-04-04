# Will attempt to perform a homework from Ely that consists in creating a serie of variables of a contact form and then print it

# My assumption is that it consists in creating lists and later printing them

# So lets create a list called Contacts that contain several sub_lists, represented by the "_l"
name_l = ["John", "Jane"]
surname_l = ["Doe", "Due"]
age_l = [23, 25]
email_l = ["john.d@gmail.com", "jane.d@gmail.com"]
tel_l = [938187693, 9287638765]
married_l = ["True", "False"]
children_l = ["False", "True"]
friends_l = ["Jane", "None"]
movies_l = ["The Godfather", "The Godfather II"]

# Now lets print only John Doe information, we could print the first element of each list separatelly, since that is the one referring to John Doe
# Added somethings so it looks pretty
print("This is how the contact info from John Doe looks like:")
print()
print("Name:",(name_l[0]))
print("Surname:",(surname_l[0]))
print("Age:",(age_l[0]))
print("E-mail:",(email_l[0]))
print("Telephone:",(tel_l[0]))
print("Married:",(married_l[0]))
print("Children:",(children_l[0]))
print("Friends:",(friends_l[0]))
print("Movie:",(movies_l[0]))
print()

# But like this the code would be unnecesarily big, instead, for Jane Due, we could first make a list of the lists:
Contacts = [name_l, surname_l, age_l, email_l, tel_l, married_l, children_l, friends_l, movies_l]

# And then create a variable for the position from which we want to retrieve the information of the list of lists. The != means is not equal to, so if C is 0, for the first, or 1 for the second.
for C in Contacts:
   if C != []:
     print(C[1])
print()

# It worked! A few things come into my mind, like adding the list alias like shown in John Doe for Jane Due, but I do not know how to make it within a list of lists.

# Another modification we could make is to change Age for Year of Birth. Age is currently a static interget, we could the age from a simple calculation.

# We would need to import the datetime module to define what year we are in
import datetime

today = datetime.date.today()
year = today.year

print(f"We are in the year",year)
print()

# Then we would need to have a list of Year of Birth, for example
yearbith_l = [1995, 1980]

# Then we would create a new age_l
currentage_l = [(year-yearbith_l[0]), (year-yearbith_l[1])]

# Now lets update our list of lists and print again Jane Due info to see if it worked, her age now should be 43
Contacts = [name_l, surname_l, currentage_l, email_l, tel_l, married_l, children_l, friends_l, movies_l]
for C in Contacts:
   if C != []:
     print(C[1])
print()
