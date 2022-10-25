text = input("Enter your text: ").lower()
latter = []

#Show the latter repetition:
latter.append(input("Enter your first latter: ").lower())
latter.append(input("Enter your second latter: ").lower())
latter.append(input("Enter your third latter: ").lower())

latter_repeat1 = text.count(latter[0])
latter_repeat2 = text.count(latter[1])
latter_repeat3 = text.count(latter[2])

print('\n')
print("Latter Repetition:")
print(f"'{latter[0]}' is {latter_repeat1} times")
print(f"'{latter[1]}' is {latter_repeat2} times")
print(f"'{latter[2]}' is {latter_repeat3} times")

#Words Counter:
word_list = text.split()
count_word = len(word_list)

print('\n')
print("Words Count: ")
print(f"There are {count_word} words.")

#Invert Text
word_list.reverse()
inverted_text = " ".join(word_list)
print('\n')
print("Inverted text: ")
print(f"After invertion the text will be '{inverted_text}'")

#Is word 'python' there?
is_python = 'python' in text
dict = {True: 'Yes', False: 'No'}
print('\n')
print("Is word 'python' is there in the text? ")
print(dict[is_python])