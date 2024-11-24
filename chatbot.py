import nltk
from nltk.chat.util import Chat, reflections

# Predefined pairs of patterns and responses
pairs = [
    (r"hi|hello|hey", ["Hello!", "Hi there!", "Hey!"]),
    (r"how are you ?", ["I'm a bot, so I don't have feelings, but thanks for asking!", "I'm doing great!"]),
    (r"what is your name ?", ["I'm a chatbot created using NLTK!", "You can call me ChatBot!"]),
    (r"what can you do ?", ["I can chat with you, answer simple questions, and keep you company!"]),
    (r"quit", ["Goodbye!", "See you soon!", "Bye! Have a great day!"]),
]

# Reflection dictionary for basic pronoun-based replies
# Reflections are already predefined in nltk.chat.util.reflections

# Initialize the chatbot
chatbot = Chat(pairs, reflections)

def start_chat():
    print("Hi! I'm a chatbot. Type 'quit' to exit.")
    chatbot.converse()

# Run the chatbot
if __name__ == "__main__":
    start_chat()
