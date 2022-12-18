'''little sleepig pie v.0.2'''

import telebot
import time
import datetime
import re

bot = telebot.TeleBot(token)

#hour_format = '/^([0-9]|0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$/'
clarified_times =[]
events =['First waking', 'First day sllep', 'Second waking', 'Second day sleep', 'Third waking']
durations = [210,60,240,60,270]
time_zone = '+4'
process_messages = {
    'greeting':'Good morning! What time did you get up?',
    'event_sleep':'sleeping',
    'event_awake':'awaking',
    'clarify':'Clarify time...',
    'error_format':'time incorrect, enter again in format hh:mm',
    'alarm_sleep_first':'30 min to sleeping',
    'alarm_sleep_second':'Time to go bed!',
    'alarm_awake_first':'5 minutes to awake',
    'alarm_awake_second':'Time to wake up!'
}

#convert duration in minutes to format HH:MM 
#return string HH:MM
def min_to_hours(time_in_min):
  mins = int(time_in_min) % 60
  hours = (int(time_in_min) - mins) / 60
  if mins<10:
    mins = '0' + str(mins)
  str_time = str(int(hours)) + ':' + str(mins)
  return str_time

#convert time in format HH:MM to minutes
#return integer
def hours_to_mins(time_in_hours):
  split_time = time_in_hours.split(':')
  str_time = int(split_time[0])*60 + int(split_time[1])
  return str_time

#calculate time for next event
def calculate_time(current_time, duration):
  return min_to_hours(hours_to_mins(current_time) + duration)

#create message for next event
def set_next_event(clarified_time, duration, event):
  next_event_time = calculate_time(clarified_time, duration)
  text_message = 'Next ' + event + ' at ' + next_event_time
  return text_message

#calculate timeout
def set_timeout(time, duration, before):
  current_time = hours_to_mins(datetime.datetime.now().time().strftime('%H:%M'))+(int(time_zone)*60)
  if current_time<0:
    current_time=1440-current_time
  clarified_time = hours_to_mins(time)
  timeout = (duration - int(current_time) + int(clarified_time) - before)*60
  return timeout

def set_good_night():
  current_time = hours_to_mins(datetime.datetime.now().time().strftime('%H:%M'))
  time_to_midnight = 1440 - current_time
  timeout = (time_to_midnight + 360)*60
  return timeout 

def day_report():
  message = f'''
  Daily Report: \n Awaking at {clarified_times[0]} \n First day sleepig from {clarified_times[1]} to {clarified_times[2]}  \n Second day sleepig from {clarified_times[3]} to {clarified_times[4]} \n Go night at {clarified_times[5]}
  '''

def show_settings():
  msg_durations = ''
  for i in range(len(events)):
   msg_durations = msg_durations + events[i] + ': ' + min_to_hours(durations[i]) + '\n'
  message = f'''
Settings:

Number of day sleeps: 2
Time zone: UTC{time_zone}

Durations:

{msg_durations}
'''
  return message


@bot.message_handler(commands=['start', 'help'])
def send_message(message):
  bot.send_message(message.chat.id, show_settings())
	bot.send_message(message.chat.id, '''
  To start use command '/go'
  Enter time if format HH:MM
  ''')
	

@bot.message_handler(commands=['go'])
def send_welcome(message):
	msg = bot.send_message(message.chat.id, process_messages['greeting'])
	bot.register_next_step_handler(msg, process_0)
 
def process_0(message): #FIRST AWAKING
  if re.match(r'^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$', message.text):
    clarified_times.append(message)
    txt = set_next_event(message.text,durations[0],process_messages['event_sleep'])
    bot.send_message(message.chat.id, txt)
    timeout = set_timeout(message.text,durations[0],30)
    time.sleep(timeout)
    bot.send_message(message.chat.id, process_messages['alarm_sleep_first'])
    time.sleep(30*60)
    msg = bot.send_message(message.chat.id, process_messages['alarm_sleep_second'])
    msg = bot.send_message(message.chat.id, process_messages['clarify'])
    bot.register_next_step_handler(msg, process_1)
  else:
    msg = bot.send_message(message.chat.id, process_messages['error_format'])
    bot.register_next_step_handler(msg, process_0)

def process_1(message): #FIRST DAY SLEEP
  if re.match(r'^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$', message.text):
    clarified_times.append(message)
    txt = set_next_event(message.text,durations[1],process_messages['event_awake'])
    bot.send_message(message.chat.id, txt)
    timeout = set_timeout(message.text,durations[1],5)
    time.sleep(timeout)
    bot.send_message(message.chat.id, process_messages['alarm_awake_first'])
    time.sleep(5*60)
    msg = bot.send_message(message.chat.id, process_messages['alarm_awake_second'])
    msg = bot.send_message(message.chat.id, process_messages['clarify'])

    bot.register_next_step_handler(msg, process_2)

  else:
    msg = bot.send_message(message.chat.id, process_messages['error_format'])

    bot.register_next_step_handler(msg, process_1)

def process_2(message): #SECOND AWAKING
  if re.match(r'^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$', message.text):
    clarified_times.append(message)
    txt = set_next_event(message.text,durations[2],process_messages['event_sleep'])
    bot.send_message(message.chat.id, txt)
    timeout = set_timeout(message.text,durations[2],30)
    time.sleep(timeout)
    bot.send_message(message.chat.id, process_messages['alarm_sleep_first'])
    time.sleep(30*60)
    msg = bot.send_message(message.chat.id, process_messages['alarm_sleep_second'])
    msg = bot.send_message(message.chat.id, process_messages['clarify'])
    bot.register_next_step_handler(msg, process_3)
  else:
    msg = bot.send_message(message.chat.id, process_messages['error_format'])
    bot.register_next_step_handler(msg, process_2)

def process_3(message): #SECOND DAY SLEEP
  if re.match(r'^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$', message.text):
    clarified_times.append(message)
    txt = set_next_event(message.text,durations[3],process_messages['event_awake'])
    bot.send_message(message.chat.id, txt)
    timeout = set_timeout(message.text,durations[3],5)
    time.sleep(timeout)
    bot.send_message(message.chat.id, process_messages['alarm_awake_first'])
    time.sleep(5*60)
    msg = bot.send_message(message.chat.id, process_messages['alarm_awake_second'])
    msg = bot.send_message(message.chat.id, process_messages['clarify'])

    bot.register_next_step_handler(msg, process_4)

  else:
    msg = bot.send_message(message.chat.id, process_messages['error_format'])

    bot.register_next_step_handler(msg, process_3)

def process_4(message): #THIRD AWAKING
  if re.match(r'^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$', message.text):
    clarified_times.append(message)
    txt = set_next_event(message.text,durations[4],process_messages['event_sleep'])
    bot.send_message(message.chat.id, txt)
    timeout = set_timeout(message.text,durations[4],30)
    time.sleep(timeout)
    bot.send_message(message.chat.id, process_messages['alarm_sleep_first'])
    time.sleep(30*60)
    bot.send_message(message.chat.id, process_messages['alarm_sleep_second'])
    bot.send_message(message.chat.id, 'Good Nighth!')

    bot.register_next_step_handler(message.chat.id, send_welcome)

  else:
    msg = bot.send_message(message.chat.id, process_messages['error_format'])
    bot.register_next_step_handler(msg, process_4)


bot.infinity_polling()