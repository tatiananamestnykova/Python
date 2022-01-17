HW_1 = 'Python'
print(HW_1)
name = "Egor" #1.Создать переменную типа String
age = 12 #2.Создать переменную типа Integer
height = 162.5 #3.Создать переменную типа Float
byt = bytes(100) #4.Создать переменную типа Bytes
list = ['Egor', 12, 162.5] #5.Создать переменную типа List
tuple = ('Egor',12, 23.11) #6.Создать переменную типа Tuple
set = {1, 2, 2, 'data', 'data'} #7.Создать переменную типа Set
froz = frozenset({"hello", "Python"}) #8.Создать переменную типа Frozen set
dict = {"one": "This is one"} #9. Создать переменную типа Dict

print('name=',type(name))
print('age=',type(age))
print('height=',type(height))
print('byt=',type(byt))
print('list=',type(list))
print('tuple=',type(tuple))
print('set=',type(set))
print('froz=',type(froz))
print('dict=',type(dict))

country = "Ukraine"
city = "Kharkov"
motherland = country+city
print(motherland)

a = 7
b = 6
c = a + b
print(c)

print('name=',',','age=')

d = a/b
print(d)

print('name=' ,'+', 'age=')

n = a*b
print(n)

k= a/b
print(int(k))

h = a//b
print(int(h))

e = a % b
print(e)

z = (7 + 12) ** 3 + 7 * 4 - 44 / 2 ** 4
print(z) #6884.25