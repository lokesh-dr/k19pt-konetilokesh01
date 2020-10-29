from nltk.chat.util import Chat,reflections
from requried import responsepairs as pairs
def firstChatBot():
    print("hi I am your corona chatbot")
    print("how can i help you!!!")
    chatbot = Chat(pairs,reflections)
    chatbot.converse()

if __name__== '__main__':
    firstChatBot()
