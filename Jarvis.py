#bibliotecas
import pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia
import webbrowser
import os
import smtplib
#para deixar o resultado da pesquisa do wikipedia em portugues
wikipedia.set_lang("pt")
#Nome do usuário que será mestre do canoa furada
Name = 'Lagarto'

print("Initializing Jarvis") 
#Configuração da voz do Canoa Furada
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def speak(text):
    engine.say(text)
    engine.runAndWait()
#Função de entrada com os boas vindas
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=6 and hour<12:
        speak("Bom Dia " + Name +", o que faremos hoje?")
    elif hour>=12 and hour<18:
        speak("Boa Tarde " + Name +", o que faremos hoje?" )
    else:
        speak("Boa noite" + Name +", o que faremos hoje?")   
#Programa Principal
def tomarcontrole():#essa função receberá a voz do microfone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Escutando ... ")
        audio = r.listen(source)
    try:
        print("Reconhecendo...")
        query = r.recognize_google(audio , language='pt-BR')
        print(f"O usuario disse {query}\n")
    except Exception as e:
        speak("Não entendi nada, fala de novo")  
        query = None
    return query   
#função para enviar email
def email(to,content):
    server= smtplib.SMTP('smtp-mail.outlook.com',587,timeout=120)
    server.ehlo()
    server.starttls()
    server.login('login do email','senha')
    server.sendmail('login do email',to,content)
    server.close()
#Início com chamada das funções  
speak("Inicializando Canoa Furada , Robo inteligente de Ericson Cordeiro de Lima" )
wishMe()
#na query fica armazenado a linguagem natural a ser processada
query = tomarcontrole()
#Logica para executar tarefas básicas
if 'Wikipédia' in query:
        speak('Procurando na wikipedia ...')
        query = query.replace("Wikipédia"," ")
        results= wikipedia.summary(query, sentences =2)
        speak(results)
        print(results)
elif 'Abrir YouTube' in query.lower():
        webbrowser.open("http://www.youtube.com")
elif 'google' in query.lower():
        speak('Procurando no google ...')
#para quando eu pesquisar algo a palavra google não venha junto
        query = query.replace("google"," ")
        webbrowser.open("https://www.google.co.in/search?q=" +(str(query))+ "&oq="+(str(query))+"&gs_l=serp.12..0i71l8.0.0.0.6391.0.0.0.0.0.0.0.0..0.0....0...1c..64.serp..0.0.0.UiQhpfaBsuU")
elif 'abrir facebook' in query.lower():
        webbrowser.open("http://www.facebook.com")
elif 'League of Legends' in query.lower():
        lol = "C:\\Riot Games\\League of Legends\\LeagueClient.exe"
        os.startfile(os.path.join(lol)) 
elif 'fechar navegador' in query.lower():
        os.system("taskkill /im chrome.exe /f")
#Realiza Pesquisa no Youtube por musicas
elif 'tocar' in query.lower():
        query = query.replace("tocar"," ")
        webbrowser.open("https://www.youtube.com/results?search_query=" + query)
elif 'horas' in query.lower():
        strTime  = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"{Name} agora são {strTime}")
#Para funcionamento do email precisa desabilitar a função no email que bloqueia apps inseguros
elif 'e-mail' in query.lower():
    try:
        speak("O que deseja enviar?")
        content = tomarcontrole()
        to = "ericson.id@gmail.com"
        email(to, content)
        speak("Email Enviado com Sucesso")
    except Exception as e :
        print(e)
-------------------------------------------------------------------------------------------------------------------------
#FUNÇÕES FUTURAS
#loop() função a ser criada para que o Canoa Furada funcione mais de uma vez, sem precisar estar executando toda vez
#Biblioteca pyautogui para realizar tarefas repetitivas com mouse e teclado
#Utilizar a biblioteca pandas ou json para verificar finanças pessoais
#Pandas para realizar a automação de logs para planilhas no excel  
#Função abrir o Word e começar a ditar um trabalho com o microfone.
#criação de um .exe para funcionar como um app
 
