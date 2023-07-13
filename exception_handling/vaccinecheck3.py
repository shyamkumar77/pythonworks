# create function for vaccination eligible or not
# if not eligible create error

def vaccination(age):
    if age>=18:
        print("eligible for vaccination")
    else:
        raise Exception("not eligible for vaccination")

#vaccination(22)
vaccination(12)
