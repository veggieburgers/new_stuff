import pyinputplus as pyip
import re


while True:
    prompt = 'Want to know how to keep an idiot busy for hours?\n'
    response = pyip.inputYesNo(prompt)
    if response == 'no':
        break
print('Thank you. Have a nice day.\n')

# Regex alternative
while True:
    if re.compile(r'N.*', re.IGNORECASE).findall(input('Want to know how to keep an idiot busy for hours?\n')):
        print('Thank you. Have a nice day.\n')
        break

# Functionless alternative without dependencies
while True:
    if input('Want to know how to keep an idiot busy for hours?\n').lower() in ['n', 'no']:
        print('Thank you. Have a nice day.\n')
        break
