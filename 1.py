# def add(a,b):
#     return a+b
# print(add(3,5))
# print(add(3.1,5.2))
# print(type(add(3,5)))
# print(type(add(3.1,5.2)))
#
#
# f=open('newone.txt')
# print(f.read(2))
# f.close()
# f=open('newone.txt','a')
# f.write('hello')
# f.close()
# f=open('newone.txt','r')
# print(f.read())
# f=open('newone.txt','a')
# f.write('hai')
# f.close()
# f=open('newone.txt','r')
# print(f.read())
# f=open('text.txt','w')
# f.write(input())
# f.close()
f=open('text.txt','w')
f.write(input())
f.close()
f=open('text.txt','r')
# print(f.read())
a = f.read()
print(a)
count = 0
for j in a:
    if j =='a' or j=='e' or j=='i' or j=='o' or j=='u':
        count += 1
print(count)
word = 1
for j in a:
    if j == ' ':
        word += 1
print(word)








