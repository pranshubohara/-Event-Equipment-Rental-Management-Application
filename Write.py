# Function to update the quantities in the quipment file
def Update_Equipment_Quantities(new_equipment_data):
    # Open Equipment.txt in write mode to update quantities
    with open("Equipment.txt","w") as equipment_file:
        # Loop through each item in new_equipment_data
        for item in new_equipment_data:
            # Construct a line for the item with updated quantity
            line = item["Name"] + "," + item["Brand"] + "," + item["Price"] + "," + item["Quantity"] + "\n"
            # Write the line to the equipment_file
            equipment_file.write(line)
            
# Function to write invoice for rented items for customer
def Write_Invoice(Customer_name, customer_number, rent_time, invoice_items, total_amount, payment, change,):
    # Create an invoice filename based on customer name
    invoice_filename = Customer_name.replace(' ', '_') + ".txt"
    
    # Open the invoice file in write mode
    with open(invoice_filename, "w") as invoice_file:
        
        #Writing invoice for rented items based on rent details
        invoice_file.write("===== INVOICE =====\n")
        invoice_file.write(f"Customer Name: {Customer_name}\n")
        invoice_file.write(f"Contact Number: {customer_number}\n")
        invoice_file.write(f"Transaction Time: {rent_time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        invoice_file.write("Purchased Items:\n")
        # Write details of each purchased item
        for item in invoice_items:
            invoice_file.write(f"- Name: {item['Name']}, Brand: {item['Brand']}, Price: {item['Price']}, Quantity: {item['Quantity']}\n")
        invoice_file.write(f"Total Amount: {total_amount}\n")
        invoice_file.write(f"Payment: {payment}\n")
        invoice_file.write(f"Change: {change}\n")
        invoice_file.write("==================\n")
        
# Function to write the bill after the customer returns items
def Write_Bill(return_customer_name, items_info, return_date,item_name, item_brand, fine_amount):
    # Create a file name for the return bill based on customer name
    file_name = f"return_bill_{return_customer_name}.txt"
    
    # Open the file in write mode to create the return bill
    with open(file_name, "w") as f:
        # Write the Receipt bill 
        f.write("********** RETURN RECEIPT **********\n")        
        f.write(f"\nCustomer Name: {return_customer_name}\n")
        f.write("Returned Items:\n")
        # Write details of each returned item
        for item_name, quantity in items_info.items():
            f.write(f"-Item: {item_name}, Brand: {item_brand}, Quantity: {quantity}\n")
        f.write(f"\nReturn Date: {return_date}\n")
        # Only write if fine amount is greater than 0
        if fine_amount > 0:
            f.write(f"Fine Charged: ${fine_amount}\n")
        f.write("\n**********************************\n")

