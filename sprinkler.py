#******************************************************************************
# sprinkler.py
#******************************************************************************
# Name: Mohmmad Parvez
#******************************************************************************
# Collaborators/outside sources used 
#(IMPORTANT! Write "NONE" if none were used):
#
#
#
# Reminder: you are to write your own code.
#******************************************************************************
# Overall notes (not to replace inline comments):
#
#
# 
# 

import math


w = float(input("Enter width (in ft): "))
l = float(input("Enter length (in ft): "))

yd_area = (w * l)
irrigation = (yd_area  * 0.8)

sprinklers =(irrigation / 155)

spr = math.ceil(sprinklers)


gallons_per_minute = (spr * 3.11)

gallons_per_day = (gallons_per_minute * 15)

gallons_per_month = (gallons_per_day * 30)

cost_per_gallon = (4.49 / 748)

cost_per_month = (cost_per_gallon * gallons_per_month)



print("You have",yd_area, "square feet of yard area and",irrigation,"square feet for irrigation." )
print("You will need", spr, "sprinklers in your yard.")
print("It will use about", gallons_per_minute, "gallons per minute when running.")
print(f"Your bill will be about ${cost_per_month:.2f} per month.")

#CODE IS NOT DONE CHECK FORMATTING FOR LINE ISSUES AND THE DOLLAR SIGN AND SPACING AS WELL
#DONT FORGET TO WRITE COMMENTS FOR EACH BLOCK OF CODE


