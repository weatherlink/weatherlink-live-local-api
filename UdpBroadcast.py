from socket import *
import struct
import time
import requests
import json

URL = 'http://10.95.35.7:80/v1/real_time?duration=20'

def main():
        global URL
        UDP_PORT = 22222
        comsocket = socket(AF_INET, SOCK_DGRAM)
        comsocket.bind(('',22222))
        comsocket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
        resp = requests.get(URL)
        while 1:
            print("HTTP Response Code:", resp)
            data, wherefrom = comsocket.recvfrom(2048)
            json_data = json.loads(data.decode("utf-8"))        
            if json_data["conditions"] == None:
                print (json_data["error"])
            else:
                print (json_data)
        
        comsocket.close()

if __name__ == "__main__":
    main()
