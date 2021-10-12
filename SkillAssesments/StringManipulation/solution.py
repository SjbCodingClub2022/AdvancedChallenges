#defining the function
def Name(full_name):
    #creating a list containing the first name and last name
    full_name_split = full_name.split(" ")

    to_return = [
        #first name
        full_name_split[0],
        #last name
        full_name_split[1],
        #getting the first charachter of both strings in the list
        f"{full_name_split[0][0]}.{full_name_split[1][0]}",
        #upper case name
        full_name.upper(),
        #lower case name
        full_name.lower()
    ]
    #returning the list
    return to_return

#save user input to variable
full_name = input("Enter a first name and last name seperated by a space: ")

# calls the Name funciton and prints the return value
print(Name(full_name))