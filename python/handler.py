import asyncio
import tg_client
import re


async def handler(data):
        client = tg_client.TelegramClient

        # check update have text message or not
        if ('message' in data.keys()) and ('text' in data['message'].keys()):
            chat_id = data['message']['chat']['id']
            user_name = data['message']['from']['first_name']
            text =  data['message']['text']

            # check users input 
            # if user input 'start' command
            if (text == '/start'):
                 #check user is new or not
                 print('user print start')
                 # if he is new than add him add suggest set his own parameters
                 pass
                 # if not then remind him his parameters and go to main loop

            elif (text == '/set'):
                 print('user print set')

            elif (text == '/info'):
                 print('user print info')

            elif (text == '/stop'):
                 print('user print stop') 

            elif (text == '/help'):
                 print('user print stop')                    

            elif re.match(r'^([0-1]?[0-9]|2[0-3]):[0-5][0-9]\s[0-5]$', text):
                time = text.split(' ')[0]
                event = text.split(' ')[1]
                print(time)
                print(event)

            else:
                msg = 'please enter correct command: "HH:MM E" where HH:MM time of awaking or sleeping amd E number of event or use /help for more information'
                await client.send_message(chat_id, msg)
                print(msg)
            
        else:
            print(data)



