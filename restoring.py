def add(A,M):
    carry = 0
    Sum = ''
    for i in range(len(A)-1,-1,-1):
        temp = int(A[i])+int(M[i])+carry
        if temp>1:
            Sum += str(temp%2)
            carry = 1 
        else:
            Sum += str(temp) 
            carry = 0 
    return Sum[::-1]
    
def compliment(m):
    M = ''
    for i in range(0,len(m)):
        M += str((int(m[i])+1)%2)
    M = add(M,'0001')
    return M 
    
def restoring(Q,M,A):
    count = len(A)
    print("initial values :A ",A," Q:",Q," M:",M)
    while count:
        A = A[1:] + Q[0]
        comp_M = compliment(M)
        A = add(A, comp_M)
        if A[0] == '1':
            Q = Q[1:] + '0'
            A = add(A,M)
        else:
            Q = Q[1:] + '1'
        count -= 1 
    print('\nQuotient(Q): ',Q," Remainder(A): ",A) 
    
dividend = input("enter dividend: ")
divisor = input("enter divisor: ")
accumulator = '0'*len(dividend)
restoring(dividend,divisor,accumulator)