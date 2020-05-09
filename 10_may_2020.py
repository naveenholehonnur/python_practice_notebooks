# Given two binary strings return their sum (in binary). Input strings are not non empty and contains onlu characters 1 or 0.
# Input: a='11',b='1'
# Output: "100"

# Input: a='1010' b='1011'
# Output: "10101"

# Solution :--
    
a=input()
b=input()
a_len,b_len=len(a),len(b)
if a_len<b_len:
    a='0'*(b_len-a_len)+a
if b_len<a_len:
    b='0'*(a_len-b_len)+b
op,carry='',0
for i in zip(a[::-1],b[::-1]):
    val=sum(list(map(int,i)))+carry
    if val%2==0:
        op='0'+op
    else:
        op='1'+op
    carry=0
    if val>1:
        ex=1
print((str(carry)+op).lstrip('0'))
