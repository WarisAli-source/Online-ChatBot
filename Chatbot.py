from nltk.chat.util import Chat,reflections
from flask import Flask,render_template,request
import pickle

app = Flask(__name__)

f = open("pairs.txt",'rb')
#rb - read bytes
#wb - write bytes

pairs = pickle.load(f)

chat = Chat(pairs, reflections)
# #
# def chatty():
#     # print("Hi, I'm JARVIS and i want to help and chat with you!")
#     chat = Chat(pairs, reflections)
#     # reflections is a dictionary containing a some convs.
#     print(chat.respond('Hello'))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    usertext = request.args.get('msg')
    return str(chat.respond(usertext))

if __name__ == '__main__':
    app.run()


########################################################################################################################
#Writing the data into a file.
# import pickle
#
# pairs = [
#     [
#         r"my name is (.*)",
#         ["Hello %1, How are you today ?", ]
#     ],
#
#     [
#         r"(.*)help(.*) ",
#         ["I can help you ", ]
#     ],
#     [
#         r"(.*) your name ?",
#         ["My name is J.A.R.V.I.S like in Iron Man, but you can just call me Jarvis and I'm a chatbot ?", ]
#     ],
#     [
#         r"how are you ?",
#         ["I'm doing very well\nHow about You ?", ]
#     ],
#     [
#         r"sorry (.*)",
#         ["Its alright", "Its OK, never mind that", ]
#     ],
#     [
#         r"i'm (.*) doing good",
#         ["Nice to hear that", "Alright, great !", ]
#     ],
#     [
#         r"(hi|hey|hello|hola|holla)(.*)",
#         ["Hello", "Hey there", ]
#     ],
#     [
#         r"what (.*) want ?",
#         ["Make me an offer I can't refuse", ]
#
#     ],
#     [
#         r"(.*) created ?",
#         ["Varma created me using Python's NLTK library ", "top secret ;)", ]
#     ],
#     [
#         r"(.*) (location|city) ?",
#         ['Tokyo, Japan', ]
#     ],
#     [
#         r"how is the weather in (.*)?",
#         ["Weather in %1 is amazing like always", "It's hot here in %1", "It's chilli here in %1",
#          "In %1 there is a 50% chance of rain", ]
#     ],
#     [
#         r"i work (in|at) (.*)?",
#         ["%1 is an amazing company, I have heard about it.", ]
#     ],
#     [
#         r"(.*)raining in (.*)",
#         ["No rain in the past 4 days here in %2", "In %2 there is a 50% chance of rain", ]
#     ],
#     [
#         r"is it (.*) in (.*)",
#         ["No its not %1 in %2", "It could be", "Yes its %1 in %2"]
#     ],
#     [
#         r"how (.*) health (.*)",
#         ["Health is very important, but I am a computer, so I don't need to worry about my health ", ]
#     ],
#     [
#         r"(.*)(sports|game|sport)(.*)",
#         ["I'm a very big fan of Basketball", ]
#     ],
#     [
#         r"who (.*) sportsperson ?",
#         ["Messy", "LeBron", "D-Wade"]
#     ],
#     [
#         r"who (.*) (moviestar|actor|actress)?",
#         ["Tony stark"]
#     ],
#     [
#         r"quit",
#         ["Bye for now. See you soon :) ", "It was nice talking to you. See you soon :)"]
#     ],
# ]
# f = open('pairs.txt','ab')
#
# pickle.dump(pairs,f)
#
# f.close()
