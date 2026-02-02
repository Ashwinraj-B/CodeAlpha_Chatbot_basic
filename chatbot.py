# TASK 1: Basic Chatbot
# Goal: Build a simple rule-based chatbot.
# Scope:
# ● Input from user like: "hello", "how are you", "bye".
# ● Predefined replies like: "Hi!", "I'm fine, thanks!", "Goodbye!".
# Key Concepts Used: if-elif, functions, loops, input/output.

# opening the file and reads the content to answer
f=open("data.txt","r")
c=f.readlines()  
f.close()

# function for replying to user
def reply(a):
       for i in range(len(c)): 
              if c[i].strip().lower()==a.lower(): 
                     print("AI  : ",c[i+1]) 
                     return 1                   
       return 0

# function for chatbot to learn new thing
def bot_learn(a):
       print("AI  : Soory! I don't know the answer\n      If you know the answers can you tell to me")
       d=input("You : ")
       f=open("data.txt","a") 
       f.write('\n'+a+'\n'+d) 
       c.append(a+"\n")      
       c.append(d+"\n")

# function to start the conversation with chatbot
def chatbot():
       while 1:
              a=input("You : ")  
              if "bye" in a: # exiting the chatbot by saying bye
                     print("AI  : Goodbye!")
                     break
              else:
                     s=reply(a)  # calling function to reply
                     if(s==0):
                            bot_learn(a) # calling functions to learn itself   

if __name__=='__main__':
       chatbot()    # calliing function to start the conversation when this program runs directly
