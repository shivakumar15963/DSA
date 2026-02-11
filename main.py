# ------------  Two Sum II - Input Array Is Sorted ---------------------- #

'''
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]

Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

'''

#numbers: list[int] = [2,7,11,15]
#target: int = 9

def two_sum_sorted(numbers: list[int], target:int) -> list[int]:

    left, right = 0, len(numbers) -1

    while left < right:
        sum_value = numbers[left] + numbers[right]

        if sum_value == target: return [left+1, right+1]

            
        elif sum_value < target: left+=1 
            
                
        else: right -=1  

#print(two_sum_sorted(numbers,target))              



## --------------------- Remove Duplicates from Sorted Array ----------------------- ##

'''
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Consider the number of unique elements in nums to be k​​​​​​​​​​​​​​. After removing duplicates, return the number of unique elements k.

The first k elements of nums should contain the unique numbers in sorted order. The remaining elements beyond index k - 1 can be ignored.

Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.


'''

# nums:list[int] = [0,0,1,1,1,2,2,3,3,4]

def remove_duplicates_inplace(nums:list[int]) -> list[int]:

    if not nums:
        return nums
    slow = 0
    fast = 1

    while fast < len(nums):

        if nums[slow] != nums[fast]:

            slow +=1
            nums[slow] = nums[fast]
            

        fast +=1
    return nums[:slow + 1]    

# print(remove_duplicates_inplace(nums))



## ----------------------- Valid Palindrome -------------------------- ##

'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

'''

import re

# s = "$A man, a plan, a canal: Panama"

def isPalindrome(s: str) -> bool:

    s = re.sub(r'[^a-z0-9]', '', s.lower())
    left, right = 0, len(s) -1

    while left <=right:
        if s[left] != s[right]: return False

        left +=1
        right -=1

    return True

# print(isPalindrome(s))




## -------------------- Container With Most Water ---------------------- ##

'''
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.


'''
height = [1,8,6,2,5,4,8,3,7]

def maxArea(height: list[int]) -> int:
        max_area: int = 0
        left = 0
        right = len(height) -1

        while left < right:

            area = min(height[left], height[right]) * (right -left)

            max_area = max(max_area, area)

            if height[left] < height[right]:
                left +=1
            else:
                right -=1

        return max_area

# print(maxArea(height))


## ----------------------------  Max Number of K-Sum Pairs ---------------------------- ##

'''
You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.

 

Example 1:

Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.


'''
nums = [1,2,3,4]
k = 5
def maxOperations(nums: list[int], k: int) -> int:
        nums: list[int] = sorted(nums)
        left = 0
        right = len(nums) -1
        
        max_operations: int = 0
        while left < right:
            sum = nums[left] + nums[right]
            if sum == k:

                max_operations +=1
                left +=1
                right -=1

            elif sum < k:
                left+=1
            else:
                right -=1        

        return max_operations

# print(maxOperations(nums,k))


## --------------------- Squares of Sorted array -------------- ##

'''
Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]



'''

# nums = [-4,-1,0,3,10]

def sortedSquares(nums: list[int]) -> list[int]:
        n = len(nums)
        left = 0
        right = len(nums) - 1
        pos = len(nums) - 1

        result = [0] * n

        while left <= right:

            if abs(nums[left]) > abs(nums[right]):

                result[pos] = nums[left] **2
                left +=1

            else:

                result[pos] = nums[right] **2
                right -=1

            pos -=1       

        return result   

# print(sortedSquares(nums))  


## ------------------ Reverse the string in place ---------------------- ##

'''
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

 

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

'''

def reverseString(s: list[str]) -> None:
        left = 0
        right = len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1



def reverseVowels(s: str) -> str:
    # Convert string to list because strings are immutable in Python
    chars = list(s)
    vowels = set("aeiouAEIOU")
    left, right = 0, len(chars) - 1
    
    while left < right:
        # Move left pointer until a vowel is found
        while left < right and chars[left] not in vowels:
            left += 1
        
        # Move right pointer until a vowel is found
        while left < right and chars[right] not in vowels:
            right -= 1
        
        # Swap the vowels
        chars[left], chars[right] = chars[right], chars[left]
        
        # Move pointers inward
        left += 1
        right -= 1
        
    return "".join(chars)

print(reverseVowels(s = "IceCreAm"))