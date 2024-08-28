import re

text = 'The quick brown fox jump over the lazy dog'

x = re.search('^The.*dog$',text)

if x:
          print('yes')
else:
          print('no')