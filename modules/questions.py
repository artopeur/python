
def write_question(questions)->None:
    res = []
    if(questions == None):
        print("No inputs were given.")
    else:
        for ques in questions:
            print(ques)
            res.append( wait_for_response() )
        return res
    return None

def wait_for_response()->str:
    response = input("-> ")
    return response

def print_options(selection)->None:
    
   print(selection)

if __name__ == "__main__":
    print("Ran from file current file. Test output")

    response = write_question(None)
    response = write_question(["first","second","third"])

    print(response)