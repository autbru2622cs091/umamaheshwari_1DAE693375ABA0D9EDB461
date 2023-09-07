# online python compiler(interpreter) to run python online.
#write python 3 code in this online editor and run it.
def fact(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n * fact(n - 1)


print(fact(5))