#Program to display Fibonacci Series(upto nth term)
nterms = int(input("Number of terms you want?"))

#first two terms
n1, n2 = 0, 1
count = 0

#checking if the input is valid
if nterms <= 0:
    print("Please enter a positive integer")
    
#if there is only one term,return n1
elif nterms == 1:
    print("Fibonacci sequence upto",nterms,":")
    print(n1)
    
#generating fibonacci series
else:
    print("Fibonacci series:")
    while count < nterms:
        print(n1)
        nth = n1 + n2
 #updating values
        n1=n2
        n2=nth
        count +=1
        
    
    
