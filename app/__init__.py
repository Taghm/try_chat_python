#init pulls all the other parts of our app together and
#makes it into one package

from flask import Flask

#create the app instance
app = Flask(__name__)

#import views
from app import views

#import admin views
from app import admin_views
