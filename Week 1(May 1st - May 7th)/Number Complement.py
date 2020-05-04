# Number Complement
# Given a positive integer, output its complement number. The complement strategy is to flip 
# the bits of its binary representation.

# Example 1:
# Input: 5
# Output: 2
# Explanation: The binary representation of 5 is 101 (no leading zero bits),
# and its complement is 010. So you need to output 2.
 
# Example 2:
# Input: 1
# Output: 0
# Explanation: The binary representation of 1 is 1 (no leading zero bits),
# and its complement is 0. So you need to output 0

def findComplement(num):
    binary = bin(num)[2:]
    comp = ""
    for i in binary:
        if i == '1':
            comp += '0'
        else:
            comp += '1'
    return int(comp, 2)

if __name__ == "__main__":
	num = int(input())
	comp = findComplement(num)
	print(comp)