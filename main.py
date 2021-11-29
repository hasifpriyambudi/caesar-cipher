from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

def caesar(text,shift,direction):
    if shift>=len(alphabet):
        shift %= len(alphabet)

    if direction=="decode":
        shift = -shift
        
    endText = ""
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)+shift
            endText += alphabet[position]
        else:
            endText += char

    print(f"The text is {endText}\n")

run = True
while run:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text,shift,direction)
    run = input("Type 'yes' if you want to go again.\n")

    if run != "yes":
        run = False