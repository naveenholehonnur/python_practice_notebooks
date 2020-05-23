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
            
   



# Question-2

# Alice has a hand of cards, given as array of integers. Now she wants to arrange the cards into groups so that each group of size W and consists of W consecutive cards. Return true if we can split that.
# hand=[1,2,3,6,2,3,4,7,8]
# w=3
# Output: true
# Explanation: [1,2,3],[2,3,4],[6,7,8]
        
        
 # Solution :--

w=int(input('enter group of card size='))
hand = list(map(int,input('enter card numbers=').strip(' []').split(',')))
op = []
for i in range(int(len(hand)/w)):
        temp=sorted(list(set(hand)))
        op.append(temp[:w])
        check = temp[0]
        for j in temp[:w]:
            if check!=j:
                print('false')
                break
            check+=1
            hand.remove(j)
        else:
            continue
        break
else:
    print('true')
    print(op)
    








