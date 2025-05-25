def start()->None:
    print("The beginning of the game.")


def write_question(num)->None:
    questions = ["Who are you", "Where did you come from", "Who are you again?", "More questions, have you?", "No one knows, right?"]

    print(questions[num])

def wait_for_response()->str:
    response = input("-> ")
    return response

def print_options(selection)->None:
    
    text = ["Default: No proper input.","one", "two", "three", "four"]

    if int(selection) >= 0:
        print(text[int(selection)])
    elif int(selection) > 5 or int(selection) == 0:
        print(text[0])
        
    else:
        print("no proper input given...")

if __name__ == "__main__":
    print("loading...")

    start()
    while(1):
        test = 0
        for i in range(5):
            print("answer with numbers between 1-4")
            write_question(i)
            res=wait_for_response()
            print_options(res)
            