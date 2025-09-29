fruit = ['사과' , '배' , '오렌지' , '바나나']

print(fruit[0])
print(fruit[-4])
print(fruit[-3])
print(fruit[-1])

print(fruit[0:])

fruit1 = ['사과','포도' ,'오렌지']
fruit2 = ['수박','귤' ,'바나나']

print(fruit1 + fruit2)
print(fruit1*3)
print('포도' in fruit1)
print('자몽' not in fruit2)

fruit.append('자몽')
print(fruit)
fruit.remove('바나나')
print(fruit)
del(fruit[2])
print(fruit)
fruit[0] = '수박2'
print(fruit)

foo = [7,3,5,2,1]
print(sorted(foo))
print(sorted(foo , reverse=True))

print(foo.index(5))

foo1 = ('a','b','c')

print(foo1[0])
print(foo1[:2])


price ={ '짜장면' : 6000 , '짬뽕' : 7000 , "탕수육" : 20000}

print(price['짜장면'])
price['짬뽕밥'] = 7500

del(price['짬뽕'])
print(price)

print(list(price.keys()))
print(list(price.values()))
print(list(price.items()))