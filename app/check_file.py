#code to check if we can access the flask app and make changes to the text file.

#MAC COMMANDS
import os
import subprocess

def write_to_file():
    loc_1 = "static/text_folder"
    entries = os.listdir(loc_1)
    print("entries has length: %d" %len(entries))
    for entry in entries:
        print(entry)
    s = input("which files do you want to use? :> ")
    print(s)
    file1 = open(entry,'w')
    m = True
    while(m):
        print("As %s" %user0.name)
        text_to_send = input("Type text and enter to send :> ")
        file1.write(user0.name + " :>" + text_to_send + "\n")
        print("You :> %s " %text_to_send)
        m = False



#run main
if __name__ == "__main__":
    write_to_file()
