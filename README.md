# Whatsapp Arabic Voice Notes Transcriber
This project is an educational project and not a running production application, due to whatsapp limitations the only way to interact with the service without paying is through **Twilio**, in addition i have used **flask**, **ngrok**, and **Kateb API by RDI**  


# Purpose
have you ever had someone send you a long voice note that you didn't feel like listening to but still wanted to know what it contained? do you love music and wish to never stop listening to it to engage in online conversation? well, I have just the solution for you!     
with this whatsapp bot you can forward any voice note to it and it would transcribe it to you in near realtime!

![This is an video](https://i.imgur.com/wDysyKE.gif)

# Libraries and APIS
***Twilio** for interacting with whatsapp and reciveing and relaying your messages  
***Flask** to create the web application that will interact with Twilio  
***ngrok** to secure a connection between your web application and the Twilio servers  
***Kateb API** to transcribe the voice notes with Arabic Egyptian dialect, you can also use the google speech recognition API, both are paid and offer free minutes and the google api is more accurate and precise but the kateb API takes much less time to get running and doesn't require a payment method to get access to the api unlike google's

# Setup
### Python Dependencies    
to start off you install needed libraries by using **pip** in your terminal
```
pip3 install Twilio Flask
```
### ngrok     
install ngrok manually by going to  
>https://ngrok.com/download      

and by running it later in your terminal with
```
ngrok http 4000
```
### Twillio   
now the process of setting up Twilio is a little hazy but to sum it up   
1- Sign up for a Twillio account from and make sure you store your Account and Authentication tokens in your **.env** file    
>https://www.twilio.com/try-twilio    

2- Follow instructions to setup Whatsapp sandbox from
>https://www.twilio.com/console/sms/whatsapp/sandbox 


3-Once the whatsapp channel is created you can interact with the bot through messaging the number **+1 415 523 8886** with the code displayed in your sandbox  
![This is an image](https://i.imgur.com/CKXP7ZM.png)

4-In the same sandbox page make sure that the incoming message webhook is the same as your forwarding address from **ngrok**  
![This is an image](https://i.imgur.com/ZapIsd8.png)
![This is an image](https://i.imgur.com/EB0AZlC.png)  
**also it is very important to make sure that if you decide to name your flask endpoint something other than the default '/' or as i am doing in my code '/bot' is to also type it at the end of your forwarding address**   

### Kateb API
Head over to  
>https://api.kateb.ai/home  

and signup and request an api key and it will be sent to your E-mail, the next step you'll have to do only once to get your api token and you can do it in your python terminal, store the result token in your **.env** file      
![This is an image](https://i.imgur.com/S4Qfq2G.png)


# having fun with it
run **main.py** and the earlier **ngrok** terminal command and start messaging the Twillo number you texted earlier  
if you have acess to a cloud service you can host the **main.py** file there and have it run endelessly, but you'll have to account for the **Twillo** and **Kateb** free limits.
