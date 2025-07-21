a = [1,2,3,4]
print(type(a))

#implicit : Python automatically converts the type
#explicit : you need to manually convert the type

#implicit
print(4+5.5)
#here 4 is automatically converted to float datatype

#explicit
a = '54'
print(int(a))
#typeconversion is not a permanent process doesnt alter the value of the original variable 
print(a)
print(float('4'))
print(list('Hello'))