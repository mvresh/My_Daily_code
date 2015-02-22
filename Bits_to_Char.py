text = open("file.txt").read()
text = text.replace("\n","")

chars = []
for i in range(0,len(text),8):
    digits = text[i:i+8] // taking digits as a bunch of 8
    num = int(digits,2)
    char = chr(num) //converts to ascii character
    chars.append(char)
   
 result = "".join(chars)
 print(result)
