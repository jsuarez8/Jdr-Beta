"""Integration Project"""
__author__ = "Jose Suarez"
# I want to use this code, to make an app on how to
# find exactly what the prices of your iPhone model is and how much the
# total cost of financing the phone comes out to, along with cellular plan,
# and apple care if needed over the amount of months the phone will be
# financed for. Also, breaking down the prices of the most important parts
# in the phone and giving the prices it may be. Here we go!


print("Welcome to the JdrTech Beta! " * 2)
# * used as a multiplication for the string, so it prints the string twice
# in one line
name = input("What is your name? ")
time = input("What time is it? ")
age = input("How old are you? ")


def print_info(user_name, user_age, user_time):
    """
Return the users name, age, and current time where they live.
    :param user_name: Name of the user
    :param user_age: The age of the user
    :param user_time: The current time where the user lives
    :return: name, age, time
    """
    print("Your name is", user_name + "." * 2)
    print("You are", user_age + " years old!")
    print("It is currently", user_time)
    return


print_info(name, age, time)

# added the + ("!") to add it at the end of the string

print("Being the owner of JdrTech, we focus on providing our customers the "
      "best and most efficient service possible.")
print("Let's get started!")

# Device Information

device_type = input("What model iPhone do you own? ")
device_quantity = int(input("Enter how many devices you own: "))
device_memory = int(input("Enter the number of GBs your device contains: "))
device_color = input("What color is your device? ")
device_price = float(input("What was the total cost of your model? $"))
total_cost = device_price * device_quantity
# * used to multiply the values
total_memory = device_memory * device_quantity
print("You own a", device_type)
print("You own", device_quantity)
print("You have an accumulated amount of", str(total_memory) + "GBs in "
                                                               "memory!")
# + function to add the strings together after the user input, str was used
# to make the int total_memory into a string output
print("The color isn't too important, it is just good to know in the case of "
      "switching parts.")
print("The total cost is: $", format(total_cost, "0.2f"), sep='')
# 0.2f is used to display the cost after two decimal places and sep='' is
# used as a separator between the print() function
print("That is a load of money!!")

# Possible carrier plan if the customer has one

device_carrier = input("What carrier do you currently have a plan with? ")
carrier_monthly_price = float(input("Enter how much you finance your phone "
                                    "monthly: $"))
device_quantity2 = int(input("How many phones are you financing with your "
                             "carrier? "))
carrier_monthly_time = int(input("For how many months is this plan active? "))
totals_of_plan1 = carrier_monthly_price*carrier_monthly_time*device_quantity2
# * operation was used to multiply the amount of money each device is
# monthly with how many devices the user has financed multiplied to however
# many months the finance plan is.
totality_month1 = totals_of_plan1 / carrier_monthly_time
# / operation used to display total cost of monthly plan over x amount of
# months
print("You currently have", device_carrier + " as your cellular carrier.")
print("The amount of devices you currently finance is: ", device_quantity2)
print("Your finance plan is currently active for", str(carrier_monthly_time)
      + " months!")
# + was used to add the strings after the user input, str was used to make
# the input a string and add it all together
print("Every month you pay: $", format(totality_month1, "0.2f"), sep='')
print("Once your finance plan is complete, you have paid $",
      format(totals_of_plan1, "0.2f"), sep='')
# 0.2f is used to display the cost after two decimal places and sep='' is
# used for as a separator between the print() function

# Cellular plan cost over the months the finance plan is

cellular_plan = float(input("How much do you pay for your cellular plan "
                            "alongside your phone? $"))
device_quantity3 = int(input("How many devices are on your plan? "))
totality_month2 = cellular_plan * device_quantity3
totality_together = totality_month2 * carrier_monthly_time
totals_of_plan2 = totals_of_plan1 + totality_together
# * operation was used to multiply the total amount of money each device is
# monthly and the amount the cellular plan is after the finance is over
print("The amount of phones that currently have cellular service is:",
      device_quantity3)
print("Your total cost for cellular service per month is $",
      format(totality_month2, "0.2f"), sep='')
print("Your total cost of your cellular bill and monthly phone payments "
      "after your finance plan is complete will be $",
      format(totals_of_plan2, "0.2f"), sep='')
# 0.2f is used to display the cost after two decimal places and sep=''
# function is used as a separator between the print() function

# Adding apple care plan to the phone bill

print("If you have the Apple Care plan for your phone bill then it will be "
      "an additional cost.")
apple_care_cost = float(input("How much do you pay for Apple Care on a "
                              "monthly basis? $"))
device_quantity3 = int(input("How many devices have Apple Care? "))
totality_month3 = apple_care_cost * device_quantity3
totality_together2 = totality_month3 * carrier_monthly_time
totals_of_plan3 = totals_of_plan2 + totality_together2
# * operation was used to multiply the total amount of money each device is,
# how much the user pays for apple care, and the cellular plan after the
# finance is over
print("The amount of iPhones covered by Apple Care is", device_quantity3)
print("Your total cost per month for Apple Care is $",
      format(totality_month3, "0.2f"), sep='')
print("Your total cost of your cellular bill and monthly phone payments once "
      "your finance plan is complete alongside Apple Care will be $",
      format(totals_of_plan3, "0.2f"), sep='')
# 0.2f is used to display the cost after two decimal places and sep='' is
# used for as a separator between the print() function

# How much a battery and charging port costs for a given iPhone

print("Usually around a year and a half after the purchase date of any "
      "iPhone is when batteries start to deteriorate.")
battery_cost = float(input("Enter the price of a new battery for your "
                           "iPhone: $"))
battery_quantity = int(input("How many batteries would "
                             "you like to purchase? "))
print("You may need a new charging port because it could've corroded "
      "internally.")
port_cost = float(input("Enter the cost of a new charging port for your "
                        "iPhone: $"))
port_quantity = int(input("How many charging ports would you like to "
                          "purchase? "))
total_cost_battery = battery_cost * battery_quantity
total_cost_port = port_cost * port_quantity
total_cost_together3 = total_cost_battery * total_cost_port
difference_of_cost1 = abs(total_cost_battery - total_cost_port)
# - operation used to subtract the total amount of batteries the user wants
# and the total amount of charging ports the user wants. The abs function is
# used to take the absolute value of the difference between the prices
# that way the output doesn't print a negative number.
print("Your total for batteries would be $",
      format(total_cost_battery, "0.2f"), sep='')
print("Your total for charging ports would be $",
      format(total_cost_port, "0.2f"), sep='')
print("The total difference in prices between the two item is $",
      format(difference_of_cost1, "0.2f"), sep='')
# this portion of the code is used to display the total difference in price
# between the two items the user wants

# random facts section
month_battery = battery_cost * 4 * 12 // 12
# shows the amount of money to nearest whole number for how much is spend
# when buy 4 batteries every month for a year
month_port = port_cost * 4 * 24 // 24
# shows the amount of money to nearest whole number for how much is spend
# when buy 4 charging ports every month for a 2 year
cents_of_port = port_cost % 1
# shows the remaining change if 1 charging port is purchased
cents_of_battery = battery_cost % 1
print("If you were to order 4 batteries every month for an entire year, "
      "you would spend approximately $", month_battery)
print("If you were to order 4 batteries every month for 2 years, you would "
      "spend approximately $", month_port)
print("If you were to purchase 1 charging port in cash, you would still owe "
      "some cents, that amount is equal to: ",
      format(cents_of_port, "0.2f"), sep='')
print("If you were to purchase 1 battery in cash, you would still owe some "
      "cents, that amount is equal to: ", format(cents_of_battery, "0.2f"),
      sep='')
print("Get to the store prepared!")

# random math quiz
answer1 = (8 ** 6)
# ** getting the exponent of 8 to the power of 6
answer2 = (9 ** 3)
# ** getting the exponent of 9 to the power of 3
answer3 = (2 ** 9)
# ** getting the exponent of 2 to the power of 9
question1 = input("What is 8 to the power of 6? ")
print("The correct answer is: ", answer1)
question2 = input("What is 9 to the power of 3? ")
print("The correct answer is: ", answer2)
question3 = input("What is 2 to the power of 9? ")
print("The correct answer is: ", answer3)


def addition(num1, num2):
    """
Returns the sum of two numbers.
    :param num1: First number
    :param num2: Second number
    """
    answer4 = num1 + num2
    print("If the first number is", num1)
    print("The sum of this number and another number is", answer4)


addition(num1=63, num2=87)
# the parameter function was used to add 63 and 87. The program prints the
# first number and the answer to the addition problem which is 150.
print("Thank you! " * 2)
# * function used as a multiplication for the string, that way it prints the
# string twice in one line.
print("Until next user_time. " * 2)
# * used as a multiplication for the string, that way it prints the string
# twice in one line

# Part 2 Now we will be able to display the cost of iPhone Models without
# the user inputting it this can only display the iPhones that are currently
# on the market from apple or first hand sellers not third party sellers for
# now.

for x in range(3):
    print("Alright, let's keep it going, ", name + "!")
# prints welcome back three times with x in range () function.

bud_1 = input("Are you on a budget? ")
bud_2 = 1
while bud_2 <= 1:
    if (bud_1 == 'yes') or (bud_1 == 'Yes'):
        print("No worries, we can work with anything you throw our way!")
        # wrote "if" statement and included boolean "or" to show, if user
        # inputs yes or Yes then it prints the statement shown.
        bud_2 += 1
    # made a new variable bud_2 as a number so when bud_2 <= 1 it prints the
    # statement "no worries, we can work with anything you throw our way!"
    # only once. Placed it in a while loop so whenever the user answers yes
    # the loop outputs amount_bud only once.
    elif (bud_1 != 'yes') or (bud_1 != 'Yes'):
        print("Perfect!")
    # if user answers "no" or "No", the program prints "Perfect!"
    break  # break here

print("iPhones currently sold on the market are only available in:")
amount_memory1 = ["32 GBs", "64 GBs", "128 GBs", "256 GBs", "512 GBs"]
# made a list that displays the amount of GBs available for iPhones on the
# market right now.
for x in amount_memory1:
    print(x)
# print(x) displays the list to show the amount of memory available for
# iPhones on the market right now.

amount_bud = float(input("What is the max amount of money you can spend on 1 "
                         "iPhone? $")) 
if not amount_bud <= 1600:
    print("Good for you!")
    print("You can afford any iPhone model and a pair of Airpods Pro if you "
          "would like!")
elif amount_bud >= 1400:
    print("Awesome!")
    print("You can afford any of the iPhone models.")
elif not amount_bud < 1200 and amount_bud < 1400:
    print("You can afford:")
    print("iPhone 11 Pro 512GBs, iPhone 11 Pro Max 512 GBs, iPhone 12 Pro "
          "Max 512 GBs, iPhone 12 Pro 512 GBs.")
elif 1000 <= amount_bud < 1200:
    print("You can afford:")
    print("iPhone Xs Max 512 GBs, iPhone 11 Pro 256 GBs, iPhone 11 Pro Max "
          "256GBs, iPhone 12 Pro Max 128 and 256 GBs, "
          "iPhone 12 Pro 256GBs.")
elif 800 <= amount_bud < 1000:
    print("You can afford:")
    print("iPhone Xs 512 GBs, iPhone Xs Max 256 GBs, iPhone 11 Pro 64GBs, "
          "iPhone 11 Pro Max 64GBs, iPhone 12 128GBs and "
          "256GBs, iPhone 12 Pro 128 GBs, iPhone 12 mini 256GBs.")
elif 600 <= amount_bud < 800:
    print("You can afford:")
    print("iPhone 8+ 256 GBs, iPhone X 256 GBs, iPhone Xs 64 and 256 GBs, "
          "iPhone 12 64GBs, iPhone 11 128 and 256GBs, "
          "iPhone 12 mini 64 and 128GBs.")
elif 400 <= amount_bud < 600:
    print("You can afford:")
    print("iPhone 8 256 GBs, iPhone 8+ 64GBs and 128 GBs, iPhone X 64GBs, "
          "iPhone 11 64GBs, iPhone SE 128 and 256GBs, "
          "iPhone Xr 64 and 128GBs.")
elif 200 <= amount_bud < 400:
    print("You can afford:")
    print("iPhone 8 64GBs and 128GBs, iPhone SE 64GBs.")
elif not (amount_bud <= 150) and not (amount_bud > 200):
    print("You can't afford any iPhone newer than the iPhone 7 64 GBs")
else:
    print("Unfortunately, the market doesn't have any iPhone in good "
          "condition at that price.")
# the "if amount_bud" and "elif amount_bud" statements used to display what
# iPhones are available to the user
# depending on their budget. the else statement used to print
# that there are no iPhones available in the users budget

accessories_1 = input("Would you like to purchase a screen protector or case "
                      "for the iPhone(s)? ")
if (accessories_1 == 'yes') or (accessories_1 == 'Yes'):
    print("Wonderful! The average price for a screen protector is about "
          "$10-$15 and the average price of a case is "
          "around $20-$40")
else:
    print("No worries, enjoy your purchase(s).")


# the if-else function is used to ask the user if they would like to purchase
# any additional protection/accessories for their iPhone and
# an approximation of how much it would be to purchase the products

# function definition
def print_message():
    """

    :rtype: str
    """
    print("Can't thank you enough for trying the JdrTech Beta.")
    print("Thank you!")


# function definition
def main():
    """ Returns the goodbye message for the user."""
    print("Hopefully you enjoyed it, we expanded a bit more this time.")
    print_message()


# function call
main()
