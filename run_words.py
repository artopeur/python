import modules.in_and_out as io
import modules.questions as q


test = io.read_categorized("./test2_db")
test.sort()
io.print_word_list(test)
print("\n\n")

sentenses = io.get_saved_from_database("./text_db")
sentenses2 = io.get_saved_from_database("./test_db")

sentense_array = io.transform_sentenses_to_list(sentenses)
sentense_array = sentense_array + io.transform_sentenses_to_list(sentenses2)

print(sentense_array)
print("\n\n")
word_array = []
for sentense in sentense_array:
    word_array = word_array + io.transform_text_to_array(sentense)
print(word_array)
categorized = io.categorize_word_list(word_array)
print("\n\n")
print(categorized)

res = q.write_question(["Are you there?", "How is this going?"])
#res = q.write_question(sentense_array)
print("\n\n")
print(res)
categorized = []
for sentense in res:
    word_array = word_array + io.transform_text_to_array(sentense)
print(word_array)
test = test + io.categorize_word_list(categorized)
test.sort()
test = io.clear_duplicates(test)
print("\n\n")
print(test)