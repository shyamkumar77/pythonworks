# decorators: change the working of functions without changing the actual function
#decorator creation:   def decortor_name(single_argument):
#                          def fn_name(arguments used in main fn)
#                                 condtn...
#                                       return argmnt(main fn argmnts)
#
#                          return fn_name

def swapvalue(func):
    def wrapper(a,b):
        if a<b:
            a,b=b,a
            return func(a,b)
        else:
            return func(a,b)
    return wrapper


# subraction of numbers(to remove negative value)
@swapvalue #using created decorator
def subract(n1,n2):
    print(n1-n2)

subract(4,5)
subract(12,18)
subract(18,12)


# division of numbers(to remove small values)
@swapvalue
def division(num1,num2):
    print(num1/num2)

division(4,2)
division(2,4)