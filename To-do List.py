# Lets work with lists in this exercise, this example is a simple to do list that already start with basic tasks, more tasks can be added, tasks can be removed.
# For this exercise I did not use a template or a tutorial, tried to make it myself
# Result in the end of the code
To_do = ["Make bed", "Open courtains", "Make coffee"]

# Lets print the list so we know our starting point
# If we just use the print function we will get an ugly raw list
print("Example of how a list looks like without the proper format:")
print(To_do)
print ()
# But if our command contains a * before the list name and the , sep="\n" after it, it will print a nice line by line list
print("Example of how we want a list to look like:")
print(*To_do, sep="\n")
print()

# Now lets say we want to make this dynamic, asking if something is to be added to or removed from our list
initial_question = str(input("To add someting to the list, please input ADD. To remove something from the list, please input REMOVE "))

to_add = "ADD" or "add" or "Add"
to_remove = "REMOVE" or "remove" or "Remove"

# If something is to be added
if initial_question == to_add:
  new_element = str(input("What do you want to add to the list? "))
  print(new_element)

  To_do.append(new_element)
  print()
  print(*To_do, sep="\n")
  print()

# If something is to be removed
else:
  remove_element = str(input("What do you want to remove from the list? "))

  To_do.remove(remove_element)
  print()
  print(*To_do, sep="\n")
  print()

initial_question = str(input("To add someting to the list, please input ADD. To remove something from the list, please input REMOVE "))

# EXERCISE FAILED
# NEED HELP WITH MAKING IT LOOP, I CAN ONLY ADD ONCE, ALTHOUGH I GET THE MENU AGAIN
