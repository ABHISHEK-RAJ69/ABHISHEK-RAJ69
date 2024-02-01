def palindrome(a): 
    k=a
    rev=0
    while k>0:
        rev=rev*10+(k%10)
        k=k//10
    if a==rev:
        print ("It's a palindrom ")
    else :
        print ("It's not a  palindrom ")
n=int(input ("enter a numer you want to check for palindrome "))
palindrome(n)
