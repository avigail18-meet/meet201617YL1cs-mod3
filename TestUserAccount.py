#This script performs some simple tests on the UserAccount class.
from UserAccount import UserAccount

#Three things are missing from the line below - fill them in
my_user=UserAccount("avigail630" ,"avigail12","wrong")

#Call the print_secret method (function) - it takes one input - a guess for the password.
#Use the wrong password as input here
my_user.print_secret("naim")

#Use the right password here
my_user.print_secret("avigail12")
