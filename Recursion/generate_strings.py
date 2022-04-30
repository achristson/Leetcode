"""
let's say you are given a list of single characters
For example chars = ['a', 'b', 'c']
Chars will be non-empty distinct list of single character strings
And also an integer n >= 0
Write a program that prints all strings using those characters
of length exactly n
 
Example:
chars = ['a', 'b', 'c']

n=1
Expected output:
a
b
c

n=2
expected output:
aa
ab
ac
ba
bb
bc
ca
cb
cc

n = 3
Expected output:
aaa
aab
aac
aba
abb
abc
aca
...
cca
ccb
ccc

"""

def generate_strings(chars,n):
    def generate(slate):
        if len(slate) == n:
            print("".join(slate))
            return

        for i in range(len(chars)):
            slate.append(chars[i])
            generate(slate)
            slate.pop()
    generate([])
