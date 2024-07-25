# Importing needed modules
import Read
import Operations

# Function that displays the introduction to the rental shop
def main_intro():
    print("***************************************************************\n		WELCOME TO THE RENTAL SHOP \n***************************************************************\n")
    print()

#Calling the above introduction function
main_intro()

# Main Function which provides options to the users to either rent items, return items or exit the program
def Main():
    
    # while loop so that runs until user chooses option to exit
    while True:        
        try:
            # Displays options
            print("Select one of the options: \n 1.Rent \n 2.Return \n 3.Exit\n")
            Option_Input = int(input("Enter the number of preferred option: "))
            
            #if 1 is entered, necessary functions for renting are called from Operations
            if Option_Input == 1:
                Operations.display_intro()
                Operations.rent()
                
            #if 2 is entered, necessary functions for returning are called from Operations            
            elif Option_Input == 2:
                Operations.display_return_intro()
                Operations.return_item()
            
            #if 3 is entered, the while loop is exited thus exiting the program
            elif Option_Input == 3:
                print()
                print("Thank you for shopping!")
                break
            
            #If any other value than 1,2 or 3 is entered
            else:
                print("Enter a valid option\n")
        
        #try except to handle any invalid 
        except ValueError:
             print("Invalid Input. Enter a valid option (1, 2, or 3).\n")
             
# Calling main function
Main()

