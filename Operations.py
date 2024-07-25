# Importing needed modules
import Read
import Write
import datetime

# function that displays welcome to rental shop
def Welcome():
    print("***************************************************************\n		WELCOME TO THE RENTAL SHOP \n***************************************************************\n")

#function that displays welcome to rent menu
def display_intro():
    print("\n***************************************************************\n		WELCOME TO THE RENT MENU \n***************************************************************")

# Function that displays welcome to return menu
def display_return_intro():
    print("\n***************************************************************\n		WELCOME TO THE RETURN MENU \n***************************************************************")
    print()

# Rent function for the whole rent process
def rent():
    rent_loop = True
    while rent_loop:
        # Read the equipment present and also display the table
        Equipment_data = Read.Read_Equipments() 
        Read.Equipments_table(Equipment_data)
        
        Customer_name = input("Enter your full name: ")
        
        contact_loop = True
        while contact_loop:
            try:
                # Contact number input and making sure it is 10 digits
                customer_number = int(input("Enter your contact number: "))
                if len(str(customer_number)) != 10:
                    print("Entered contact must be exactly 10 digits")
                else:
                    break
            # Handling any invalid inputs from user
            except ValueError:
                print("Invalid input. Enter a valid contact number.\n")
    
        try:
            selecting_item = True
            invoice_items = [] # list created to store the items purchased 
            total_amount = 0 # Setting total amount as 0
            
            while selecting_item:
                entering_ID = True
                
                while entering_ID:
                    try:
                        # Taking input for the ID of item customer wants to purchase
                        Item_id = input("Enter the ID of the item you want to purchase: ")
                        found_item = None
                        
                        # Check if ID belongs to any item in equipment list
                        for item in Equipment_data:
                            if item["ID"] == int(Item_id):
                                found_item = item                                
                                break
                        if found_item is None:
                            print("Invalid ID. Please enter a correct ID.\n")
                        else:
                            break
                    # Handling any invalid non integer inputs from user    
                    except ValueError:
                        print("Invalid Input. Please enter a correct ID present in the table.\n") 

                choosing_quantity = True
                while choosing_quantity:
                    # Present quantity which is present in the equipment list
                    presentquantity = int(found_item["Quantity"])

                    try:
                        # Get quantity of item customer wants to buy
                        quantity_input = int(input("Enter the quantity amount you want to purchase: "))
                        
                        #Check if input is not less than or equal to 0
                        if quantity_input <= 0:
                            print("Quantity must be greater than 0.\n")
                        #Check if entered input for quantity is greater than present quantity
                        elif presentquantity < quantity_input:
                            print("Entered quantity is not available.\n")                            
                        else:
                            #Calulating the quantity of item left after purchase
                            item_quantity = presentquantity - quantity_input
                            choosing_quantity = False
                            
                            #Update the item quantity in the equipment.txt file
                            found_item["Quantity"] = str(item_quantity)
                            new_equipment_data = Equipment_data.copy()
                            new_equipment_data[(int(Item_id))-1]["Quantity"] = str(item_quantity)
                            Write.Update_Equipment_Quantities(new_equipment_data)
                            
                            #Calculating total amount
                            item_price = float(found_item["Price"].replace("$", ""))
                            total_amount += item_price * quantity_input
                            
                            #Dictionary for purchased items
                            purchased_item = {
                                "Name": found_item["Name"],
                                "Brand": found_item["Brand"],
                                "Price": found_item["Price"],
                                "Quantity": quantity_input
                                }
                            #Add the purchased items to the invoice items list
                            invoice_items.append(purchased_item)
                            
                    # Handling any invalid non integer inputs from user
                    except ValueError:
                        print("Invalid Input. Enter a correct quantity amount")
                        
                # Records the exact rental time
                rent_time = datetime.datetime.now()
                
                purchase_again = True
                while purchase_again:
                    print()
                    #Ask if customer wants to purchase again
                    Continue_Purchase = input("Do you wish to purchase more items? (Enter yes to continue or else enter any other value to proceed to checkout)")
                    if Continue_Purchase.lower() == "yes":
                        #Table shown to help continue the process
                        Read.Equipments_table(Equipment_data)
                        break
                    else:
                        #Printing invoice if customer does not wish to continue 
                        print()
                        print("********** RENT INVOICE **********")
                        print("Invoice For: ", Customer_name)
                        print("Contact Number:", customer_number)
                        print("Transaction Time:", rent_time.strftime("%Y-%m-%d %H:%M:%S"))
                        print()
                        print("Purchased Items: ")
                        #Printing items purchased by customer
                        for item in invoice_items:
                            print("Name:", item["Name"], "Brand:", item["Brand"], "Price:", item["Price"], "Quantity:", item["Quantity"])
                        print()
                        print("Total Amount: ", total_amount)
                        print("**********************************")                        
                        print()
                                                    
                        while True:
                            try:
                                #Input for payment from customer
                                payment = float(input("Enter the payment amount: $"))
                                
                                if payment >= total_amount:
                                    #Calculate change if more money was paid than total amount
                                    change = payment - total_amount
                                    print()
                                    print("Thank you for renting. Your change is $",change)
                                    #Writing the invoice to a file to save rent invoice
                                    Write.Write_Invoice(Customer_name, customer_number, rent_time, invoice_items, total_amount, payment, change)
                                    print()
                                    print("=============THANK YOU=============")
                                    print()
                                    break                                
                                else:
                                    #If amount not sufficient
                                    print("Insufficient payment. Please pay the correct amount.")
                            # Handling any invalid non integer inputs from user        
                            except ValueError:
                                print("Invalid Input")
                        # After the purchase all loops are ended        
                        purchase_again = False
                        selecting_item = False
                        rent_loop = False
        #To handle any exception                
        except Exception as e:
            print("Error:", e)
            
# return_item function for the whole return process  
def return_item():
    # Read the equipment data drom the equipment file
    Equipment_data = Read.Read_Equipments()
    
    return_loop = True
    while return_loop:
        try:
            return_name = True
            while return_name:
                # Getting name of customer
                return_customer_name = input("Enter your full name: ")
                # Retrieve information based on the name entered
                rent_items = Read.Read_Invoices(return_customer_name)
                
                #If rent invoice of person is not found then display this
                if not rent_items:
                    print("No rental information found for this customer")
                    return
                else:
                    #Dictionary to store information about rented items
                    items_info = {}
                    
                    for item in rent_items[0]["Purchased Items"]:
                        item_name = item["Name"]
                        item_brand = item["Brand"]
                        quantity = int(item["Quantity"])
                        # Check if item_name is already in items_info dictionary
                        if item_name in items_info:
                            # Add quantity to existing quantity for same item
                            items_info[item_name] += quantity 
                        else:
                            # Quantity is not added as not same item
                            items_info[item_name] = quantity 
                    print()
                    # Displaying rented items by customer
                    print("********** RENTED ITEMS **********")
                    for item_name, quantity in items_info.items():
                        print(f"Item: {item_name}, Brand: {item_brand}, Quantity: {quantity}")
                    
                    # Extracting rental transaction time and displaying it
                    rent_transaction = rent_items[0]['Transaction Time']
                    rent_date = datetime.datetime.strptime(rent_transaction, "%Y-%m-%d %H:%M:%S")
                    print("Rental Date:", rent_date)
                    print()
                    
                    # Ask for customer's input to go through the return
                    input("Would you like to return items now? (Press any key to continue)")
                    
                    # Calculate the difference between return date and rental date
                    return_date = datetime.datetime.now()
                    time_difference = return_date - rent_date
                    days_rented = time_difference.days

                    # Initialize the fine amount variable to 0
                    fine_amount = 0
                    
                    # Check if the rental period exceeds 5 days for possible fines
                    if days_rented > 5:
                        fine_per_day = 100
                        fine_amount = (days_rented - 5) * fine_per_day
                        print()
                        print("FINED: $ "+str(fine_amount)+" fine charged for exceeding rental period")

                        while True:
                            try:
                                # Input from user for paying fine
                                payment = float(input("Enter the fine amount: $"))
                                # If payment amount is greater than or equal to fine amount 
                                if payment >= fine_amount:
                                    change = payment - fine_amount
                                    print("Thank you for returning. Your change is $", change)
                                    break
                                # Else insufficient payment as fine amount not fully cleared
                                else:
                                    print("Insufficient payment. Please pay the correct amount.")
                            # Handling any invalid non integer inputs from user
                            except ValueError:
                                print("Invalid input. Enter a valid payment amount.")
                    
                    # Copy of Equipment_data so to update quantities
                    new_equipment_data = Equipment_data.copy()
                    
                    # Add the quantites for the returned items in the new_equipment_data
                    for item_name, quantity in items_info.items():
                        for equipment_item in new_equipment_data:
                            if equipment_item["Name"] == item_name:
                                equipment_item["Quantity"] = str(int(equipment_item["Quantity"]) + quantity)
                                break
                    # Write the updated quantities to the equipment file
                    Write.Update_Equipment_Quantities(new_equipment_data)
                    
                    # Printing the Return Receipt
                    print()
                    print("********** RETURN RECEIPT **********")
                    print()
                    print("Customer Name:", return_customer_name)
                    print("Returned Items:")
                    
                    # Display details of returned items
                    for item_name, quantity in items_info.items():
                        print(f"Item: {item_name}, Brand: {item_brand}, Quantity: {quantity}")
                    print("Return Date:", return_date)
                    
                    # Display fine amount if fine amount more than 0
                    if fine_amount > 0:
                        print("Fine Charged: $", fine_amount)
                    print()                    
                    print("************************************")

                    # Write return receipt to a file
                    Write.Write_Bill(return_customer_name, items_info, return_date, fine_amount, item_brand, fine_amount)
                    print()
                    print("=============THANK YOU=============")
                    print()
                    
                    # End the loops
                    return_name = False
                    return_loop = False
                    
        #To handle any exception            
        except Exception as e:
            print("ERROR:", e)

    