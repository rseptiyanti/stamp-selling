#!/usr/bin/env python
# coding: utf-8

# # REMOVE

# Name : Rizky Septiyanti
# Student id: 32899580
# Start date : 27 october 2021
# Last modified : 31 october 2021

# delete () : user can delete the item exist in shopping cart

# since the shopping cart only limited to 2 item, then user have to chose between item 1 or item 2. User asked a confirmation question to delete item. If user want to delete both, user can chose item one then item 2.

# In[ ]:


def delete ():
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


# In[ ]:


delete()

