#Anon Chatbox v.0.0.1
#cli commands to send text with the requests module.
#import necessary modules
#we may need to collect the filetext at 127.0.0.1:5000/static/
import subprocess, requests, os, time



class User:
    def __init__(self, name):
        self.name = name

user0 = User(input("Sign in as: "))
print("As %s" %user0.name)
#create the file where to write text.
def create_file():
    #create the file if it's not already created
    #allow users to have admin privileges with http://127.0.0.1:5000
    #user's static folder which contains the text file
    loc_1 = "static/text_folder"
    entries = os.listdir(loc_1)
    #print("entries has length: %d" %len(entries))
    file1 = open(loc_1 + "/" + "test_file1.txt", "a+")
    m = True
    while(m):
            #class_send = input("Type 'm' to send a message \n:> ")
        #print("As %s" %user0.name)
        text_to_send = input(":> ")
        file1.write(user0.name + " :>" + text_to_send + "\n")
        print("You :> %s " %text_to_send)
        m = False



def show_file():
    #show_file = subprocess.run(["atom", "file0.txt"], stdout=subprocess.DEVNULL)
    file_to_read = requests.get("http://127.0.0.1:5000/static/text_folder/test_file1.txt")
    file_to_read.status_code == requests.codes.ok
    print("Chatbox: ", file_to_read.text)
    '''file3 = open(file_to_read, "r")
    print(file3.read())
    #print(show_file)'''

'''def get_input():
    input_chat = input("Type 'm' to send  message; 's'  to see the whole chat. Type 'e' to exit \n:> ")
    return input_chat'''

def chat_dynamics():
    while True:
        input_chat = input("Type 'm' to send  message; 's'  to see the whole chat. Type 'e' to exit \n:> ")
        if(input_chat == "m"):
            print("type and send [enter]... ")
            create_file()
            chat_dynamics()
        elif(input_chat == "s"):
            print("showing whole chat... ")
            show_file()
            chat_dynamics()
        elif(input_chat == "e"):
            time_loc2 = time.localtime()
            time_s2 = time.strftime("%m/%d/%Y, %H:%M:%S", time_loc2)
            print("exiting... Program Close at ", time_s2)
            exit()






if __name__ == "__main__":
    #specify time
    time_loc = time.localtime()
    time_s = time.strftime("%m/%d/%Y, %H:%M:%S", time_loc)
    print("time at beginning of program: ", time_s)
    chat_dynamics()
