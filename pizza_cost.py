#!/usr/bin/env python3
# Created by: Remy Skelton
# Created on: Oct 3, 2023
# This program asks the user for the diameter of the
# pizza. It then calculates and displays the total cost
# of the pizza with tax
import constants


def main():
    # get the diameter from user
    diameter = int(input("Enter the diameter of the pizza (inches): "))

    # create variables
    subtotal = (
        constants.LABOUR_COST + constants.RENTAL_COST + constants.INGRED_COST * diameter
    )
    tax = constants.HST * subtotal
    total = subtotal + tax

    # display the variables to user
    print("")
    print("The subtotal cost is = ${:,.2f}".format(subtotal))
    print("The tax cost is = ${:,.2f}".format(tax))
    print("The total cost is = ${:,.2f}".format(total))


if __name__ == "__main__":
    main()
