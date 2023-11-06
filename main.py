def factorialofnum(n):
  if (n==0):
    return 1
  else:
    return n*factorialofnum(n-1)

num = int(input("Enter the number : "))
res = factorialofnum(num)
print("The Factorial of",num,"is", res)