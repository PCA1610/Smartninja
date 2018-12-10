print "Mit diesem Programm kann man Kilometer in Meilen umrechnen."

question = 0

while True:
    userZahl = int(raw_input("Gib eine Entfernung in Kilometer ein, die du in Meilen umrechnen willst: "))

    userZahlinMeilen = userZahl / 1.609

    print str(userZahl) + " sind " + str(userZahlinMeilen) + " in Meilen."

    choice = raw_input("Would you like to do another conversion (y/n): ")

    if choice.lower() != "y" and choice.lower() != "yes":
        break
