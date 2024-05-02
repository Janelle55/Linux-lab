def encryption(plaintext,number):
    New_word=""
    O_word=plaintext.upper()
    for i in range(len(plaintext)):
        ch = O_word[i]
        ascii_code = ord(ch)
        if ch.isalpha():
            if(ascii_code+number<=90):
                ascii_code+=number
                New_word+= chr(ascii_code)
            else:
                ascii_code= ascii_code+number-26
                New_word+= chr(ascii_code)
    return New_word
            
        


plaintext = input("Enter a message: ")
number= int(input("Please enter the number of shifts: "))
message=encryption(plaintext, number)

blocks_per_line = 10
blocks_P = 0
blocks= 5
for i in range(0, len(message), blocks):
    print(message[i:i+blocks], end=" ")
    blocks_P += 1
    if blocks_P % blocks_per_line == 0:print()