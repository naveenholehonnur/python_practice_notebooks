# Question-1

# Write a program to find the nth super ugly number. Super ugly numbers are postive numbers whose prime factors in the given list primes of size k.
# Input: n=12, primes=[2,7,13,9]
# Output:32
# Explanation: [1,2,4,7,8,13,14,16,19,26,28,32] is the sequence of first 12 super ugly numbers for the given primes.

# Solution :--

n=int(input('enter nth super ugly number='))
primes=list(map(int,input('enter primes=').strip(' []').split(',')))
op=[]
x=1
while True:
    for i in range(2,x):
        if x%i==0:
            if i in primes:
                continue
            elif i not in op:
                break
        else:
            for j in primes:
                if x%j==0:
                    break
            else:
                break
    else:
        op.append(x)
    if len(op)==n:
        break
    x+=1
print(op[n-1])
            
        
        
        
        








