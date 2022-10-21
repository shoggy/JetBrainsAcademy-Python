import re

# your code here
text = input()
if re.match('[B-N][aeoiu].*', text):
    print('Suitable!')
