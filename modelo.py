import tweepy
from googlesearch import search
from urllib.parse import urlparse
import pandas as pd

APP_KEY3 = 'otL2NcmWPGgCPuxJ2TLtp5bwy'
APP_SECRET3 = 'VjKgOfREevo9pz4tCJqMOnISJBMZegjvwZmwBQxApv8bykY5QT'
OAUTH_TOKEN3 = '119386763-XmvKPX5t59nHsRcZloLzb30RgUPF33kt9wkrSC1V'
OAUTH_TOKEN_SECRET3 ='AVEVXoJlP5IlkA97kPO7x3Q3zQZzSZv0M0CvCYpBrl5Cb'

auth = tweepy.OAuthHandler(APP_KEY3, APP_SECRET3)
auth.set_access_token(OAUTH_TOKEN3, OAUTH_TOKEN_SECRET3)

api3 = tweepy.API(auth,wait_on_rate_limit=True)

def lista_NombrePartido(df):
    df = df[["NOMBRE1","APELLIDO1","AGRUPACIÓN POLITICA", "GENERO"]]
    listaNombrePartido = []
    for i in range(0,len(df)):
        if str(df.iloc[i,3]) == "M":
            nombrePartido = str(df.iloc[i,0]) + " " + str(df.iloc[i,1]) + " candidato "+ str(df.iloc[i,2]) 
            listaNombrePartido.append(nombrePartido)
        else:
            nombrePartido = str(df.iloc[i,0]) + " " + str(df.iloc[i,1]) + " candidata "+ str(df.iloc[i,2]) 
            listaNombrePartido.append(nombrePartido)
    return listaNombrePartido

def lista_NombrePartido2(df):
    df = df[["NOMBRE1", "NOMBRE2","APELLIDO1", "ID_RENGLON"]]
    listaNombrePartido = []
    for i in range(0,len(df)):
        if str(df.iloc[i,1])!="nan":
            nombrePartido = str(df.iloc[i,0]) + " " + str(df.iloc[i,1]) + " " + str(df.iloc[i,2]) + " numero "+ str(df.iloc[i,3]) 
        else:
            nombrePartido = str(df.iloc[i,0]) + " " + str(df.iloc[i,2]) + " numero "+ str(df.iloc[i,3]) 
        listaNombrePartido.append(nombrePartido)
    return listaNombrePartido

def lista_NombrePartido3(df):
    df = df[["NOMBRE1", "NOMBRE2","APELLIDO1", "ID_RENGLON", "DESC_DPTO"]]
    listaNombrePartido = []
    for i in range(0,len(df)):
        if str(df.iloc[i,1])!="nan":
            nombrePartido = str(df.iloc[i,0]) + " " + str(df.iloc[i,1]) + " " + str(df.iloc[i,2]) + " numero "+ str(df.iloc[i,3]) + " " +str(df.iloc[i,4])
        else:
            nombrePartido = str(df.iloc[i,0]) + " " + str(df.iloc[i,2]) + " numero "+ str(df.iloc[i,3]) + " " +str(df.iloc[i,4])
        listaNombrePartido.append(nombrePartido)
    return listaNombrePartido

def identify_twitter (nombre):

    query= nombre + " twitter"
    #print(query)
    count=0
    username=None
    while username is None:
        response = search(query, tld="co.in", num=1, stop=1, pause=2)
        count+=1
        for result in response:
            parsed_url=urlparse(result)
            if "twitter" in parsed_url.hostname:
                if "status" not in parsed_url.path:
                    username=parsed_url.path
        if count>=5:
            break
    return username

def revisarPartido(username, partido):
    following = []
    followers = []
    try:
        for page in tweepy.Cursor(api3.friends_ids, id= usuario).pages():
            following.extend(page)
            
        for page in tweepy.Cursor(api3.followers_ids, id= usuario).pages():
            followers.extend(page)

    except Exception as e:
        print(e)
        next
    
    for follower in followers: 
        info = api3.get_user(id =follower)._json
        if info["name"] == partido:
            return True

    for follow in following: 
        info = api3.get_user(id =following)._json
        if info["name"] == partido:
            return True

    return False

