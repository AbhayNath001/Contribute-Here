import random                                                               #pip install random2
import json
import torch                                                                #pip install pytorch
from brain import NeuralNet
from NeuralNetwork import bag_of_words, tokenize
import datetime                                                             #pip install DateTime

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
with open("intents.json",'r') as json_data:
    intents = json.load(json_data)
FILE = "TrainingData.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]

model = NeuralNet(input_size,hidden_size,output_size).to(device)
model.load_state_dict(model_state)
model.eval()

name = "Rudra"

from Listen import Listen
from Speak import Say
from Task import NonInputExecution
from Task import InputExecution
from Task import ApiExecution
from Task import StockExecution

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        Say("Good Morning!")

    elif hour>=12 and hour<18:
        Say("Good Afternoon!")

    else:
        Say("Good Evening!")
wishMe()        

def Main():
    sentence = Listen() #Text()
    sentence = tokenize(sentence)
    X = bag_of_words(sentence,all_words)
    X = X.reshape(1,X.shape[0])
    X = torch.from_numpy(X).to(device)
    output = model(X)
    _ , predicted = torch.max(output,dim = 1)
    tag = tags[predicted.item()]
    probs = torch.softmax(output,dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                reply = random.choice(intent["responses"])
                
#Get from json file ______________________________________________________________ 
               
                if "bye" in reply:
                    exit()
               
                elif "time" in reply:
                    NonInputExecution(reply)
                    
                elif "date" in reply:
                    NonInputExecution(reply)
                    
                elif "day" in reply:
                    NonInputExecution(reply) 
                    
                elif "task" in reply:
                    NonInputExecution(reply)
                    
                elif "universe_news" in reply:
                    ApiExecution(reply,sentence)
                
                else:    
                    Say(reply) 
while True:                
    Main()                
    