print("Question1")
list=[]
for i in range(10):
    num=input("Enter values %d" %(i+1))
    list.append(num)
for value in list:
    print("Values are:",value)
print('*'*10)
print('\n')


print("Question2")
while True:
    print("Hiiii")
print('*'*10)
print('\n')


print("Question3")
list1=[]
number=int(input("Enter input"))
for i in range(number):
    num=int(input("Enter values"))
    list1.append(num)
print("First List",list1)
list2=[]
for i in list1:
    list2.append(i*i)
print("Squared values",list2)
print('*'*10)
print('\n')


print("Question4")
list3=[2,'a','b',3.2,5,6.7,'c','d']
list_str=[]
list_int=[]
list_float=[]
for i in list3:
    if(type(i)==str):
        list_str.append(i)
    elif(type(i)==int):
        list_int.append(i)
    elif(type(i)==float):
        list_float.append(i)
print("String List",list_str)
print("Integer List",list_int)
print("Float List",list_float)
print('*'*10)
print('\n')


print("Question5")
list4=[]
for i in range(1,101):
    list4.append(i)
even_list=[]
odd_list=[]
list5=[]
for k in list4:
    if(k%2==0):
        even_list.append(k)
    else:
        odd_list.append(k)
list5=even_list+odd_list
print("Combined List:",list5)
print('*'*10)
print('\n')


print("Question6")
for i in range(4):
    i=i+1
    print('*'*i)
print('*'*10)
print('\n')


