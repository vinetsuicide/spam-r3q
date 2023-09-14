import requests
import time
from colorama import Fore, Style

################################################################################

initial_url = 'link'
register_url = 'link'
tor_check_url = 'https://check.torproject.org/'
#change links


#modify this with your data
username_file = 'data'
password_file = 'data'
email_file_path = 'data
gsm_file_path = 'data'
first_name_file_path = 'data'
surname_file_path = 'data'
#U can add other data...

################################################################################

def print_green(text):
    print(f"{Fore.GREEN}{text}{Style.RESET_ALL}")



def save_successful_req(username, email, password, gsm):
    with open('successful_req.txt', 'a') as success_file:
        success_file.write(f'Username: {username}, Email: {email}, Password: {password}, GSM: {gsm}\n')


################################################################################

with open(username_file, 'r') as user_file, \
        open(password_file, 'r') as pass_file, \
        open(email_file_path, 'r') as email_file, \
        open(gsm_file_path, 'r') as gsm_file, \
        open(first_name_file_path, 'r') as first_name_file, \
        open(surname_file_path, 'r') as surname_file:

    
    usernames = user_file.readlines()
    passwords = pass_file.readlines()
    emails = email_file.readlines()   
    gsms = gsm_file.readlines()
    first_names = first_name_file.readlines()
    surnames = surname_file.readlines()
    #u can also modify this

total_entries = max(len(usernames), len(emails), len(gsms))

################################################################################

tor_check_frequency = 5

#check for tor connection
for i in range(total_entries):
    if i % tor_check_frequency == 0:
        
        try:
            response = requests.get(tor_check_url, timeout=5)
            if 'Congratulations. This browser is configured to use Tor.' not in response.text:
                print('Not connected to Tor')
                break
        except requests.exceptions.RequestException as e:
            print(f'Error checking Tor connection: {e}')
            break

  
    username = usernames[i].strip()
    email = emails[i].strip()
    password = passwords[i % len(passwords)].strip()  
    gsm = gsms[i % len(gsms)].strip()  
    firstname = first_names[i % len(first_names)].strip()  
    lastname = surnames[i % len(surnames)].strip() 

  
    response = requests.get(initial_url, allow_redirects=True)

   
    if response.status_code == 200:
       
       #U need change and modify this payload!
        payload = {
            'username': username,
            'password': password,
            'password_confirmation': password,
            'email': email,
            'gsm': gsm,
            'sex': 'non-binary',
            'firstname': firstname,
            'lastname': lastname,
            'identification_no': '',
            'country': 'US',
            'city': '1337',
            'address': 'address',
            'checkmail': 'true',
            'captcha': '',
            'branch': '1913'
        }


        response = requests.post(register_url, data=payload)

      
        response_data = response.json()
        if 'status' in response_data and response_data['status'] == 1:
            save_successful_req(username, email, password, gsm)
            print_green(f'Successful! r3quest for {username}')
        else:
            print(f'r3quest failed for {username}: {response_data}')

       #try not to harm server ;)
        time.sleep(2)

    else:
        print(f'bad URL. status code: {response.status_code}')


print("work finished sir")
