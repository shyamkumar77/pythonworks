# continue: it skips the current iteration


# for i in range(5):
#     if(i==2):
#         continue
#     print(i)

# in while
#exmp1:

# i=1
# while i<=5:
#     if(i==2):# if this condtn true then icremnt dont work
#         continue
#     print(i)
#     i=i+1

#exmp2:

# i=1
# while(i<=5):
#     i=i+1  #icrmnt stmnt before continue works
#     if(i==2):
#         continue
#     print(i)
print("*"*100)


for i in range(5):
    for j in range(5):
        if(i==3):
            break  # it breaks j loop
    break  # it breaks i loop

