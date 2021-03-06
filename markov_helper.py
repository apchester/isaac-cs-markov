import random

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
    
def simple_model(corpus):
    print("Using pre-built simple model")
    model = {} #An empty hash to store the values as they are added
    
    words = corpus.split() #Split the corpus up into individual words
    
    for i in range(len(words)-2): 
        phrase = "{} {}".format(words[i], words[i+1])
        next_word = words[i+2]
        
        if phrase not in model:
            model[phrase] = []
        
        model[phrase].append(next_word)
        
    return model    
    
def tuneable_model(corpus, states=2):
    print("Using pre-built tunable model")
    model = {} #An empty hash to store the values as they are added
    
    words = corpus.split() #Split the corpus up into individual words
    
    for i in range(len(words)-states-1): 
        phrase = " ".join(words[i:i+states])
        next_word = words[i+states]
        
        if phrase not in model:
            model[phrase] = []
        
        model[phrase].append(next_word)
        
    return model
    
#This function reads the str parameter and decides if it is a valid starting point (i.e starts with a capital letter)
def is_valid_start(str):
    return str[0].isupper() or str[0] == "@"
    
#This function reads a string parameter and decides if it is a valid end point
def is_valid_end(str):
    return str[-1] == "." or str[-1] == "!" or str[-1] == "?"

#This function should produce the number of words in the string provided
def words_in_string(str):
    return len(str.split())
    
def generate_text(model, sentences_to_generate=5, input_words=2, minimum_sentence_length=3):
    
    text = [] #An array of sentences
    words_added = 0
    for i in range(sentences_to_generate):
        sentence = ""
        #Choose a sentence starting location from the keys of the hash. Remember the rules!
        starting_point = random.choice(list(model.keys()))
        
        while is_valid_start(starting_point) == False:
            starting_point = random.choice(list(model.keys()))
        
        sentence += starting_point
        
        #Loop infinitely until we have reached the valid end of a sentence 
        while True: 
            key = " ".join(sentence.split()[-input_words:])
            
            next_generated_word = random.choice(model[key])
            
            sentence += (" " + next_generated_word)
            
            if words_in_string(sentence) >= minimum_sentence_length and is_valid_end(sentence):
                text.append(sentence)
                break
        
        
    return '\n'.join(text)