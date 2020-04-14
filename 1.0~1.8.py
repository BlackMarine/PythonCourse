#1.0
a_string = "Like this"
a_number = 2
a_float = 3.14
a_boolean = False
e_none = None
#파이썬에만 있음 "존재하지않음" 

a = 1
b = 3

print(a+b)
print(type(a_string))
print(type(a_number))
print(type(a_float))
print(type(a_boolean))
print(type(e_none))

# snake case임 
# 언더바는 파이썬 약속임 super_long_variable 처럼
# 만약 자바라면 superLongVariable 


#1.1 #mutable 변경가능한것! lsit {dictionary}
days = ["Mon","Tue","Wed","Thur","Fri"]
days.append("Sat") 
print(days)
days.reverse()
print(days)

#1.2 immutable 변경불가능한것! tuple

print(days)
tuples = ("ddMon","Tue","Wed","Thur","Fri")
print(tuples)
#dictionary 안에 리스트로 넣어줌 
nico = {
"name" : "Nico",
"age" : 29,
"korean" : True,
"fav_food" : ["Kimchi", "Sashimi"]
}

print(nico)
nico["handsome"] = True
print(nico)

#1.3 built-in functions 이해하기 print() len() type()
#int bool str 
age = "18"
print(age)
print(type(age)) # str 18

n_age = int(age)
print(n_age)
print(type(n_age)) # str 18

nico2 = {age:44} 
print(nico2)

#1.4 함수 정의 하는방법
def say_hello():
  print("hello")
  print("bye")
say_hello()
say_hello()


#1.5 def 함수 옆 (argument인자)
#def say_hello(who)):
#  print("hello", who)
#
#say_hello()

def say_hello(name="anonymous"): #default 값설정하기
  print("hello",name)

say_hello()
say_hello("nico")

#1.6 return 함수결과를 저장하고싶을때
print("@@@@@@@@@@@@@@@@@@")
def p_plus (a, b):
  print(a + b)

def r_plus(a, b):
  return a + b
  print("리턴한 후 함수는 종료됨 이거 출력 안됨")


p_result = p_plus(2, 3) #프린트 p_plus를 했을 뿐 저장x
r_result = r_plus(2, 3) #return a + b 이거로 값을 저장함

print(p_result, r_result)
   #       None   5

#1.7 하트
#1.8 keyworded Arguments

def plus (a, b):
  return a+b;

result = plus(2,4)
print(result)

# 키워드 알규먼트로 인자(argument) 이용가능
result = plus(b=30, a=1)
print(result)


#string 앞에 f 붙여서 format 하기
def say_hello2(name, age):
  return "hello name you are age years old"

hello = say_hello2("nico","12")
print(hello)

# name 이랑 age를 string이 아닌 f 랑 {}로 사용해야함
def say_hello3(name, age):
  return f"hello {name} you are {age} years old"

hello = say_hello3(name = "nico",age="12")
print(hello)