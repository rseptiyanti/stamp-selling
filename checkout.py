#!/usr/bin/env python
# coding: utf-8

# # Check Out

# User proceed to check out shopping. User will get text file containing invoice and detail about shipping item. User check out will be recorded in.

# Name : Rizky Septiyanti
# Student id: 32899580
# Start date : 27 october 2021
# Last modified : 31 october 2021
# 

# In[ ]:


#invoice
from datetime import datetime
timestr = datetime.now().strftime("%Y-%m%--%d% %H%__%M%__%S")

invoice = timestr +".txt"

fi = open (invoice, "w")

fi.write("----------- INVOICE -----------")

if len (type_list) == 1: #if in list only contain 1 item
    fi.write("\n" + item_list[0] +  "  Type: " + type_list[0] + "  Destination: " + destination_list[0] + "  Weight: "
            + str(weight_list[0]) + "kg" + "  Size: " + size_list[0] + "  Price: $" + str(price_list[0]) )
    fi.write("\n")
    fi.write("\n Total cost : $" + str(sum(price_list)))
    fi.write("\n")
    fi.write("\nTHANK YOU FOR SHOPPING WITH US")
    fi.write("\n")
    fi.write("\n")
    fi.write("---------- End INVOICE ----------")
    fi.write("\n")
    fi.write("\n")
    fi.write("--------- Purchased Stamps --------")
    fi.write("\n" + type_list[0])
    fi.write("\nDestination: " + destination_list[0])
    fi.write("   Weight: " + str(weight_list[0]) + "kg")
    fi.write("\n")
    fi.write("-----------------------------------")
    


elif len(type_list) == 2: #if in list contain 2 item
    fi.write("\n" + item_list[0] +  "  Type: " + type_list[0] + "  Destination:" + destination_list[0] + "  Weight: "
            + str(weight_list[0]) + "kg" + "  Size: " + size_list[0] + "  Price: $" + str(price_list[0]) )
    fi.write("\n" + item_list[1] +  "  Type: " + type_list[1] + "  Destination:" + destination_list[1] + "  Weight: "
            + str(weight_list[1]) + "kg" + "  Size: " + size_list[1] + "  Price: $" + str(price_list[1]) )
    fi.write("\n")
    fi.write("\n Total cost : $" + str(sum(price_list)))
    fi.write("\n")
    fi.write("\nTHANK YOU FOR SHOPPING WITH US")
    fi.write("\n")
    fi.write("\n")
    fi.write("---------- End INVOICE ----------")
    fi.write("\n")
    fi.write("\n")
    fi.write("--------- Purchased Stamps --------")     #could make invoice fuction so do not have to write each item
    fi.write("\n" + type_list[0])
    fi.write("\nDestination: " + destination_list[0])
    fi.write("   Weight: " + str(weight_list[0]) + "kg")
    fi.write("\n")
    fi.write("-----------------------------------")
    fi.write("\n")
    fi.write("\n")
    fi.write("--------- Purchased Stamps --------")
    fi.write("\n" + type_list[1])
    fi.write("\nDestination: " + destination_list[1])
    fi.write("   Weight: " + str(weight_list[1]) + "kg")
    fi.write("\n")
    fi.write("-----------------------------------")
             
else : #if no item in list so the program not result in error
    fi.write("\nYou have no item in the shopping chart")
    fi.write("\n")
    fi.write("\nTHANK YOU FOR SHOPPING WITH US")
    fi.write("\n")
    fi.write("---------- End INVOICE ----------")


fi.close()
print("your invoice: " + invoice) #print the invoice name, user know which recent invoice text file


# In[ ]:


#import and append CSV
from datetime import datetime
import csv 

time = datetime.now().strftime("%Y-%m%--%d% %H%:%M%:%S") #format time

with open ("sales_history.csv", "a", newline = "") as sales:
    writer = csv.writer(sales)
    
    if len(type_list) == 1: 
        writer.writerow(["301", time, type_list[0], weight_list[0], 
                         destination_list[0], size_list[0], price_list[0]] )
    elif len(type_list) == 2:
        writer.writerow(["301", time, type_list[0], weight_list[0], 
                         destination_list[0], size_list[0], price_list[0]] )
        writer.writerow(["301", time, type_list[1], weight_list[1], 
                         destination_list[1], size_list[1], price_list[1]] )
    else :
        print("No item in shopping cart")

