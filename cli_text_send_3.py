#Anon Chatbox v.0.0.1
#cli commands to send text with the requests module.
#import necessary modules
#we may need to collect the filetext at 127.0.0.1:5000/static/
import subprocess, requests, os, time



class User:
    def __init__(self, name):
        self.name = name

user0 = User(input("Sign in as: "))
list_users = []
list_users.append(user0.name)
print("As %s" %user0.name)
#create the file where to write text.
def create_file():
    #create the file if it's not already created
    #allow users to have admin privileges with http://127.0.0.1:5000
    #user's static folder which contains the text file
    loc_1 = "app/static/text_folder"
    entries = os.listdir(loc_1)
    #print("entries has length: %d" %len(entries))
    file1 = open(loc_1 + "/" + "test_file1.txt", "a+")
    m = True
    while(m):
            #class_send = input("Type 'm' to send a message \n:> ")
        #print("As %s" %user0.name)
        file1.write("Anon Chatbox Users: " + str(list_users)[1:-1] + "\n")
        text_to_send = input(":> ")
        file1.write(user0.name + " :>" + text_to_send + "\n")
        print("You :> %s " %text_to_send)
        m = False



def show_file():
    #show_file = subprocess.run(["atom", "file0.txt"], stdout=subprocess.DEVNULL)
    file_to_read = requests.get("http://127.0.0.1:5000/static/text_folder/test_file1.txt")
    file_to_read.status_code == requests.codes.ok
    print("Anon Chatbox v.0.0.1: ", file_to_read.text)

def save_to_github():
    #push to github with subprocess before exiting (finish later)
    #first we have to pull to get recent changes from other users.
    new_elements_pull = subprocess.run(["git", "pull"], stdout=subprocess.DEVNULL)
    # then we can add everything in all directories + current one
    new_elements_add = subprocess.run(["git", "add", "--all"], stdout=subprocess.DEVNULL)
    #commit changes to github: the site serves as a server for our data.
    new_elements_commit = subprocess.run(["git", "commit", "-m", "'new lines in chat app directories'"], stdout=subprocess.DEVNULL)
    #push to the repo
    new_elements_push = subprocess.run(["git", "push", "-u", "origin", "master"], stdout=subprocess.DEVNULL)


def chat_dynamics():
    while True:
        input_chat = input("Type 'm' to send  message; 's'  to see the whole chat. Type 'e' to exit \n:> ")
        if(input_chat == "m"):
            print("type and send [enter]... ")
            create_file()
            print("send it through the server...")
            save_to_github()
            print("message Sent!")
            chat_dynamics()
        elif(input_chat == "s"):
            print("Collecting chat messages ...")
            save_to_github()
            print("Showing all messages:")
            show_file()
            chat_dynamics()
        elif(input_chat == "e"):
            print("saving before exiting...")
            save_to_github()
            print("Saved!")
            time_loc2 = time.localtime()
            time_s2 = time.strftime("%m/%d/%Y, %H:%M:%S", time_loc2)
            print("exiting... Program Terminated at ", time_s2)
            exit()






if __name__ == "__main__":
    #specify time
    time_loc = time.localtime()
    time_s = time.strftime("%m/%d/%Y, %H:%M:%S", time_loc)
    print("time at beginning of program: ", time_s)
    print("Anon Chatbox Users: ", list_users)
    #run  the chat_dynamics method
    chat_dynamics()
