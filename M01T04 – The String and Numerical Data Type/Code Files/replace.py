# Below is a single sentence with ! and ! will be replaced by a space " "

sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog."

# Replace all occurrences of "I" with " "

new_sentence = sentence.replace("!", " ")
print(f"Original: {sentence}")
print(f"Replaced all: {new_sentence}")

# make all the letters in the sentence upper case

uppercase_sentence = new_sentence.upper()

print(uppercase_sentence)

# writing the sentence in reverse 

reverse_sentence = sentence[::-1]

print(reverse_sentence)