#!/usr/bin/env python
# coding: utf-8

# # STAMP SELLING

# Name : Rizky Septiyanti
# Student id: 32899580
# Start date : 27 october 2021
# Last modified : 31 october 2021
# 

# # USER

# In[3]:


import user

user.sign_in ()


# # Add Item To Shopping Chart

# (file cannot be imported because many global variable. I've try global function but the list not transfered to next modul )

# In[4]:


def price_parcel ():

    z = open('Countries and Zones.csv', 'r') 
    reader = csv.reader(z) 
    destination = {}

    for row in reader :
        destination[row[0]] = row[1]

    while True:
        dest = input("enter the destination :").capitalize()
        if dest in destination.keys():
            destination_list.append(dest)
            file1.write("   Destination: ")
            file1.write(dest)
            print ("your destination is in: " + destination.get(dest))
            break
        else:
            print("your destination is not on the list, please enter again")

    w = open('Economy Parcel Price Guide.csv', 'r') 
    reader1 = csv.reader(w) 

    weight_dict = {}

    for row in reader1:
        weight_dict[row[0]] = {"Zone 1":row[1], "Zone 2":row[2], "Zone 3":row[3],"Zone 4":row[4], "Zone 5":row[5], "Zone 6 ":row[6], "Zone 7":row[7], "Zone 8":row[8],"Zone 9":row[9]}

    while True: 
        weight_item = input("please enter the weight of your item in kg :")
        if 15 < int(weight_item) <= 20 :
            weight_price = weight_dict["Up to 20kg"][destination.get(dest)]
            print("your estimate price is: " + weight_price +" dollar")
            weight_list.append(float(weight_item))
            wprice_list.append(float(weight_price))
            file1.write("   Weight: ")
            file1.write(weight_item)
            break
        elif 10 < int(weight_item) <= 15:
            weight_price =weight_dict["Up to 15kg"][destination.get(dest)]
            print("your estimate price is: " + weight_price+ " dollar")
            weight_list.append(float(weight_item))
            wprice_list.append(float(weight_price))
            file1.write("   Weight: ")
            file1.write(weight_item)
            break
        elif 5 < int(weight_item) <= 10 :
            weight_price = weight_dict["Up to 10kg"][destination.get(dest)]
            print("your estimate price is: " + weight_price+ " dollar")
            weight_list.append(float(weight_item))
            wprice_list.append(float(weight_price))
            file1.write("   Weight: ")
            file1.write(weight_item)
            break
        elif 3 < int(weight_item) <= 5 :
            weight_price = weight_dict["Up to 5kg"][destination.get(dest)]
            print("your estimate price is: " + weight_price + " dollar")
            weight_list.append(float(weight_item))
            wprice_list.append(float(weight_price))
            file1.write("   Weight: ")
            file1.write(weight_item)
            break
        elif 2.5 < int(weight_item) <= 3 :
            weight_price= weight_dict["Over 2.5 kg up to 3kg"][destination.get(dest)]
            print("your estimate price is: " + weight_price + " dollar")
            weight_list.append(float(weight_item))
            wprice_list.append(float(weight_price))
            file1.write("   Weight: ")
            file1.write(weight_item)
            break
        else :
            print("your item weight should be over 2.5kg to 20 kg")

    while True:
        size = input("enter the size of parcel (small/medium/large): ").lower()
        if size == ("small"):
            size_price = weight_price
            print("final price for the item is : " + str(size_price) + " dollar")
            size_list.append(size)
            file1.write("   Size: ")
            file1.write(size)
            break
        elif size == ("medium"):
            size_price = int(float(weight_price)) + (int(float(weight_price))*0.1)
            print("final price for the item is : " + str(size_price) + " dollar")
            size_list.append(size)
            file1.write("   Size: ")
            file1.write(size)
            break
        elif size == ("large"):
            size_price = int(float(weight_price)) + (int(float(weight_price))*1.5)
            print("final price for the item is : " + str(size_price) + " dollar")
            size_list.append(size)
            file1.write("   Size: ")
            file1.write(size)
            break
        else :
            print("invalid input")

    file1.write("   Price: ")
    file1.write(str(size_price))
    price_list.append(float(size_price))


# In[5]:


def price_letter ():

    z = open('Countries and Zones.csv', 'r') 
    reader = csv.reader(z) 
    destination = {}

    for row in reader :
        destination[row[0]] = row[1]

    while True:
        dest = input("enter the destination :").capitalize()
        if dest in destination.keys():
            print ("your destination is in: " + destination.get(dest))
            file1.write("   Destination: ")
            destination_list.append(dest)
            file1.write(dest)
            break
        else:
            print("your destination is not on the list, please enter again")

    w = open('Economy letter Price Guide.csv', 'r') 
    reader1 = csv.reader(w) 

    weight_dict = {}

    for row in reader1:
        weight_dict[row[0]] = {"Zone 1":row[1], "Zone 2":row[2], "Zone 3":row[3],"Zone 4":row[4], "Zone 5":row[5], "Zone 6 ":row[6], "Zone 7":row[7], "Zone 8":row[8],"Zone 9":row[9]}
    
    while True:
        weight_item = input("please enter the weight of your item in kg :")
        if 1.5 < float(weight_item) <= 2 :
            weight_price = weight_dict["Up to 2kg"][destination.get(dest)]
            print("your estimate price is: " + weight_price +" dollar")
            weight_list.append(weight_item)
            wprice_list.append(float(weight_price))
            file1.write("   Weight: ")
            file1.write(weight_item)
            break
        elif 1 < float(weight_item) <= 1.5:
            weight_price = weight_dict["Up to 1.5kg"][destination.get(dest)]
            print("your estimate price is: " + weight_price + " dollar")
            weight_list.append(weight_item)
            wprice_list.append(float(weight_price))
            file1.write("   Weight: ")
            file1.write(weight_item)
            break
        elif 0.5 < float(weight_item) <= 1 :
            weight_price = weight_dict["Up to 1kg"][destination.get(dest)]
            print("your estimate price is: " + weight_price + " dollar")
            weight_list.append(weight_item)
            wprice_list.append(float(weight_price))
            file1.write("   Weight: ")
            file1.write(weight_item)
            break
        elif 0 < float(weight_item) <= 0.5 :
            weight_price = weight_dict["Up to 500g"][destination.get(dest)]
            print("your estimate price is: " + weight_price + " dollar")
            weight_list.append(weight_item)
            wprice_list.append(float(weight_price))
            file1.write("   Weight: ")
            file1.write(weight_item)
            break
        else :
            print("your item should be limited to 2kg")
    
    while True:
        size = input("enter the size of parcel (small/medium/large): ").lower()
        if size == ("small"):
            size_price = weight_price
            print("final price for the item is : " + str(size_price) + " dollar")
            file1.write("   Size: ")
            file1.write(size)
            size_list.append(size)
            break
        elif size == ("medium"):
            size_price = int(float(weight_price)) + (int(float(weight_price))*0.1)
            print("final price for the item is : " + str(size_price) + " dollar")
            file1.write("   Size: ")
            file1.write(size)
            size_list.append(size)
            break
        elif size == ("large"):
            size_price = int(float(weight_price)) + (int(float(weight_price))*1.5)
            print("final price for the item is : " + str(size_price) + " dollar")
            file1.write("   Size: ")
            file1.write(size)
            size_list.append(size)
            break
        else :
            print("invalid input")
    
    file1.write("   Price: ")
    file1.write(str(size_price))
    price_list.append(float(size_price))
    
    w.close()


# In[6]:


def add_item ():
    while True :
        type_post = input("please input the type of item (letter/parcel) :")

        if type_post == "parcel":
            type_list.append(type_post)
            file1.write("   item type : ")
            file1.write(type_post)
            dp = pd.read_csv('Economy Parcel Price Guide.csv')
            print(dp)
            print ("Here is the price guide for parcel, prices in the table are for small size, there is addition rate for bigger size")
            print ("for medium size final price increase by 10%")
            print ("for large size final price increase by 15%")
            price_parcel()
            break     
        elif type_post == "letter":
            type_list.append(type_post)
            file1.write("   item type : ")
            file1.write(type_post)
            dl = pd.read_csv('Economy letter Price Guide.csv')
            print(dl)
            print ("Here is the price guide for letter")
            print ("Here is the price guide for parcel, prices in the table are for small size, there is addition rate for bigger size")
            print ("for medium size final price increase by 10%")
            print ("for large size final price increase by 15%")
            price_letter()
            break
        else :
            print ("please type the exact word (letter/parcel)")


# In[8]:


import pandas as pd
import csv

with open("Shopping_chart.txt", "w") as file1 :
    print("------WELCOME TO SHOPPING CHART--------")
    file1.write("------WELCOME TO SHOPPING CHART--------")

    type_post = ""
    type_list = [] #list of types
    destination_list = [] #list of destination
    weight_list = [] #list of weight
    size_list = [] #list of size
    wprice_list = []
    price_list = [] #list of final item price
    item_list = [] #list of item
    
    #item_list= [item1, item2, item3]

    
    file1.write("\nItem no : 1")
    item_list.append("item 1")
    add_item()
    file1.write("\n")
    while True: 
        nextitem = input("ypu can input 1 other  item, do you want to add another item (yes/no): ")
        if nextitem == "yes":
            item_list.append("item 2")
            file1.write("Item no : 2")
            add_item()
            if type_list[0]==type_list[1] and destination_list[0] == destination_list[1] and weight_list[0] == weight_list[1] and size_list[0]==size_list[1]:
                confirmation = input("you input the same item do you want to proceed? (yes/no) : ").lower()
                if confirmation == "yes":
                    print("next")
                else :
                    print("restart")
            break
        elif nextitem == "no":
            print("proceed to view shopping chart")
            break
        else :
            print("wrong input")


    total_cost = sum(price_list)
    print("total cost: " + str(total_cost) + "dollar")
    file1.write("\n \nTotal cost: ")
    file1.write(str(total_cost))
    
    print("   ")
    print("Shopping chart limited to two item, proceed to view shopping chart -->")
    
    


# # View Shopping Cart

# In[10]:


import view

view.cart()


# # AMEND

# (file cannot be imported because many global variable. I've try global function but the list not transfered to next modul )

# In[11]:


def weight_letter_newp(x) : #function for getting price after weight change in letter item
    
    if 1.5 < float(weight_list[x]) <= 2:
        weight_newprice = weight_dict["Up to 2kg"][destination.get(destination_list[x])]
        print("your estimate price is: " + str(weight_newprice) + " dollar")
        del wprice_list [x]
        wprice_list.insert(x, float(weight_newprice))
    elif 1 < float(weight_list[x]) <= 1.5:
        weight_newprice = weight_dict["Up to 1.5kg"][destination.get(destination_list[x])]
        del wprice_list [x]
        wprice_list.insert(x, float(weight_newprice))
        print("The new weight price for item 1 is "+ str(weight_newprice))
    elif 0.5 < float(weight_list[x]) <= 1 :
        weight_newprice = weight_dict["Up to 1kg"][destination.get(destination_list[x])]
        del wprice_list [x]
        wprice_list.insert(x, float(weight_newprice))
        print("The new weight price for item 1 is "+ str(weight_newprice))
    elif 0 < float(weight_list[x]) <= 0.5 :
        weight_newprice = weight_dict["Up to 500g"][destination.get(destination_list[x])]
        del wprice_list [x]
        wprice_list.insert(x, float(weight_newprice))
        print("The new weight price for item 1 is "+ str(weight_newprice))


# In[12]:


def weight_parcel_newp(x): #function for getting price after weight change in parcel item

    if 15 < float(weight_list[x]) <= 20 :
        weight_newprice = weight_dict2["Up to 20kg"][destination.get(destination_list[x])]
        print("your estimate price is: " + str(weight_newprice) + " dollar")
        del wprice_list [x]
        wprice_list.insert(x, float(weight_newprice))

    elif 10 < float(weight_list[x]) <= 15:
        weight_newprice = weight_dict2["Up to 15kg"][destination.get(destination_list[x])]
        print("your estimate price is: " + str(weight_newprice) + " dollar")
        del wprice_list [x]
        wprice_list.insert(x, float(weight_newprice))
        
    elif 5 < float(weight_list[x]) <= 10 :
        weight_newprice = weight_dict2["Up to 10kg"][destination.get(destination_list[x])]
        print("your estimate price is: " + str(weight_newprice) + " dollar")
        del wprice_list [x]
        wprice_list.insert(x, float(weight_newprice))

    elif 3 < float(weight_list[x]) <= 5 :
        weight_newprice = weight_dict2["Up to 5kg"][destination.get(destination_list[x])]
        print("your estimate price is: " + str(weight_newprice) + " dollar")
        del wprice_list [x]
        wprice_list.insert(x, float(weight_newprice))

    elif 2.5 < float(weight_list[x]) <= 3 :
        weight_newprice = weight_dict2["Over 2.5 kg up to 3kg"][destination.get(destination_list[x])]
        print("your estimate price is: " + str(weight_newprice) + " dollar")
        del wprice_list [x]
        wprice_list.insert(x, float(weight_newprice))


# In[13]:


def size_newp(x): #function for getting price after size change

    if size_list[x] == ("small"):
        size_newprice = wprice_list[x]
        print("final price for the item is : " + str(size_newprice) + " dollar")
        del price_list[x]
        price_list.insert(x, size_newprice)
    
    elif size_list[x] == ("medium"):
        size_newprice = int(float(wprice_list[x])) + (int(float(wprice_list[x]))*0.1)
        print("final price for the item is : " + str(size_newprice) + " dollar")
        del price_list[x]
        price_list.insert(x, size_newprice)
        
    elif size_list[x] == ("large"):
        size_newprice = int(float(wprice_list[x])) + (int(float(wprice_list[x]))*0.1)
        print("final price for the item is : " + str(size_newprice) + " dollar")
        del price_list[x]
        price_list.insert(x, size_newprice)
        


# In[14]:


def change_item(x):
    
    #input changes
    while True:
        change_item = input("Do you want to change weight/size (type : weight / size): ")
        if change_item == "weight" :
            while True:
                try:
                    weight_c = float(input("please input new item weight for " + "item " + str(x+1) + ": "))
                    if type_list[x] == "parcel":
                        if weight_c < 2.5 or (weight_c) > 20 :
                            print("Weight should be minimum 2.5kg and maximum 20kg")
                        elif int(float(weight_c)) >= 2.5:
                            print("item 1, parcel, weight:" + str(weight_c))
                            del weight_list[x]
                            weight_list.insert(x,weight_c) 

                            #Change value of the weight price
                            weight_parcel_newp(x)
                            #Change value of the final price (include size)
                            size_newp(x)

                            break
                        else :
                            print("wrong input")

                    elif type_list[x] == "letter":

                        if weight_c > 2 :
                            print("Weight should be maximum 2kg")
                        elif weight_c <= 2:
                            print("item1, letter, weight:" + str(weight_c))
                            del weight_list[x]
                            weight_list.insert(x,weight_c)


                            #Change value of the weight price
                            weight_letter_newp(x)
                            #Change value of the final price (include size)
                            size_newp(x)
                            break
                        else :
                            print("wrong input")
                except ValueError : #valueerror might rise if input word
                    print("please enter a number not word")
                    
            break                  

        if change_item == "size" :
            while True: 
                size_c = input("please input new item size for item 1 (small/medium/large): ")
                if  size_c == "small" or size_c == "medium" or size_c == "large" :
                    print("item1, size:" + size_c)
                    del size_list[x]
                    size_list.insert(x,size_c)
                    
                    #change the value of price
                    size_newp(x)
                    break
                else :
                    print("wrong input")
            break
        else:
            print('wrong input')


# In[15]:


import csv

#open the csv file again

z = open('Countries and Zones.csv', 'r') 
reader = csv.reader(z) 
destination = {}

for row in reader :
    destination[row[0]] = row[1]

w = open('Economy letter Price Guide.csv', 'r') 
reader1 = csv.reader(w) 

weight_dict = {}

for row in reader1:
    weight_dict[row[0]] = {"Zone 1":row[1], "Zone 2":row[2], "Zone 3":row[3],"Zone 4":row[4], "Zone 5":row[5], "Zone 6 ":row[6], "Zone 7":row[7], "Zone 8":row[8],"Zone 9":row[9]}

w = open('Economy Parcel Price Guide.csv', 'r') 
reader1 = csv.reader(w)

weight_dict2 = {}

for row in reader1:
    weight_dict2[row[0]] = {"Zone 1":row[1], "Zone 2":row[2], "Zone 3":row[3],"Zone 4":row[4], "Zone 5":row[5], "Zone 6 ":row[6], "Zone 7":row[7], "Zone 8":row[8],"Zone 9":row[9]}

#try to put open file code in function weight_letter_newp(x) weight_parcel_newp(x) but does not work


while True :
    amend = input("do you want to change the weight or size of the item?(yes/no): ").lower()
    if amend == "yes": 
        change = input("which item (1/2): ")
        if change == "1":
            change_item(0)
        elif change == "2" :
            if len(item_list) < 2: #if not check the line item in list, when there no item 2 result in error
                print("you don't have item 2")
            else :
                change_item(1)
        else :
            print("wrong input, please input number 1 or 2 ")
    else :
        print("Proceed to next step")
        break
w.close()
z.close()


# # Remove

# (file cannot be imported because many global variable. I've try global function but the list not transfered to next modul )

# In[16]:


def delete () :
    while True:
            delete = input("do you want to delete an item? (yes/no): ").lower()
            if delete == "yes":
                item_delete = int(input("which item do you want to delete? (1/2)"))
                if item_delete == 2 and len(item_list) < 2: #if not check the line item in list, when there no item 2 result in error
                    print("you don't have item 2")
                else:
                    print("item" + str(item_delete) + " type : " + str(item_list[item_delete - 1]) + ", destination : " 
                          + str(destination_list[item_delete - 1]) + ", weight: " + str(weight_list[item_delete - 1])
                          + ", size: " + str(size_list[item_delete - 1]) + ", price: " + str(price_list[item_delete - 1]) )
                    del_confirmation = input("are you sure you want to delete item " + str(item_delete) + (" (yes/no): ")).lower()
                    if del_confirmation == "yes" :
                        del item_list[item_delete - 1] #deleting each item in the list accoring to the index
                        del type_list[item_delete - 1]
                        del destination_list[item_delete - 1]
                        del weight_list[item_delete - 1]
                        del size_list[item_delete - 1]
                        del wprice_list [item_delete - 1]
                        del price_list[item_delete - 1]
                        print("item " + str(item_delete) + " deleted")
    #                     return item_list
    #                     return type_list
    #                     return destination_list
    #                     return weight_list
    #                     return size_list
    #                     return wprice_list 
    #                     return price_list
                        if item_list == []:
                            print("you have no item in the shopping chart")
                            break
                        else :
                            print("next")
                    elif del_confirmation == "no" :
                        print ("item " + str(item_delete) + " still in shopping chart")

            #customer have to be sure there are no other item they want to delete
            elif delete == "no" :
                print("proceed to check out --->")
                break
            else :
                print("wrong input")
                


# In[17]:


delete()


# # Check Out

# (file cannot be imported because many global variable. I've try global function but the list not transfered to next modul )

# In[18]:


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


# In[19]:


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

