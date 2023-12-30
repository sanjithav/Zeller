# File: Zeller.py
# Student: Sanjitha Venkata
# UT EID: sv28325
# Course Name: CS303E
# 
# Date: 9/18/2023
# Description of Program: Calculates day of the week based on user input of year, month, and day of the month

def main():
    # Describe what this function does here. 

    # Accept the year from the user and convert it to an int.
    Y = int( input("\nEnter year (e.g., 2008): "))
    # If the year is not greater than 1752, print an error
    # message and exit the program. 
    if (Y < 1753):
        print("Year must be > 1752. Illegal year entered:", Y, "\n")
        return

    # handle the month similarly
    m = int( input("Enter month (1-12): "))
    if (m < 1 or m > 12):
        print("Month must be in [1..12]. Illegal month entered:", m, "\n")
        return
    if(m==1 or m==2):
        m+=12
        Y-=1
    # handle the day of the month similarly
    d = int( input("Enter day of the month (1-31): "))
    if (d < 1 or d > 31):
        print("Day must be in [1..31]. Illegal day entered:", d, "\n")
        return

    # Compute the other variables, including h
    K = Y%100
    J = Y//100
    h = ( d + (13 * (m + 1))//5 + K + K//4 + J//4 + 5*J ) % 7

    # Compute the name of the day from h
    if(h==0):
        day="Saturday"
    elif(h==1):
        day="Sunday"
    elif(h==2):
        day="Monday"
    elif(h==3):
        day="Tuesday"
    elif(h==4):
        day="Wednesday"
    elif(h==5):
        day="Thursday"
    elif(h==6):
        day="Friday"

    # print the day of week message
    print("Day of the week is", day, "\n")

# You'll need this to run your main program. 
main()
