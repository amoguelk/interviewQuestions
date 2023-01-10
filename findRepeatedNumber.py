def findRepeatedNumber(arr : list[int]) -> int:
  found : list[int] = []
  while True:
    n = arr.pop()
    if found.count(n) > 0: return n
    found.append(n)