print "What is today's menu?"

menu_dict = {}

while True:
    todaymenu = raw_input("Please enter today's menu: ")
    price = raw_input("Was is the price of today's menu?: ")
    print "Today's menu is: " + todaymenu

    menu_dict[todaymenu] = price  # this is how we add a key-value pair into a dict

    new = raw_input("Would you like to enter a new menu? (yes/no) ")

    if new == "no":
        break

menu_file = open("menu.txt", "w+")  # open the TXT file (or create a new one)

print "This was your last menu: %s" % menu_dict
menu_file.write("Today's menu:\n")  # write into the TXT file

menu_file.write("Menu: " + todaymenu + " " + "Price: " + price + "\n")  # add task into the TXT file

menu_file.write("\n")

menu_file.close()  # close the TXT file

print "END"
