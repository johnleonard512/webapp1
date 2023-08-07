
def meters_to_feet(meters):
    feet = meters * 3.281
    print(str(feet) + " feet")



if __name__ == '__main__':
    user_input = input("Enter meters to convert to feet: ")
    user_input = int(user_input)
    meters_to_feet(user_input)







