"""
write a program that asks the user for how many
minutes and seconds that is. for instance,200 seconds is 3 minutes and 20 seconds.
hint: use the // operator to get minutes and % operator to get seconds.

"""
seconds = eval(input("enter number of seconds :"))
minutes = seconds // 60
seconds = seconds % 60
print("there is", minutes, "min and ", seconds, "sec")






