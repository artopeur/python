import sys
#print(sys.path)
#sys.path.append('C:\\GIT\\python\\env\\modules')
#import '.\modules\in_and_out.py'
import in_and_out as inout



if __name__ == "__main__":
    #print(sys.path)
    categorized = "./testfile.txt"
    sentenses = "./test_db"
    datafile = "./test2_db"

    test = inout.get_saved_from_database("./test2_db")
    list2 = inout.transform_text_to_array(test)
    #print(list2)
    list_of_words = inout.read_categorized(datafile)
    #print(list_of_words)
    #print(inout.get_saved_from_database("./testfile.txt"))
    number_of_inputs = 0
    print("If you leave the input empty, the program will turn of. Otherwise Input a sentense :) \nHave fun...")
    while 1:
        user_input = input("Give input: ")
        if(user_input != ""):
            print(f"your input was: {user_input}")
            number_of_inputs = number_of_inputs + 1
            print("writing to sentenses::")
            inout.save_to_database(user_input, sentenses)
            print("writing done.")
            uncategorized = inout.get_saved_from_database("./test_db")
            list_of_sentenses = inout.transform_text_to_array(uncategorized)
            print(list_of_sentenses)
            uncategorized_word_list = []
            for sentense in list_of_sentenses:
                print(sentense)
                uncategorized_word_list.append(sentense)
            uncategorized_word_list = inout.clear_duplicates(uncategorized_word_list)
            categorized_word_list = inout.categorize_word_list(uncategorized_word_list)
            #print(uncategorized_word_list)
            categorized_old = inout.read_categorized("testfile.txt")
            categorized_word_list += categorized_old
            categorized_word_list = inout.clear_duplicates(categorized_word_list)
            inout.save_categorized(categorized_word_list, datafile)
            #inout.print_word_list(uncategorized_word_list)
        else:
            break
    
    print(f"\n\nThe number of sentenses were {number_of_inputs}.")
    print("Thank you for using this program.\n\n")
