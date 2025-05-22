# -----------------------Using while loop --------------#

# def isPalindrome(str):
#     left = 0
#     right = len(str) - 1

#     while left <= right:
#         if str[left] != str[right]:
#             return False
#         left += 1
#         right -= 1
#     return True

# print(isPalindrome('racecar'))
# print(isPalindrome('dad'))
# print(isPalindrome('son'))


# ---------------------Using Recursion -----------------#
def isPalindrome(str):
    if len(str) <= 1:
        return True
    
    if str[0] != str[-1]:
        return False
    return isPalindrome(str[1:-1])


print(isPalindrome('racecar'))
print(isPalindrome('121'))

# ---------------------Using Python one Liner -----------------#

# def isPalindrome(str):
#     if str == str[::-1]:
#         return True
#     return False
    
# print(isPalindrome('mom'))
# print(isPalindrome('son'))
# print(isPalindrome('121'))


#------------------------------isPalindrome for numbers ------------#
def isPalindrome(num):
    if 0 <= num <= 9:
        return True
    
    result = 0
    result += num % 10
    num = num // 10
    return isPalindrome(num)

print(isPalindrome(122))