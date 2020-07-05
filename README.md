# try_chat_python
just a simple Terminal chat app written in python

How to use it: (for simpler instructions skip to @CMD Tutorial below):
Using 2 terminals (Term 1 & Term 2)

In Term 1
1. git clone the repository and cd into it
2. type "flask run"
This command runs "run.py" which runs our server: 
this help in opening the 127.0.0.1 server where our app is hosted, it also helps with the python requests module in the code used to retrieve newly written messages in the txt chat file.

In Term 2

cd into the "app" folder and type "python cli_text_send_3.py" and Enter
Step will open the Terminal App and allow you to send (m), view (s) or exit (e) the app.

N.B. Remember to always check the http://127.0.0.1:5000 address with a browser to see if the server is working in order to get the recent text/messages.

____________________________________________________________________________________________
@CMD Tutorial:
commands to run the app in respective order (after cloning the repo):
Using two different terminals (Term 1 & Term 2)

In Term 1
cd try_chat_python
/try_chat_python$ flask run

In Term 2
/try_chat_python$ cd app
/try_chat_python/app$ python cli_text_send_3.py


To stop the server in Term 1:
/try_chat_python$ ^C
