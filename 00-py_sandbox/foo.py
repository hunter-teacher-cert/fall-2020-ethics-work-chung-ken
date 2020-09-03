#print statement
print("Hello, World!")

#defining and using variables
a, b = 1, 2
print(a+b)

#defining and calling functions
def sampleFunction(arg):
    print("%d + %d = %d" % (a, b, a+b))
    print((arg + ' ') * 3)

sampleFunction("ha!")

#lists 1D and 2D
list1 = [3, "hello", 2.0]
list2 = [["Toph",1], ["DW",2], ["Mike",0]]

print(list1)
print(list1[1])
print(list2[0][0])

#hashmaps (dictionaries)
sample_dic = { 1:"hello", "world":2, "name":"John" }

print(sample_dic)
print(sample_dic[1])
print(sample_dic["world"])
print(sample_dic["name"])
