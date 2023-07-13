# *
# * *
# * * *
# * * * *

for row in range(5):      #row=0                   #row=1       row=2    row=3
    for col in range(row): #col=0(no looop exist)  #1  col=0    col=0,1  col=0,1,2
        print("*", end=" ") # end used for control to stay in the same line
    print() # to goto next line
