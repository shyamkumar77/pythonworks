


def admincheck(func):
    def wrapper(a,b):
        if a!='admin':
            raise Exception("not allowed")
        else:
            return func(a,b)
    return wrapper


# raise 'not eligible', if username other than 'admin'
# ie, only admin is eligible for pin_change
@admincheck
def change_pin(username,pin):
    current_pin=pin
    return current_pin

print(change_pin("admin",4561))
print(change_pin("shyam",2568))

