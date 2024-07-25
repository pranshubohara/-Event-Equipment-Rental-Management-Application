# Function to read the equipment.txt file
def Read_Equipments():
    
    # Open the Equipment.txt file in read mode
    Equipment_file = open("Equipment.txt","r")
    # Read the lines and split them into a list of lines
    Equipment_lines = Equipment_file.read().splitlines()
    equipment_list = []
    
    # Loop through each line in the Equipment_lines list
    for i in range(len(Equipment_lines)):
        # Split the line into items wherever comma is present
        item = Equipment_lines[i].split(",")
        #Add the items to the equipment_list
        equipment_list.append(item)
    
    equip = []
    
    # Loop through each item in the equipment_list
    for i in range(len(equipment_list)):
        # Create a dictionary for each equipment item
        dictionary = {
            "ID": i + 1,
            "Name" : equipment_list[i][0],
            "Brand" : equipment_list[i][1],
            "Price" : equipment_list[i][2],
            "Quantity" : equipment_list[i][3],      
            }
        # Append the dictionary to the equip list
        equip.append(dictionary)
        
    Equipment_file.close()
    return equip

Equipment_data = Read_Equipments()

# Function for displaying table
def Equipments_table(Equipment_data):
    # Table Headers
    print("=" *80)
    headers = ["ID","Name"," Brand"," Price","Quantity"]
    print("{:<5} {:<32} {:<20} {:<10} {:<10}".format(*headers))
    print("=" *80)
    
    # Loop through each item in Equipment_data and display items and details
    for item in Equipment_data:
        ID = item["ID"]
        name = item["Name"]
        brand = item["Brand"]
        price = item["Price"]
        quantity = item["Quantity"]
        print("{:<5} {:<32} {:<20} {:<10} {:<10}".format(ID,name, brand, price, quantity))
        
    # Table Footer
    print("=" *80)
    
# Function to read the invoice files
def Read_Invoices(return_customer_name):
    
    # Create the filename based on customer name
    rent_invoice = return_customer_name.replace(" ", "_") + ".txt"
    # List to store invoice data
    invoices = []
    
    # Open and read the invoice file
    with open(rent_invoice, "r") as invoice_file:
        invoice_lines = invoice_file.readlines()
        
        # Dictionary to store invoice details
        invoice = {}
        items_section = False
        # List to store purchased item details
        purchased_items = []
        
        # Loop through each line in invoice_lines
        for line in invoice_lines:
            line = line.strip()
            
            # Check if line contains customer name
            if line.startswith("Customer Name:"):
                invoice["Customer Name"] = line.split(": ", 1)[1]
            # Check if line contains contact number
            elif line.startswith("Contact Number:"):
                invoice["Contact Number"] = line.split(": ", 1)[1]
            # Check if line contains transaction time
            elif line.startswith("Transaction Time:"):
                invoice["Transaction Time"] = line.split(": ", 1)[1]
            # Check if line indicates start of purchased items section
            elif line == "Purchased Items:":
                items_section = True
            # Process lines within the purchased items section
            elif items_section and line.startswith("- "):
                item_details = line.lstrip("- ")
                item = {}
                
                # Loop through parts of the item details
                for part in item_details.split(", "):
                    key_value = part.split(": ")
                    # Check if part contains key-value pair
                    if len(key_value) == 2:
                        key, value = key_value
                        item[key] = value
                        
                # Append the item dictionary to purchased_items list
                purchased_items.append(item)
                
        # Add purchased item details to the invoice dictionary
        invoice["Purchased Items"] = purchased_items
        invoices.append(invoice)
        
    # Return the list of invoice dictionaries
    return invoices

