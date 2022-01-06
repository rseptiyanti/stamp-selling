#!/usr/bin/env python
# coding: utf-8

# # AMEND

# Name : Rizky Septiyanti
# Student id: 32899580
# Start date : 27 october 2021
# Last modified : 31 october 2021

# user can amend item limited to its weight. price change everytime weight and size change

# weight_parcel_newp() : price letter guide to change price

# In[ ]:


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


# weight_parcel_newp() : price letter guide to change price

# In[ ]:


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


# size_newp(x) : size guide for item 1 or 2

# In[ ]:


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
        


# change_item(x): to change item 1 or item 2

# In[ ]:


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



# main input for changing weight and size of item

# In[ ]:


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

#try to open file code in function weight_letter_newp(x) weight_parcel_newp(x) but does not work


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

