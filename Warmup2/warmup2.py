#################################
# Warmup-2
# Desription: Medium warmup string/list problems with loops (solutions available)
# Author : Igor Kurchatov 5/12/2016
#################################

#Given a string and a non-negative int n, return a larger string that is n copies of the original string.
def string_times(str, n):
  if n < 0:
    return ""
  return str * n

#Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, 
#or whatever is there if the string is less than length 3. Return n copies of the front.
def front_times(str, n):
  if n < 0:
    return str
  return str[:3] * n

#Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".
def string_bits(str):
  res = ""
  for i in range(len(str)):
    if i % 2 == 0:
      res = res + str[i]
  return res

#Given a non-empty string like "Code" return a string like "CCoCodCode".
def string_splosion(str):
  res = ""  
  for i in range(len(str)):
    res = res + str[:i+1]
  return res

#Given a string, return the count of the number of times that a substring length 2 appears in the string 
#and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).
def last2(str):
  
  if len(str) < 2:
    return 0
  
  l = str[len(str)-2:]  
  cnt = 0
  
  for i in range(len(str)-2):
    s = str[i:i+2]
    if s == l:
      cnt = cnt + 1
  return cnt

#Given an array of ints, return the number of 9's in the array.
def array_count9(nums):
  cnt = 0
  for val in nums:
    if val == 9:
      cnt = cnt + 1
  return cnt

#Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.
def array_front9(nums):
  
  l = len(nums)
  if l > 4:
    l = 4
  
  for i in range(l):
    if nums[i] == 9:
      return True

  return False

#Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.
def array123(nums):
  for i in range(len(nums)-2):
    if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
      return True
  return False

#Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. 
#So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.
def string_match(a, b):
  cnt = 0
  for i in range(len(a)-1):
    astr = a[i:i+2]
    #for j in range(len(b)-1):
    bstr = b[i:i+2]
    if astr == bstr:
      cnt = cnt + 1
  return cnt

