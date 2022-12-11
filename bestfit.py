P = [200, 300, 600, 400]
M = [700, 500, 200, 100, 600]

for i in range (4):
    size = []
    for j in range(5):
        if M[j]>= P[i]:
            size.append(M[j]-P[i])
        else:
            size.append(999)
    a = size.index(min(size))
    print('Process', i+1, 'goes into block', a+1)
    M[a]=M[a]-P[i]