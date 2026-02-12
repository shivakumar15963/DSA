## ----------------Find Closest Number to Zero ---------------------##
'''
Given an integer array nums of size n, return the number with the value closest to 0 in nums. If there are multiple answers, return the number with the largest value.

 

Example 1:

Input: nums = [-4,-2,1,4,8]
Output: 1
Explanation:
The distance from -4 to 0 is |-4| = 4.
The distance from -2 to 0 is |-2| = 2.
The distance from 1 to 0 is |1| = 1.
The distance from 4 to 0 is |4| = 4.
The distance from 8 to 0 is |8| = 8.
Thus, the closest number to 0 in the array is 1.
'''




def findClosestNumber(nums: list[int]) -> int:
        closest_num = nums[0]

        for num in nums:
            if abs(num) < abs(closest_num): closest_num = num

        if closest_num < 0 and abs(closest_num) in nums:
            return  abs(closest_num)

        return closest_num  



## ------------------ Merge Strings Alternately -------------------------- ##

'''

You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

 

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r

'''



def mergeAlternately(self, word1: str, word2: str) -> str:
        
        A, B = len(word1),len(word2)
        a,b = 0,0
        word =1
        s = []

        while a<A and b<B:

            if word == 1:
                s.append(word1[a])
                a+=1
                word=2

            else:
                s.append(word2[b])
                b+=1
                word=1

        while a < A:
            s.append(word1[a])
            a+=1
        while b < B:
            s.append(word2[b])
            b+=1   

        return ''.join(s)     




## ------------------  Roman to Integer -------------- ##

'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

 

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.


'''


def romanToInt(s: str) -> int:

        values = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

        total = 0
        n = len(s)
        i = 0

        while i < n:
            # If next value is bigger → subtract
            if i + 1 < n and values[s[i]] < values[s[i + 1]]:
                total += values[s[i + 1]] - values[s[i]]
                i+=2
            else:
                total += values[s[i]]
                i+=1

        return total



## ---------------- Is Subsequence ---------------------- ##

'''
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true

'''

def isSubsequence(s: str, t: str) -> bool:
        S = len(s)
        T = len(t)

        j = 0

        if s == "": return True

        if S > T : return False

        for i in range(T):

            if s[j] == t[i]:

                if j == S -1:
                    return True

                j+=1

        return False            
        
