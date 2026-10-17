# try:
#     a=int(input("enter your number:"))
#     result=a/0


# except:
#     print("error occured")

# else:
#     print(result)
# finally:
#     print("code run successfully")            

# ***********************************************
# try:
#     a=int(input("enter your number:"))
#     result=a/3
# except ZeroDivisionError:
#     print("zero division error occures")    





# except:
#     print("error occured")

# else:
#     print(result)

# finally:
#     print("code run successfully")
# ***********************************************

# try:
#     a=[23,45,67,89]
#     a.add(45)
# except:
#     print("error occures")
# else:
#     print(a)
# finally:
#     print("code executed successfully")            

# *************************************************

try:
    a=[23,45,67,89]
    a.append(45)
except AttributeError:
    print(" attribute error occures")
except NameError:
    print("name error occures")
else:    
    print(a)
finally:
    print("code executed successfully")