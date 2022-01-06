#!/usr/bin/env python
# coding: utf-8

# # Add Item To Shopping Chart

# Name : Rizky Septiyanti 
# Student id: 32899580 
# Start date : 25 october 2021 
# Last modified : 31 October 2021

# This program provide user input to item in the shopping chart. The shopping chart list only limited to two item then proceed to view shopping chart. User will be able to change and remove item in the next program.

# price_parcel function contain destination input, weight input, and size input for parcel item. Customer will get the price according ro parcel price guide rules

# In[1]:


def price_parcel ():

    z = open('Countries and Zones.csv', 'r') 
    reader = csv.reader(z) 
    destination = {}

    for row in reader :
        destination[row[0]] = row[1] #read csv as dictionary

    while True:
        dest = input("enter the destination :").capitalize()
        if dest in destination.keys():
            destination_list.append(dest)
            file1.write("   Destination: ")
            file1.write(dest)
            print ("your destination is in: " + destination.get(dest)) #take destination zone
            break
        else:
            print("your destination is not on the list, please enter again")

    w = open('Economy Parcel Price Guide.csv', 'r') 
    reader1 = csv.reader(w) 

    weight_dict = {}

    for row in reader1: #display and take value from csv
        weight_dict[row[0]] = {"Zone 1":row[1], "Zone 2":row[2], "Zone 3":row[3],"Zone 4":row[4], "Zone 5":row[5], "Zone 6 ":row[6], "Zone 7":row[7], "Zone 8":row[8],"Zone 9":row[9]}

    while True: #weight price condition
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

    while True: #size price condition
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
    file1.write(str(size_price)) #take price
    price_list.append(float(size_price)) #total price for 1 item



# price_letter function contain destination input, weight input, and size input for parcel item. Customer will get the price according ro letter price guide rules.

# In[8]:


def price_letter ():

    z = open('Countries and Zones.csv', 'r') 
    reader = csv.reader(z) 
    destination = {}

    for row in reader : #read csv as dictionary
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

    w = open('Economy letter Price Guide.csv', 'r') #read csv content and take value
    reader1 = csv.reader(w) 

    weight_dict = {}

    for row in reader1:
        weight_dict[row[0]] = {"Zone 1":row[1], "Zone 2":row[2], "Zone 3":row[3],"Zone 4":row[4], "Zone 5":row[5], "Zone 6 ":row[6], "Zone 7":row[7], "Zone 8":row[8],"Zone 9":row[9]}
    
    while True: #weight condition
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
    
    while True: #size condition
        size = input("enter the size of parcel (small/medium/large): ").lower()
        if size == ("small"):
            size_price = weight_price #size small
            print("final price for the item is : " + str(size_price) + " dollar")
            file1.write("   Size: ")
            file1.write(size)
            size_list.append(size)
            break
        elif size == ("medium"): #size medium
            size_price = int(float(weight_price)) + (int(float(weight_price))*0.1) # price + price times 10% / 0.1
            print("final price for the item is : " + str(size_price) + " dollar")
            file1.write("   Size: ")
            file1.write(size)
            size_list.append(size)
            break
        elif size == ("large"): #size large
            size_price = int(float(weight_price)) + (int(float(weight_price))*1.5) # price + price times 15% / 1.5
            print("final price for the item is : " + str(size_price) + " dollar")
            file1.write("   Size: ")
            file1.write(size)
            size_list.append(size)
            break
        else :
            print("invalid input")
    
    file1.write("   Price: ")
    file1.write(str(size_price))
    price_list.append(float(size_price)) #total price for one item
    
    w.close()



# add_item function use to seperate the input between parcel and letter

# In[9]:


def add_item ():
    while True :
        type_post = input("please input the type of item (letter/parcel) :") #chose type between letter or parcel

        if type_post == "parcel":
            type_list.append(type_post)
            file1.write("   item type : ")
            file1.write(type_post)
            dp = pd.read_csv('Economy Parcel Price Guide.csv')
            print(dp)
            print ("Here is the price guide for parcel")
            print ("prices in the table are for small size, there is addition rate for bigger size")
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
            print ("prices in the table are for small size, there is addition rate for bigger size")
            print ("for medium size final price increase by 10%")
            print ("for large size final price increase by 15%")
            price_letter()
            break
        else :
            print ("please type the exact word (letter/parcel)")



# Main input for item 1 and item 2 include all the empty list.

# In[10]:


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
    
    #item_list= [item1, item2]

    
    file1.write("\nItem no : 1")
    item_list.append("item 1")
    add_item()
    file1.write("\n")
    while True: 
        nextitem = input("you can add 1 more item, do you want to add another item (yes/no): ") #add another item
        if nextitem == "yes":
            item_list.append("item 2")
            file1.write("Item no : 2")
            add_item()
            if type_list[0]==type_list[1] and destination_list[0] == destination_list[1] and weight_list[0] == weight_list[1] and size_list[0]==size_list[1]:
                confirmation = input("you input the same item do you want to proceed? (yes/no) : ").lower()
                if confirmation == "yes":
                    print("next") #checking for the same item
                else :
                    print("restart")
            break
        elif nextitem == "no":
            print("proceed to view shopping chart") 
            break
        else :
            print("wrong input")


    total_cost = sum(price_list) #calculate total price for 2 item
    print("total cost: " + str(total_cost) + "dollar")
    file1.write("\n \nTotal cost: ")
    file1.write(str(total_cost))
    
    print("   ")
    print("Shopping chart limited to two item, proceed to view shopping chart -->")
    


# To Check

# 
# print(type_list) 
# print(destination_list)
# print(weight_list)
# print(size_list) 
# print(wprice_list)
# print(price_list) 
# print(item_list) 
