import torch
import torch.nn as nn
from torch.autograd import Variable
from torch import optim
import torch.nn.functional as F
import pickle
import re
import numpy as np

def normalizeString(s):
	s = s.lower().strip()
	s = re.sub(r"<br />",r" ",s)
	s = re.sub(r'(\W)(?=\1)', '', s)
	s = re.sub(r"([.!?])", r" \1", s)
	s = re.sub(r"[^a-zA-Z.!?]+", r" ", s)
	
	return s

class Model(torch.nn.Module) :
	def __init__(self,embedding_dim,hidden_dim) :
		super(Model,self).__init__()
		self.hidden_dim = hidden_dim
		self.embeddings = nn.Embedding(vocabLimit+1, embedding_dim)
		self.lstm = nn.LSTM(embedding_dim,hidden_dim)
		self.linearOut = nn.Linear(hidden_dim,2)
	def forward(self,inputs,hidden) :
		x = self.embeddings(inputs).view(len(inputs),1,-1)
		lstm_out,lstm_h = self.lstm(x,hidden)
		x = lstm_out[-1]
		x = self.linearOut(x)
		x = F.log_softmax(x)
		return x,lstm_h
	def init_hidden(self) :
		return (Variable(torch.zeros(1, 1, self.hidden_dim)).cuda(),Variable(torch.zeros(1, 1, self.hidden_dim)).cuda())	




vocabLimit = 50000
max_sequence_len = 500
model = Model(50,100)
model=model.cuda();


with open('dict.pkl','rb') as f :
	word_dict = pickle.load(f)



model.load_state_dict(torch.load('model3.pth'))



def  analyse(data):
    data=data.strip()
    input_data=[]
    for word in data.split(' ') :
        if not word in word_dict :
            input_data.append(vocabLimit)
        else :
            input_data.append(word_dict[word])	
        if len(input_data) > max_sequence_len :
            input_data = input_data[0:max_sequence_len]
    input_data = Variable(torch.LongTensor(input_data))
    input_data=input_data.cuda()
    hidden = model.init_hidden()
    y_pred,_ = model(input_data,hidden)
    y_pred=y_pred.cpu()
    pred = y_pred.data.max(1)[1].numpy()
    return str(pred[0])

