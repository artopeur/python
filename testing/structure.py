def start()->None:
    print("The beginning of the game.")


def write_question(num)->None:
    questions = ["Who are you", "Where did you come from", "Who are you again?", "More questions, have you?", "No one knows, right?"]

    print(questions[num])

def wait_for_response()->str:
    response = input("-> ")
    return response

def print_options(selection)->None:
    
   print(res)

if __name__ == "__main__":
    print("loading...")

    start()
    res = []
    while(1):
        #test = 0
        for i in range(5):
            print("answer with numbers between 1-4")
            write_question(i)
            res.append(wait_for_response())
        break
    print_options(res)
            