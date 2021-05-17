def fetch_corpus(str):
    input_file = None
    if str == "taylor":
        input_file = "./data/taylor.txt"
    elif str == "trump":
        input_file = "./data/trump.txt"
    elif str == "wikipedia":
        input_file = "./data/wikipedia.txt"
    elif str == "bbc":
        input_file = "./data/bbc.txt"
    else:
        print("Unknown Corpus")
        return ""
        
    with open(input_file, 'r') as file:
        data = file.read().replace('\n', '')
        
    return data
    
