import json
from flask import jsonify
from config import UPLOAD_FOLDER
import requests
import re
import datetime
from App import translator
# -------------------------- BUSCA DADOS TEMPERATURA POR LONGITUDE E LATITUDE --------------------------
def search_dados_temperatura_lat_lon(lat,lon,units):
    chavekey='078e25e1759b62d7d25ad0f48217d730'

    url = f'https://api.openweathermap.org/data/2.5/weather?units={units}&lat={lat}&lon={lon}&appid={chavekey}'
    print(url)
    req = requests.get(url)
    try:
        return req.json()
    except:
        return None


# -------------------------- BUSCA DADOS TEMPERATURA POR LATITUDE E LONGITUDE --------------------------
def search_dados_temperatura_lat_log(lat,lon,units):
    chavekey = '078e25e1759b62d7d25ad0f48217d730'

    url = f'https://api.openweathermap.org/data/2.5/weather?units={units}&lat={lat}&lon={lon}&appid={chavekey}'
    print(url)
    req = requests.get(url)
    try:
        return req.json()
    except:
        return None


# -------------------------- BUSCA DADOS TEMPERATURA POR CIDADE,UF --------------------------
def search_dados_temperatura_city(city, units):
    chavekey = '078e25e1759b62d7d25ad0f48217d730'

    url = f'https://api.openweathermap.org/data/2.5/weather?units={units}&q={city}&appid={chavekey}'
    print(url)
    req = requests.get(url)
    try:
        return req.json()
    except:
        return None


# -------------------------- BUSCA DADOS LATITUDE E LONGITUDE GEOLOCATOR --------------------------
def search_latitude_longitude_geolocator(strcyte):
    from geopy import Nominatim
    geolocator = Nominatim(user_agent="sisnutri")
    try:
        result = geolocator.geocode(strcyte)
        return result
    except:
        return None


# -------------------------- TRADUZ DETERMINADO TEXTO EM INGLES OU VICE-VERSA EM PORTUGUES = RETURN JSON --------------------------
def translate(txttranslate,src='',dest=''):
    if src == '' and dest == '':
        detect = translator.detect(txttranslate)

        if detect.lang=='en':
            dest = 'pt'
            src = 'en'
        else:
            dest = 'en'
            src = 'pt'


    translation = translator.translate(txttranslate,src=src,dest=dest)
    traducao = translation.text
    origin = translation.origin
    strjson = {
        'src':translation.src,
        'dest': translation.dest,
        'origin':origin,
        'traducao':traducao
        }
    return strjson


# -------------------------- BUSCA DADOS LOCALIDADE DE ACORDO COM O CEP INFORMADO = RETURN JSON --------------------------
def busca_dados_CEP(cep):
    ceporg = re.sub('[^a-zA-Z0-9 \n\.]', '', cep)
    req = requests.get('https://viacep.com.br/ws/'+ceporg+'/json/')
    if req.status_code==200:
        data = req.json()
    else:
        data = {'erro':True}
    return data


# ENviar SMS TWILIO -Continuação
def sendsms_twilio(msgsms,phone):
    from config import TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN
    from twilio.rest import Client

    account_sid = TWILIO_ACCOUNT_SID
    auth_token = TWILIO_AUTH_TOKEN
    client = Client(account_sid, auth_token)
    mensagem = client.messages.create(to=phone,
                                      from_='+5532984422783',
                                      body=msgsms)
    result = mensagem.sid()
    return  result
