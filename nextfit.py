P= [200,300,400,100];
M= [160, 360, 480, 700];

for i in range (0,4):
    for j in range (0,4):
        if P[i]<=M[j] :
            #print(f'process {i+1} goes into block {j+1}')
            print('process ', (i+1) ,' goes into block ', (j+1))
            M[j] = 0;
            for k in range (0,j):
                M[k] = 0;
            break
        else:
            M[j]=M[j]