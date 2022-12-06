#Обратный RLE
import re

strng = input()

out = re.sub('(\w)(\d+)', lambda x: x[1]*int(x[2]), strng)
print(out)