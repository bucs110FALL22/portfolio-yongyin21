class StringUtility:
  def __init__ (self,string):
    self.string = string
  
  def __str__(self):
    result_str = self.string
    return result_str

  def vowels(self):
    numvowels = 0
    for i in self.string:
      if i in ["a","e","i", "o", "u","A","E","I","O","U"]:
        numvowels = numvowels + 1
    if numvowels >=5 :
      numvowels = "many"
      return numvowels
    elif numvowels < 5:
      return str(numvowels)
      
  def bothEnds(self):
    if len(self.string) <= 2:
      return ""
    else:
     stringx = self.string[0:2] + self.string[-2:]
    return stringx
    
  def fixStart(self):
    if len(self.string) <= 1:
      return self.string
    firstlet = self.string[0]
    count = 0
    for chr in self.string:
      if chr in firstlet:
        count += 1 
    if count <= 1 :
      return self.string
    else:
      for i in range(len(self.string)+1):
        stringx = self.string.replace(firstlet,"*")
        stringy = firstlet + stringx[1:len(stringx)+1]
        return stringy
        
  def asciiSum(self):
    total = 0
    for i in range(len(self.string)):
      total = total + ord(self.string[i])
    return total
    
  def cipher(self):
    result = ""
    shift =len(self.string)
    for i in range(len(self.string)):
      if self.string[i].islower():
        value = (((( (ord(self.string[i])) - 97)+shift) %26)+97)
        result += chr(value)
      elif self.string[i].isupper():
        value1 = (((( (ord(self.string[i])) - 65)+shift) %26)+65)
        result += chr(value1)
      else:
        result += self.string[i]
    return result