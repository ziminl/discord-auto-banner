import requests
import datetime
import time



WEBHOOK_URL = 'webhook'



def send_webhook_message(message, username):
    data = {'content': message,'username': username}
    response = requests.post(WEBHOOK_URL, json=data)
    if response.status_code == 204:
        print('sent')
    else:
        print(f'error: {response.status_code}')
def main():
    message = 'message'
    username = 'username'
    
    while True:
        current_time = datetime.datetime.now().time()
        if current_time.hour == 0 and current_time.minute == 0:
            send_webhook_message(message, username)
        time.sleep(55)

if __name__ == '__main__':
    main()
