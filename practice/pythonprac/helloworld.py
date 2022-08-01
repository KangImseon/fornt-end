# helloWorld.py

from os import pread


msg = "hellggggo world"
print(msg)

a = 1
b = 2

print("sum",a+b)

##파이선에서는 문자와 숫자를 더하면 에러가 납니다.

a_list = ['apple','peach']

print(a_list)

a_list.append('melon')
print(a_list)

a_dict = {'name':'sean','age':28}
print(a_dict['name'])
a_dict['height'] = 158
print(a_dict)

#함수사용
def sum(num1,num2):
    return num1+num2
result = sum(2,3)
print(result)

def sumtest(num1,num2):
    print('ass')
    return num1+num2
result01 = sumtest(2,3)
print(result01)
#함수사용 - if 편 들여쓰기 에러 조심할것.
def is_adult(age):
    if age > 20 :
        print('성인')
    else :
        print('성인X')
is_adult(20)



#리스트 예제 - for
fruits = ['사과','배','배','감','수박','귤','딸기','사과','배','수박']
applecount = 0
for fruit in fruits:
    print(fruit) ##과일 리스트
    if fruit == '사과':
        applecount += 1

print(applecount) ##사과 갯수


#딕셔너리 예제
people = [{'name': 'bob', 'age': 20}, 
          {'name': 'carry', 'age': 38},
          {'name': 'john', 'age': 7},
          {'name': 'smith', 'age': 17},
          {'name': 'ben', 'age': 27}]


for person in people:
    print(person['name'])