# wap to calculate the root of the numbers using map funciton

def calculateSqaure(n):
    return n**2

list_of_numbers=[2,3,4,5,6,8]
sqaures=list(map(calculateSqaure,list_of_numbers))
print(f'The sqaures of {list_of_numbers} is {sqaures}')
