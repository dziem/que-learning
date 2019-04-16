f = open('DataTugas3ML2019.txt', 'r')
x = f.read().split('\n')
f.close()
z = []
for i in x:
	a = i.split('\t')
	z.append(a)
print(z)