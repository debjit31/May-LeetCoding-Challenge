# Input: Get 3 strings in 3 lines as input

# Hello

# Hi

# Good Morning



# Output:

# In the 1st string, replace the vowels with '$', in the 2nd string replace the consonants with '#' and for the 3rd string replace the upper case into lower and lower case into upper. And print these converted string in a single line as output.

# H $ll$ #i gOOD mORNING



a = list(input())
b = list(input())
c = list(input())
ans=""
for i in range(len(a)):
	if a[i]  in 'aeiou' or a[i] in 'AEIOU':
		a[i] = '$';
ans += "".join(a)
for i in range(len(b)):
	if b[i] not in  'aeiou' and b[i] not in 'AEIOU' :
		b[i] = '#';
ans += "".join(b)
for i in range(len(c)):
	if c[i].islower():
		c[i] = c[i].upper()
	else:
		c[i] = c[i].lower()
ans += "".join(c)
print(ans)
		







