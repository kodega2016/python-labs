# wap to filter the prime numbers only from a list of numbers.
def checkIfNumIsPrime(n):
    if n<=1:
        return False
    for i in range (2,n):
        if n%i==0:
            return False
    return True

numbers=[12,34,9,7,12,54,3,11,17]
prime_numbers_only=list(filter(checkIfNumIsPrime,numbers))
print(f'The prime numbers are:{prime_numbers_only}')
