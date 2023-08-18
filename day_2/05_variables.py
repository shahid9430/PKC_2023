samosa = ('maida','sabz mirch','aalo', 'podeena', 'waghera')
# Pros
# it reduces the human effort
# easy to recal
# easy to write for long databases

# strategies
#1 don't use reserve words as variables
#2 don't use varibales names with spaces instead use underscore(_)
#3 don't use more than two words
#4 don't use special characters
#5 do not use numbers at the beginning
#6 do not capatalize
#7 meaningful
# 8 follow global trends such as (df= dataframe)
# 9 don't even repeat the same variable
# 10 do not use operators (+,-,/,*,**,%)
# 11 do not use "" or '' in variables

x= 2+1
fruit_basket = ("apple", "banana","mangoe","melon")
print(fruit_basket)
print(type(fruit_basket))

print (x)
print(type(x))
print (samosa)
print(type(samosa))

# typecasting in python
# lets take a variable
x= '12'
print(type(x))             #x is a string data type

x1= int(x)     # here we convert the previous x varibale to int and store it in x1
print(type(x1))
