# Write a function is_even that will return true if the passed-in number is even.

def is_even(a_number):
    if a_number % 2 == 0:
        print('Even!')
    else:
        print('Odd')


# Read a number from the keyboard
while True:
    num = input("Enter a number: ")
    if num.isdigit():
        num = int(num)
        break

# Print out "Even!" if the number is even. Otherwise print "Odd"

is_even(num)
