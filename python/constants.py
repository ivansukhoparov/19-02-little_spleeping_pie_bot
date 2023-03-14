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

