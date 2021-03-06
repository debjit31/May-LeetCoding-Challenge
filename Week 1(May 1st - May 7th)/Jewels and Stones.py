
# Problem Name : - Jewels and Stones

# You're given strings J representing the types of stones that are jewels,
# and S representing the stones you have.  Each character in S is a type of stone you have.
# You want to know how many of the stones you have are also jewels.
# The letters in J are guaranteed distinct, and all characters in J and S are letters. 
# Letters are case sensitive, so "a" is considered a different type of stone from "A".

# TestCases : 
# Input: J = "aA", S = "aAAbbbb"
# Output: 3

# Input: J = "z", S = "ZZ"
# Output: 0

def numJewelsInStones(J,S):
    c=0
    for i in S:
        if J.find(i) >= 0:
            c+=1
    return c
  
if __name__ == "__main__":
	J,S = list(map(str, input().split()))
	res = numJewelsInStones(J,S)
	print(res)