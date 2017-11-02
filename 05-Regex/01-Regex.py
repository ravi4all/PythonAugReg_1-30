import re

str = "Id of Ram is ram123@gmail.com and id of shyam is shyam.11_xyz@gmail.com and id of mukesh is mukesh_sharma_1212@yahoo.co.in"

# pattern = re.findall('[^A-Z\s][\w.]+@+[\w.]+', str)
# print(pattern)

# email = input("Enter your mail id : ")
pattern = '[^A-Z][\w.]+@+[\w.]+'
match = re.search(pattern, str)
if match:
    print("Pattern Match...")
    print(re.findall(pattern, str))
else:
    print("Pattern not match...")
