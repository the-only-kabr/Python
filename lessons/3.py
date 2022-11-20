a=[int(i) for i in input().split()] #list comprehensionb=list(map(int,input().split()))#обычный ввод списка с изменениемnames=input().split(',')#ввод списка с клавиаутры БЕЗ ИЗМЕНЕНИЙ ЕГО ЭЛЕМЕНТОВ

print("Наибольшее число: ", max(a))
