def save_to_database(words, file):
    with open(file, "a") as f:
        #if(words.isalpha()):
        print(words)
        f.write(words + "\n")
    f.close()
    print("written.")

def get_saved_from_database(file):
    #print("read.")
    #text = "this is, a test of luck. Come now."
    with open(file) as f:
        file_input = f.read()
    f.close()
    return file_input

def save_categorized(array_of_words, file):
    with open(file, "w") as f:
        for word in array_of_words:
            #if(word.isalpha()):
            #print(word)
            f.write(word[0] + "|" + str(word[1]) + "|" + str(word[2]) + "|" + str(word[3]) + "\n")
    f.close()
    print("written.")

def read_categorized(file):
    build_list = []
    rowstart = []
    address = []
    row = []
    # test|1|1|2
    
    with open(file) as f:
        data = f.read()
        f.close()
        #print(data)
        nextrow=0
        rowstart.append(0)
        row = []
        for i in range(len(data)):
            if(data[i] == '|'):
                row.append(i)
            elif(data[i] == '\n'):
                nextrow = i
                #row.append(nextrow)
                address.append(row)
                rowstart.append(i+1)
                row = []
    i = 0
    #print(address)
    #print(rowstart)
    #print(len(rowstart))
    #print(len(address))
    count = 0
    for i in range(len(address)):
        #print(data)
        #print(data[rowstart[i] : address[i][0]])
        #build_list.append(data[rowstart[i] : address[i][0]])
        #print(data[address[i][0]+1 : address[i][1]])
        #print()
        build_list.append( [ data[rowstart[i] : address[i][0]], int(data[address[i][0]+1:address[i][1]]), int(data[address[i][1]+1:address[i][2]]) , int(data[address[i][2]+1:address[i][2]+2]) ])
        """
        print(data[address[i][0]+1:address[i][1]])
        print(data[address[i][1]+1:address[i][2]])
        print(data[address[i][2]+1:address[i][2]+2])
        
        #print()
        #"""
        count = count+1
    
    #print(data[0:address[0][2]])
    #print(build_list)
    return build_list
        
 
def is_letter(char):
    return char.isalpha() or char.isdigit()

def transform_text_to_array(text):
    tokens = []
    current = ""
    for char in text:
        if char == "'":
            current += char
        elif char == ".":
            pass
        elif char == ",":
            pass
        elif(is_letter(char)):
            current += char
        else:
            if current:
                tokens.append(current)
                current = ""
            if char not in " \t\n":
                tokens.append(char)
    if current:
        tokens.append(current)
    return tokens

def transform_sentenses_to_list(sentenses) ->list:
    sentense_list = []
    current = ""
    for char in sentenses:
        if char in "\n.?!":
            current += char
            sentense_list.append(current.strip())
            current = ""
        else:
            current += char
    if current.strip():
        sentense_list.append(current.strip())
    return sentense_list

        

def print_word_list(words):
    for i in range(len(words)):
        end_char = ", "
        if (i+1) % 20 == 0:
            end_char = "\n"
        elif i == len(words) - 1:
            end_char = ""
        print(words[i], end=end_char)

def categorize_word_list(wordlist):
    categorized_list = []
    if(len(wordlist) == 0):
        print("The list is empty")
    else:
        for word in wordlist:
            weight = 1
            category = 1
            length = len(word)
            categorized_list.append([word,weight,category,length])
    #print(categorized_list)
    return categorized_list

def clear_duplicates(words):
    altered_words=[]
    for word in words:
        if word not in altered_words:
            altered_words.append(word)
    return altered_words

if __name__ == "__main__":
    #TheFile = "./testing/text_db"
    #testFile="test_db"

    #words = get_saved_from_database(TheFile)
    """
    list_of_words = transform_text_to_array(words)
    print_word_list(list_of_words)
    print("\n")
    list_of_words=clear_duplicates(list_of_words)
    print_word_list(list_of_words)
    print("\n")
    list_of_words=categorize_word_list(list_of_words)
    print("\n")
    #save_to_database(list_of_words, testFile)
    save_categorized(list_of_words, "test2_db")
    """
    list_of_words=read_categorized("test2_db")
    #read_categorized("test2_db")
    print_word_list(list_of_words)
    print()
    for word in list_of_words:
        size = len(word)
        print(word[0:size])
    save_categorized(list_of_words, "test2_db")

# REMOVED CODES
"""
    print()
    print(len(address))
    print(address)
    print()
    

    #print(f"end: {i}")
                end = i
                if start == 0:
                    build_list.append([data[start:prevending], int(data[nextstart:i])])
                    start = i+1
                else:
                    build_list.append([data[start:prevending], int(data[nextstart:i])])
                    start = i+1
        #print(build_list)
    #return build_list
"""        