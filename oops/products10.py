# create object for product.txt
# refer product.txt

class Products:
    def __init__(self,id,name,price):
        self.id=id
        self.name=name
        self.price=price

    def printvalues(self):
        print(self.id,self.name,self.price)

f=open('products.txt','r')
max=0
for i in f:
    data=i.rstrip("\n").split(",")
    #print(data)
    id=data[0]
    name=data[1]
    price=data[2]

    product1=Products(id,name,price)
    product1.printvalues()
#find product with max price
    price=int(product1.price)  #bcoz data from text file will always be string
    if price>max:
        max=price

print(max)





