#!/usr/bin/env python
# coding: utf-8

# # User Log-in / Register

# Name : Rizky Septiyanti
# Student id: 32899580
# Start date : 14 october 2021
# Last modified : 28 october 2021

# Script for user to log in and register. In login user ask to input username until similar with the rules which is alphabetical only and greater than 8. User input password with the rule 4 digit. User re-enter username to check if exist then enter password. Password also have to be match.
# In register, user asked to input username until similar with the rules which is alphabetical only and greater than 8. User input password with the rule 4 digit. Then re-login to see if the password and username exist.

# In[3]:


def sign_in ():
    with open("user_details.txt", "w") as file :

        user =""
        key = 32899580 % 128

        def passwords () : #function for input password
            while True :
                password = (input("Please enter your password:  "))
                if len(password) != 4 :
                    print("your password should be only 4 digit")
                elif len(password) == 4 :
                    print("password entered")
                    encrypted_pass = []
                    for letter in password :
                        cipher_text = ord(letter) + key
                        encrypted_pass += str(cipher_text).split(',')
                    file.write("\npassword: ")
                    file.write(str(encrypted_pass)+ "\n")

                    decrypted_pass = ""

                    for number in encrypted_pass :
                        plain_text = chr(int(number) - key)
                        decrypted_pass += str(plain_text)
                    
                    return decrypted_pass

                    break


        def reg() :     #function for register
            while True :
                register = input("Please enter your username:  ")  
                if len(register)<= 8 :
                    print("your username should be alphabetical only and greater than 8 character")
                elif register.isalpha()== False:
                    print("your username should be alphabetical only and greater than 8 character")
                elif len(register) >= 8 and register.isalpha()== True :
                    print("username created, your username:", register)
                    encrypted_reg = []
                    for letter in register :
                        cipher_text = ord(letter) + key
                        encrypted_reg += str(cipher_text).split(',')
                    file.write("username register: ")
                    file.write(str(encrypted_reg)+ "\n")


                    decrypted_reg = ""
                    for number in encrypted_reg :
                        plain_text = chr(int(number) - key)
                        decrypted_reg += str(plain_text)
                    
                    #get password
                    decrypted_pass = passwords()
                    
                    #re-login to check account   
                    while True: 
                        reg1 = input("Please re-enter your username:  ")
                        if reg1 == decrypted_reg :
                            print("username exist")
                            break
                        elif reg1 != decrypted_reg :
                            print("username doesn't exist")

                    while True:
                        pass2 = input("Please re-enter your password:  ")
                        if pass2 == decrypted_pass :
                            print("password match, account signed in")
                            break

                        elif pass2 != decrypted_pass :
                            print("password not match, try again")
                            
                    break         



        def log (): #function for login
            while True :
                login = input("Please enter your username:  ")
                if len(login)<= 8 :
                    print("your username should be alphabetical only and greater than 8 character")
                elif login.isalpha()== False:
                    print("your username should be alphabetical only and greater than 8 character")
                elif len(login) >= 8 and login.isalpha()== True :
                    print("username entered, your username:", login)
                    encrypted_log = []
                    for letter in login :
                        cipher_text = ord(letter) + key
                        encrypted_log += str(cipher_text).split(',')
                    file.write("username log in: ")
                    file.write(str(encrypted_log))

                    decrypted_log = ""
                    for number in encrypted_log :
                        plain_text = chr(int(number) - key)
                        decrypted_log += str(plain_text)
                    
                    while True: 
                        reg1 = input("Please re-enter your username:  ")
                        if reg1 == decrypted_log :
                            print("username exist")
                            break
                        elif reg1 != decrypted_log :
                            print("username doesn't exist")
                    
                    #passwords() to get password from text           
                
                    decrypted_pass = passwords()
                    
                    #re-login after login to check account

                    while True:
                        pass2 = input("Please re-enter your password:  ")
                        if pass2 == decrypted_pass :
                            print("password match, account signed in")
                            break

                        elif pass2 != decrypted_pass :
                            print("password not match, try again")
                            
                    break         
                    
        #ask the user if they have an account
    
        while True :
            user =input("do you have an account? (yes/no): ")
            if user == "yes": #if they have account
                log()
                break
            elif user == "no": #if they don't have account
                reg()
                break
            else :
                print('do you have an account? please type yes/no): ')
                


# In[6]:


#sign_in()

