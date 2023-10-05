# n1=0
# n2=1
# count=2

# if nterms<=0:
#     print("Please enter an Positive Integer")
# elifnterms==1:
#     print("Fibonacci Series upto",":")
#     print(n1)
# else:
#     print("Fibonacci Series upto",":")
#     print(n1,n2,",",end=",")
#     while count <nterms:
#         nth =n1+n2
#         print(nth,end=',')

#         n1=n2
#         n2=nth
#         count+=1


n1 = 0
n2 = 1
count = 2

nterms = int(input("Enter the number of terms: "))

if nterms <= 0:
    print("Please enter a positive integer")
elif nterms == 1:
    print("Fibonacci sequence up to", nterms, ":")
    print(n1)
else:
    print("Fibonacci sequence up to", nterms, ":")
    print(n1, ",", n2, end=',')

    while count < nterms:
        nth = n1 + n2
        print(nth, end=',')
        n1 = n2
        n2 = nth
        count += 1







def fibonacci(n):
    fib_seq = [0, 1]
    for i in range(2, n):
        fib_seq.append(fib_seq[i-1] + fib_seq[i-2])
    return fib_seq

n = int(input("Enter the number of Fibonacci numbers to generate: "))
print(fibonacci(n))