users ={
    'user__id_test_1': {'user_name':'name 1',
                 'sleep_number': "3",
                 'time_zone':'+1',
                 'durations': [210,60,240,60,270],
                 },

}

def string_to_list(srting: str, delimiter):
    srting = srting.replace('[', '')
    srting = srting.replace(']', '')
    string = srting.split(delimiter)
    for i in string:
        i = int(i)
    return string

def load_data():
    with open('users_data.txt', 'r') as file:
        data = file.read().split('\n')
        for line in data:
            if (line != ''):
                line = line.split('\t')
                users[line[0]] = {'user_name':line[1],
                            'sleep_number': line[2],
                            'time_zone':line[3],
                            'durations':string_to_list(line[4],',')
                            }
       


def wrtite_data():
    with open('users_data.txt', 'w') as file:
        for user_id in users.keys():
            user = users[user_id]
            data = ''
            for param in user.keys():
                data = data + '\t' + str(user[param])
            file.write(user_id + data + '\n')



# wrtite_data()

load_data()
print(users)