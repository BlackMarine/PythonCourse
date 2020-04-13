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
