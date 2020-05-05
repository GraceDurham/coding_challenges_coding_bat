


def sum67(nums):

  """ Return the sum of the numbers in the array,  except ignore
      sections of numbers starting with a 6 and extending to the 
      next 7 (every 6 will be followed by at least one 7). Return 0
      for no numbers."""

  skip = False
  sums = 0

  for num in nums:
    if (num == 6):
      skip = True
      continue

    if (num == 7 and skip is True):
      skip = False
      continue

    if (skip is False):
      sums = sums + num

  return sums
      
print(sum67([1,2,2])) 
print(sum67([1, 2, 2, 6, 99, 99, 7]))
print(sum67([1, 1, 6, 7, 2]))
print(sum67([1,6,2,2,7,1,6,99,99,7]))
print(sum67([1,6,2,6,2,7,1,6,99,99,7]))
print(sum67([2,7,6,2,6,7,2,7]))
print(sum67([2,7,6,2,6,2,7]))
print(sum67([1,6,7,7]))
print(sum67([6,7,1,6,7,7]))
print(sum67([6,8,1,6,7]))
print(sum67([]))
print(sum67([6,7,11]))
print(sum67([11,6,7,11]))
print(sum67([2,2,6,7,7]))