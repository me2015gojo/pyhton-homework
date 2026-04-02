ch= input('enter a character:')
i=0
found=False
while i <= 127:
    if chr(i)==ch:
        print('ACSII value is:',i)
        found=True
        break
    i+=1
if not found:
    print('character not found in ACSII range')