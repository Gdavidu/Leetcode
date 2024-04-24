# def decode(message_file):
#     # Read the content of the file
#     with open(message_file, 'r') as file:
#         lines = file.readlines()

#     # Initialize an empty list to store the decoded words
#     decoded_words = []

#     # Iterate over the lines of the file
#     for i, line in enumerate(lines):
#         # Split each line into number and word
#         num, word = line.split()
#         # Convert the number to an integer
#         num = int(num)
#         # Check if the number is part of the pyramid structure
#         if num == (i * (i + 1) // 2) + 1:
#             # Add the word to the list of decoded words
#             decoded_words.append(word)

#     # Join the decoded words into a single string
#     decoded_message = ' '.join(decoded_words)
#     return decoded_message

# # Example usage:

# print(decode('coding_qual_input.txt'))
str = '130 electric'
print(str.split())
