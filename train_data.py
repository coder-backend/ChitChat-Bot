
from SimilarSentences import SimilarSentences

check =0
with open('chatBotDataSet.txt','r') as f:
    for line in f:
        if check%2==0:
            line = line.replace("?","")
            line = line.replace(".","")
            line= line.lower()
            with open('questions.txt','a+') as writer:
                writer.write(line)
            check+=1
        else:
            check+=1


model = SimilarSentences('questions.txt',"train")
model.train()