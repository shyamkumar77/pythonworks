# index out of range prblm

l=[1,2,3]

index=int(input("enter the index:"))
# try:
#     print(l[index])
# except:
#     print("index over")
#
#######################################################################################


try:
    print(l[index])
except Exception as e: # calling Exception module, to know for user which error has occured
    #print("index over")
    print(e)