def isPalindrome(string : str) -> bool:
  string = string.lower()
  while len(string) > 0:
    if string[0] != string[len(string) - 1]: return False
    string = string[1:len(string) - 1]
  return True
