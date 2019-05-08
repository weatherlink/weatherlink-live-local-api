import time
import socket
import os
import json
from multiprocessing import Process
import requests

current_conditions_url = 'http://10.95.35.7:80/v1/current_conditions'

def make_request_using_socket(url):
        try:
            resp = requests.get(url)
            print("HTTP Response Code:", resp)
            json_data = json.loads(resp.text)        
            if json_data["data"] == None:
               print (json_data["error"])
            else:
               print (json_data)
        except ConnectionRefusedError:
            print("Encountered 'ConnectionRefusedError'. Please Retry")
        except TimeoutError:        
            print("Encountered 'TimeoutError'. Please Retry")
			
             
def main():
    global current_conditions_url
    try:            
        make_request_using_socket(current_conditions_url)
        time.sleep(5)
    except ConnectionRefusedError:
        print("Encountered 'ConnectionRefusedError'. Please Retry")
    except TimeoutError:        
        print("Encountered 'TimeoutError'. Please Retry")		    
          
if __name__ == "__main__":
    main()


