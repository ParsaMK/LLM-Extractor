
with open("./processed_texts/KID2.txt", "r") as file:
    text = file.read()


# approximately each token is 4 characters long
num_tokens = len(text)/4

print(num_tokens)