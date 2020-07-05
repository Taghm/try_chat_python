#cli commands to send text with the requests module.
#import necessary modules
#we may need to collect the filetext at 127.0.0.1:5000/static/
import subprocess, requests, os, time



class User:
    def __init__(self, name):
        self.name = name

user0 = User(input("Sign in as: "))
#create the file where to write text.
def create_file():
    #create the file if it's not already created
    #allow users to have admin privileges with http://127.0.0.1:5000
    #user's static folder which contains the text file
    loc_1 = "static/text_folder"
    entries = os.listdir(loc_1)
    print("entries has length: %d" %len(entries))
    if(len(entries) > 0):
        for entry in entries:
            print(entry)
        s = input("which file do you want to use? If it's only one file present, choose it :> ")
        print("file chosen :> %s" %s)
        file1 = open(loc_1 +"/"+ s,'a+')
        m = True
        while(m):
            print("As %s" %user0.name)
            text_to_send = input("Type text and enter to send :> ")
            file1.write(user0.name + " :>" + text_to_send + "\n")
            print("You :> %s " %text_to_send)
            m = False


    else:
        file1 = open(loc_1 + "/" + "test_file1.txt", "a+")
        m = True
        while(m):
            print("As %s" %user0.name)
            text_to_send = input("Type text and enter to send :> ")
            file1.write(user0.name + " :>" + text_to_send + "\n")
            print("You :> %s " %text_to_send)
        m = False



def show_file():
    #show_file = subprocess.run(["atom", "file0.txt"], stdout=subprocess.DEVNULL)
    file_to_read = requests.get("http://127.0.0.1:5000/static/text_folder/test_file1.txt")
    file_to_read.status_code == requests.codes.ok
    print(file_to_read.text)
    '''file3 = open(file_to_read, "r")
    print(file3.read())
    #print(show_file)'''

def chat_dynamics():
    value_true = True
    sys_ask = input("Type 'y' to start typing a message; 'see' (or) 's' to check the  chat for messages,\n and'n' to stop the program. \n:>")
    if(sys_ask == "y"):
        while(value_true):
            #send text
            create_file()
            #see reply from user2
            #i.e. refresh
            see_text = input("Check whole chat -type 'y' (or) send new message -type 'n' \nTo EXIT -type 'e'. \n:>")
            if (see_text == "y"):
                show_file()
                type2nd = input("respond, 'y' or 'n' :> ")
                if(type2nd == "y"):
                    create_file()
                else:
                    chat_dynamics()
            elif (see_text == "n"):
                create_file()
            elif(see_text == "e"):
                #del_file = subprocess.run(["rm", "file0.txt"], stdout=subprocess.DEVNULL)
                print("Closing Chat ...")
                print("Process Ended.")
                exit()
    elif(sys_ask == "see" or sys_ask == "s"):
        show_file()
        type2nd = input("respond, 'y' or 'n' :> ")
        if(type2nd == "y"):
            create_file()
        else:
            chat_dynamics()
    elif(sys_ask == "n"):
         exit_ask = input("Do you want to exit the program? 'y' or 'n'. \n:>")
         if(exit_ask == "y"):
             #del_file = subprocess.run(["rm", "file0.txt"], stdout=subprocess.DEVNULL)
             print("Closing Chat... Process Ended.")
             exit()
         else:
             res_proc = input("Send a text? 'y' or 'n' :> ")
             if(res_proc == "y"):
                 chat_dynamics()
             else:
                 #del_file = subprocess.run(["rm", "file0.txt"], stdout=subprocess.DEVNULL)
                 print("Program Exited.")
                 exit()




if __name__ == "__main__":
    #specify time
    time_loc = time.localtime()
    time_s = time.strftime("%m/%d/%Y, %H:%M:%S", time_loc)
    print("time at beginning of program: ", time_s)
    chat_dynamics()
