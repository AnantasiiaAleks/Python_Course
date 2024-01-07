q,*w, e = (11, 22, 33, 44, 55)
print(q)
print(w)
print(e)

q,*w, e = (11, 22, 33)
print(q)
print(w)
print(e)

q,*w, e = (11, 22)
print(q)
print(w)
print(e)

my_list = [(1,2,3,4,5), (11,22,33), (111,222)]
for q,w,*e in my_list:
    print(q,w,e, sep=' -\\- ')