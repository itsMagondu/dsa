# With characters {} () [],  firnd if the string is balanced.
# () is balanced
# ([]) is balanced.
# () [] is balanced too.

class BalanedParenthesis:
  def __init__(self):
    self.stack = []

  def compare(self, opening_char, closing_char):
    if opening_char == '(': 
      return closing_char == ')'
    elif opening_char == '[':
      return closing_char == ']'
    elif opening_char == '{': 
      return closing_char == '}'
    else: 
      print ('error: ', opening_char, closing_char)

  def check(self, s):
    # Loop through each item and add opening characters in a stack.
    # If you see a closing character, then pop and compare. If not matching, return false
    # If stack empty when there exists a closing character, return false.
    # Else return true.
    for item in s:
      if item in ['{', '(', '[']:
        self.stack.append(item)
      elif item in ['}', ')', ']']:
        if len(self.stack) == 0:
          return False

        opening_char = self.stack.pop()
        if not self.compare(opening_char, item):
          return False

    # Finished looping and stack is not empty
    return len(self.stack) == 0

# Successful tests
bp = BalanedParenthesis()
print ('test1', bp.check(''))

bp = BalanedParenthesis()
print ('test2', bp.check('[]'))

bp = BalanedParenthesis()
print ('test3', bp.check('[()]'))

bp = BalanedParenthesis()
print ('test4', bp.check('()[][]'))

# Should fail
bp = BalanedParenthesis()
print ('test5', bp.check('[(})]'))

bp = BalanedParenthesis()
print ('test6', bp.check('()[]]'))

bp = BalanedParenthesis()
print ('test7', bp.check('[()]}'))

bp = BalanedParenthesis()
print ('test8', bp.check('()[][]('))