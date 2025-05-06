def getLocation(abc):
    print(abc)

def change_to_list(abc, separator):
    abc = abc.replace(',', '')
    print(abc)
    if(abc.find(".")):
       splitted = abc.split(".")
       #print(splitted)
    val_list=splitted[0].split(separator)
    
    return val_list

def check_if_exists(abc, txt):
    start = abc.find(txt)
    return True


def find_string(input, searchstring):
    result=""
    #input=a
    #searchstring = b
    input.split(".")
    print(input)
    if (check_if_exists(input, searchstring)):
        print("Exists. So, let's chop this and see where it is.")

        character_list = change_to_list(input, " ")
        location = 0
        for x in character_list:
            location = location + 1
            if(x == searchstring):
                result = x
                loc = location
                #print(loc)
    return result, loc, character_list

def check_if_equal_replace_with_b(a,b):
    if a == b:
        print(f"equal. {a=}, {b=}")
    else:
        print(f"not equal. {a=}, {b=}")
        print("making equal")
        a = b

    print("Should now be equal, let's see")
    if(a == b):
        print(f"are now equal.. {a=}, {b=} \n")

if __name__ == "__main__":
    print("This is for testing...")
    a = 1
    b = 22
    #print("This is the main")
    check_if_equal_replace_with_b(a,b)
    input_string = "this is to see this test."
    to_find = "test"
    res = ""
    res,location, char_list = find_string(input_string, to_find)
    print(f"{res=}, {location}")
    print(char_list)
    input_string = "This is a test to see where it is."
    to_find = "test"
    res,location, char_list = find_string(input_string, to_find)
    print(f"{res=}, {location}")
    print(char_list)
    print("\n\n The End of testing...")