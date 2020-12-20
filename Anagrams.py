str1 = 'listen'
str2 = 'silent'
print('The strings are anagrams.' * (sorted(str1) == sorted(str2)) + "The strings aren't anagrams." * (sorted(str1) != sorted(str2)))
