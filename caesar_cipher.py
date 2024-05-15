alphabet="abcdefghijklmnopqrstuvwxyz"
alphabets=list(alphabet)
# direction=input("type 'encode for encrypt,type 'decode' to decrypt \n")
# text=input("write your message \n")
# shift=int(input("type the shift you want"))
def caesar(start_text,shift_amount,cipher_direction):
    end_text= ""
    if cipher_direction=='decode':
        shift_amount *= -1
    for char in start_text:
            if char in alphabets:
                postion =alphabets.index(char)
                new_position=postion +shift_amount
                end_text += alphabets[new_position]
            else:
                 end_text += char

    print(f"here's the {direction}d result:{end_text}")
should_continue=True
while should_continue:   
    direction=input("type 'encode for encrypt,type 'decode' to decrypt \n")
    text=input("write your message \n")
    shift=int(input("type the shift you want"))
    shift=shift%26
    caesar(start_text=text,shift_amount=shift,cipher_direction=direction)
    result =input("do you want  to go again 'yes' , 'no'")
    if result =="no":
         should_continue =False
         print("thank you ")