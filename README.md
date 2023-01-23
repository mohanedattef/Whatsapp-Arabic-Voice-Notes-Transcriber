# Whatsapp Arabic Voice Notes Transcriber
This project is an educational project and not a running production application, due to whatsapp limitations the only way to interact with the service without paying is through **Twilio**, in addition i have used **flask**, **ngrok**, and **Kateb API by RDI**  


# Purpose
have you ever had someone send you a long voice note that you were refusing to listen to and thought to yourself that you should be able to know what's inside it without having to actually listen? do you love music and wish to never stop listening to it to engage in online conversation? well i have just the solution for you
with this whatsapp bot you can forward any voice note to it and it would transcribe it to you in near realtime!



# Libraries and APIS
***Twilio** for interacting with whatsapp and reciveing and relaying your messages  
***Flask** to create the web application that will interact with Twilio  
***ngrok** to secure a connection between your web application and the Twilio servers  
***Kateb API** to transcribe the voice notes with Arabic Egyptian dialect, you can also use the google speech recognition API, both are paid and offer free minutes and the google api is more accurate and precise but the kateb API takes much less time to get running and doesn't require a payment method to get access to the api unlike google's

# Setup and Code Snippets 
to start off you install needed libraries by using **pip** in your terminal
```
pip3 install Twilio Flask
```
and install ngrok manually by going to  
>https://ngrok.com/download      

and by running it later in your terminal with
```
ngrok http 4000
```
the only thing that remains is setting up Twilio   
1- Sign up for a Twillio account from 
>https://www.twilio.com/try-twilio    

2- Follow instructions to setup Whatsapp sandbox from
>https://www.twilio.com/console/sms/whatsapp/sandbox 


3-Once the whatsapp channel is created you can interact with the bot through messaging the number **+1 415 523 8886** with the code displayed in your sandbox  
![This is an image](https://i.imgur.com/CKXP7ZM.png)


