# def sumOfList():
#     nums=[2,4,5,2,4]
#     print(nums[0]+nums[1]+nums[2]+nums[3]+nums[4])

# sumOfList()

# def sum(numbers):
#     total=0
#     for n in numbers:
#         total+=n
#     return total

# print(sum((1,3,4,5,3)))

# def largest(a,b,c):
#     if a > b and a > c:
#         print(a," is the greatest number")
#     elif b > a and b > c:
#         print(b," is the greatest number")
#     else:
#         print(c," is the greatest number")

# largest(3,5,2)

# numList=[]
# def evenNums(numbers):
#     for n in numbers:
#         if n % 2 == 0:
#             numList.append(n)

# evenNums((24,53,8,9,3,45,12,72,5,4))
# print(numList)

# def inOrOutRange(num):
#     #if(num<0 or num>10):
#     if num in range(0,11):
#         print(num ," is in the range of 0 and 10")
#     else:
#         print(num ," is out of the range of 0 and 10")

# inOrOutRange(0)
def lowerOrUpper(sentence):
    lowerCount=0
    upperCount=0
    for letters in sentence:
        if letters.islower():
            lowerCount+=1
        elif letters.isupper():
            upperCount+=1
    print(lowerCount)
    print(upperCount)
sentence="Good morning Alexander"
lowerOrUpper(sentence)


