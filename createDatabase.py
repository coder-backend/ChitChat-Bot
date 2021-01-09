import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user='root',
    passwd='9840382936',
    database="chatdata"
)




my_cursor = mydb.cursor()
# my_cursor.execute("CREATE DATABASE chatData")
# my_cursor.commit()

# my_cursor.execute("CREATE TABLE talkative (questionID INTEGER AUTO_INCREMENT PRIMARY KEY, questions TEXT, answers TEXT)")
# mydb.commit()
records =[]
check=0
tupleList=[]
with open('chatBotDataSet.txt','r') as f:
    for line in f:
        if check%2==0:
            line = line.replace("\n","")
            line = line.replace("?","")
            line = line.replace(".","")
            line= line.lower()
            tupleList.append(str(line))
            check+=1
        else:
            line = line.replace("\n","")
            line = line.replace(".","")
            line= line.lower()
            tupleList.append(str(line))
            t = tuple(tupleList)
            records.append(t)
            tupleList.clear()
            check+=1



sqlStuff = "INSERT INTO talkative (questions, answers) VALUES (%s, %s)"

my_cursor.executemany(sqlStuff, records)
mydb.commit()
            

# # a = input("Your Questions: ")
# # finalText = removeWords(a)
# # print(finalText)
# # my_cursor.execute("SELECT answers FROM talkative WHERE mainKey=%s",(finalText,))
# # result = my_cursor.fetchall()
# # print(result)
# check =0
# with open('chatBotDataSet.txt','r') as f:
#     for line in f:
#         if check%2==0:
#             line = line.replace("?","")
#             line = line.replace(".","")
#             line= line.lower()
#             with open('questions.txt','a+') as writer:
#                 writer.write(line)
#             check+=1
#         else:
#             check+=1
