import nltk
from nltk.stem import WordNetLemmatizer
import numpy as np
import random
import string
QA_pairs = {
    "hi": "Hello! How can I help you?",
    "how are you": "I'm just a bot, but I'm doing great! How can I assist you?",
    "what is your name": "I'm a simple chatbot built using NLTK.",
    "bye": "Goodbye! Have a great day.",
    "help": "You can ask me things like 'what is your name', 'how are you', or say 'bye' to exit.",
}
lemmatizer = WordNetLemmatizer()
def preprocess(sentence):
    sentence = sentence.lower()
    sentence = sentence.translate(str.maketrans('', '', string.punctuation))
    tokens = nltk.word_tokenize(sentence)
    lemmas = [lemmatizer.lemmatize(token) for token in tokens]
    return lemmas
def get_response(user_input):
    processed_input = preprocess(user_input)
    max_overlap = 0
    best_match = None
    for question in QA_PAIRS:
        processed_question = preprocess(question)
        overlap = len(set(processed_input) & set(processed_question))
        if overlap > max_overlap:
            max_overlap = overlap
            best_match = question
    if max_overlap > 0:
        return QA_PAIRS[best_match]
    else:
        return "I'm sorry, I didn't understand that. Try asking something else."
def chat():
    print("Chatbot: Hi! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye", "exit", "quit"]:
            print("Chatbot: Bye! Take care.")
            break
        response = get_response(user_input)
        print(f"Chatbot: {response}")
if __name__ == "__main__":
    chat()
