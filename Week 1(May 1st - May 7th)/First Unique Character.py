#  First Unique Character in a String
# Solution
# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

# Examples:

# s = "leetcode"
# return 0.

# s = "loveleetcode",
# return 2.
# Note: You may assume the string contain only lowercase letters.

def firstUniqChar(s):
    if s == "":
        return -1
    flag = 0
    for i in range(len(s)):
        if s.count(s[i]) == 1:
            flag = 1
            return i
            break
    if flag == 0:
        return -1

if __name__ == "__main__":
	s = input()
	re = firstUniqChar(s)
	print(re)
    