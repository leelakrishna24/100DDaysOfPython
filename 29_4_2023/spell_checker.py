from textblob import TextBlob

word = input("Enter a word : ")

txt = TextBlob(word)

# using correct() method
txt = txt.correct()

print(txt)







# word = word.correct()
# if word in corrector:
#     print("correct")
# else:
#     correct_word = corrector.correction(word)
#     print("Correct spelling is", correct_word)