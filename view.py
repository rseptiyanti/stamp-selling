#!/usr/bin/env python
# coding: utf-8

# # View Shopping Cart

# Name : Rizky Septiyanti
# Student id: 32899580
# Start date : 25 october 2021
# Last modified : 26 october 2021 

# Shopping cart is viewed in the text file. so user can get clearer look.

# In[3]:


def cart():
    view = open("Shopping_chart.txt")

    view_shopping = view.read()

    view.close()

    print(view_shopping)


# In[1]:


#cart ()

