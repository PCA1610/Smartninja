import random
import json


country_capital_dict = {"Slovenia" : "Ljublijana", "Austria" : "Vienna", "Czech" : "Prag", "Germany" : "Berlin"}

try:
    countries = open("countries2.jason", "w+")
    countries.write(json.dumps(country_capital_dict))
except:
    print "Konnte nicht geladen werden"
finally:
    countries.close


rand_value = random.randint(0, 3)

print ("Hey, Nice to see you at the awsome country quiz!")

select_country = country_capital_dict.keys()[rand_value]
user_input = raw_input("Do you know the capital of %s? " % select_country)
