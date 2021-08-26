import re

text = """
<li>THis is line 1</li>
<li>this is line 2</li>
<li>line 3 is different</li>
"""

regex_ = r"<li> \b(?=\w)" + re.escape("line 3") + r"\b(?!\w))<\li>"
# re.search(r'Part 1\.(.*?)Part 3', s).group(1)
print (re.search(regex_, text, re.IGNORECASE))
