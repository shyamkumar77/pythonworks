

# decorator
def agecheck(func): #func: related as below fns name
    def wrapper(a,b):
        if b<18:
            raise Exception("not eligible") #raising error
        else:
            return func(a,b) #otherwise fn gets executed
    return wrapper



# raise 'not eligible for age<18'

@agecheck
def vaccination(name,age):
    print("vaccinated successfully")

vaccination("shyam",21)
vaccination("anu",17)


@agecheck
def driving_license(name,age):
    print("you can take test")

driving_license("arjun",25)
driving_license("arun",15)



