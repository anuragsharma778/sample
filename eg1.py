'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
t=int(raw_input())
for i in range(t):
    n=int(raw_input())
    a=list(map(int,raw_input().split()))[:n]
    k=a
    print k
    a.sort()
    print a
    min=1000
    for i in range(n):
        for j in range(i,n):
            if i!=j:
                k=(a[i] and a[j])^(a[i] or a[j])
                if k<min:
                    print "Comparing ",a[i],'and ',a[j],' value = ',k
                    min=k
    print k
