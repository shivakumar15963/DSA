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

nums:list[int] = [0,0,1,1,1,2,2,3,3,4]

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

print(remove_duplicates_inplace(nums))