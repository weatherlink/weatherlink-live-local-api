# Introduction

The WeatherLink Live **(WLL)** implements a HTTP interface for getting
current weather data. The response to a valid HTTP Get request is a JSON
document with the current weather from all the Davis transmitters it is
tracking. The Live's barometer, inside temperature, and inside humidity
are also returned. The interface can support continuous requests as
often as every 10 seconds. Additionally, you can also start a real-time
2.5 sec broadcast for wind speed and rain over UDP port 22222. The
syntaxes of supported HTTP requests are described below. You can test
this interface using a browser or the Windows curl utility.

# Local API Current Conditions

### Format of the Incoming HTTP Requests

     http://<WeatherLink Live’s ip_addr:port>/v1/current_conditions
	
Returns a JSON document with the current conditions record along with
the transmitter ID, logical sensor ID, data structure type, device ID
and current timestamp at which the request was made.

##### HTTP Request

    http://10.189.36.37:80/v1/current_conditions

or in CURL:

    curl -X GET -H "application/json" http://10.189.36.37:80/v1/current_conditions

##### Response string

The data_structure_type field can be used to determine what type of
record a JSON object represents. Possible values include:

> 1 = ISS Current Conditions record
>
> 2 = Leaf/Soil Moisture Current Conditions record
>
> 3 = LSS BAR Current Conditions record
>
> 4 = LSS Temp/Hum Current Conditions record

{

    "data":
    {
        "did":"001D0A700002",
        "ts":1531754005,
        "conditions": [
        {
                "lsid":48308,                                  // logical sensor ID **(no unit)**
                "data_structure_type":1,                       // data structure type **(no unit)**
                "txid":1,                                      // transmitter ID **(no unit)**
                "temp": 62.7,                                  // most recent valid temperature **(°F)**
                "hum":1.1,                                     // most recent valid humidity **(%RH)**
                "dew_point": -0.3,                             // **(°F)**
                "wet_bulb":null,                               // **(°F)**
                "heat_index": 5.5,                             // **(°F)**
                "wind_chill": 6.0,                             // **(°F)**
                "thw_index": 5.5,                              // **(°F)**
                "thsw_index": 5.5,                             // **(°F)**
                "wind_speed_last":2,                           // most recent valid wind speed **(mph)**
                "wind_dir_last":null,                          // most recent valid wind direction **(°degree)**
                "wind_speed_avg_last_1_min":4                  // average wind speed over last 1 min **(mph)**
                "wind_dir_scalar_avg_last_1_min":15            // scalar average wind direction over last 1 min **(°degree)**
                "wind_speed_avg_last_2_min":42606,             // average wind speed over last 2 min **(mph)**
                "wind_dir_scalar_avg_last_2_min": 170.7,       // scalar average wind direction over last 2 min **(°degree)**
                "wind_speed_hi_last_2_min":8,                  // maximum wind speed over last 2 min **(mph)**
                "wind_dir_at_hi_speed_last_2_min":0.0,         // gust wind direction over last 2 min **(°degree)**
                "wind_speed_avg_last_10_min":42606,            // average wind speed over last 10 min **(mph)**
                "wind_dir_scalar_avg_last_10_min": 4822.5,     // scalar average wind direction over last 10 min **(°degree)**
                "wind_speed_hi_last_10_min":8,                 // maximum wind speed over last 10 min **(mph)**
                "wind_dir_at_hi_speed_last_10_min":0.0,        // gust wind direction over last 10 min **(°degree)**
                "rain_size":2,                                 // rain collector type/size **(0: Reserved, 1: 0.01", 2: 0.2 mm, 3:  0.1 mm, 4: 0.001")**
                "rain_rate_last":0,                            // most recent valid rain rate **(counts/hour)**
                "rain_rate_hi":null,                           // highest rain rate over last 1 min **(counts/hour)**
                "rainfall_last_15_min":null,                   // total rain count over last 15 min **(counts)**
                "rain_rate_hi_last_15_min":0,                  // highest rain rate over last 15 min **(counts/hour)**
                "rainfall_last_60_min":null,                   // total rain count for last 60 min **(counts)**
                "rainfall_last_24_hr":null,                    // total rain count for last 24 hours **(counts)**
                "rain_storm":null,                             // total rain count since last 24 hour long break in rain **(counts)**
                "rain_storm_start_at":null,                    // UNIX timestamp of current rain storm start **(seconds)**
                "solar_rad":747,                               // most recent solar radiation **(W/m²)**
                "uv_index":5.5,                                // most recent UV index **(Index)**
                "rx_state":2,                                  // configured radio receiver state **(no unit)**
                "trans_battery_flag":0,                        // transmitter battery status flag **(no unit)**
                "rainfall_daily":63,                           // total rain count since local midnight **(counts)**
                "rainfall_monthly":63,                         // total rain count since first of month at local midnight **(counts)**
                "rainfall_year":63,                            // total rain count since first of user-chosen month at local midnight **(counts)**
                "rain_storm_last":null,                        // total rain count since last 24 hour long break in rain **(counts)**
                "rain_storm_last_start_at":null,               // UNIX timestamp of last rain storm start **(sec)**
                "rain_storm_last_end_at":null                  // UNIX timestamp of last rain storm end **(sec)**
        },
        {
                "lsid":3187671188,
                "data_structure_type":2,
                "txid":3,
                "temp_1":null,                                 // most recent valid soil temp slot 1 **(°F)**
                "temp_2":null,                                 // most recent valid soil temp slot 2 **(°F)**
                "temp_3":null,                                 // most recent valid soil temp slot 3 **(°F)**
                "temp_4":null,                                 // most recent valid soil temp slot 4 **(°F)**
                "moist_soil_1":null,                           // most recent valid soil moisture slot 1 **(|cb|)**
                "moist_soil_2":null,                           // most recent valid soil moisture slot 2 **(|cb|)**
                "moist_soil_3":null,                           // most recent valid soil moisture slot 3 **(|cb|)**
                "moist_soil_4":null,                           // most recent valid soil moisture slot 4 **(|cb|)**
                "wet_leaf_1":null,                             // most recent valid leaf wetness slot 1 **(no unit)**
                "wet_leaf_2":null,                             // most recent valid leaf wetness slot 2 **(no unit)**
                "rx_state":null,                               // configured radio receiver state **(no unit)**
                "trans_battery_flag":null                      // transmitter battery status flag **(no unit)**
        },
        {
                "lsid":48307,
                "data_structure_type":4,
                "temp_in":78.0,                                // most recent valid inside temp **(°F)**
                "hum_in":41.1,                                 // most recent valid inside humidity **(%RH)**
                "dew_point_in":7.8,                            // **(°F)**
                "heat_index_in":8.4                            // **(°F)**
        },
        {
                "lsid":48306,
                "data_structure_type":3,
                "bar_sea_level":30.008,                       // most recent bar sensor reading with elevation adjustment **(inches)**
                "bar_trend": null,                            // current 3 hour bar trend **(inches)**
                "bar_absolute":30.008                         // raw bar sensor reading **(inches)**
        }]
    },
    "error":null
}


# Real Time Data Broadcast through UDP


If there are more than 3 ISS transmitters
registered to the WeatherLink Live, the data will be sent in multiple
UDP packets. Note, data is sent every 2.5 seconds. Broadcast time is
accepted only in SECONDS. Maximum broadcast time is set to **86400**
seconds (24 hours). If the requested broadcast time is more than 24
hours, response code "**400** -- Bad request" is sent.

### Format of Real -- Time Broadcast Request

    Live's ip_addr:port >/v1/real_time

 Tells the WW to begin broadcasting UDP data and continue for 1200
 seconds (20 minutes)

 The default duration is 20 minutes.

 (OR)

    Live's ip_addr:port >/v1/real_time?duration=xxx

 Tells the WW to begin broadcasting UDP data and continue for 'xxx'
 seconds

##### HTTP Request

    curl -X GET -H "application/json" http://10.95.35.21:80/v1/real_time

##### HTTP Response for UDP Broadcast Request

    {
        "data":
        {
                "broadcast_port":22222,
                "duration":70
        },
        "error":null
    }

###### Note:
Duration returned may be longer than the
duration requested, if the broadcast is already enabled. If there is
another request to extend the broadcast time before the previous request
is completed, then

-   If the new broadcast time requested is less than the time interval
    remaining for the previous broadcast, the new request is ignored.

-   If the new broadcast time requested is greater than the time
    interval remaining for the previous broadcast, then the broadcast
    time is reset to the new time and the data broadcast is continued

##### UDP Broadcast Response

The data_structure_type field can be used to determine what type of
record a JSON object represents. Possible values include:

> 1 = ISS Rapid Update record

###### First Broadcast Packet (with 3 ISS Sensors):

{

        "did":"001D0A700002",
        "ts":1532031640,
        "conditions": [
        {
                "lsid":3187671188,                           // logical sensor ID **(no unit)**
                "data_structure_type":1,                     // data structure type **(no unit)**
                "txid":1,                                    // transmitter ID **(no unit)**
                "wind_speed_last":0.08,                      // most recent wind speed **(mph)**
                "wind_dir_last":26.7,                        // most recent wind direction **(°degree)**
                "rain_size":2,                               // rain collector size/type **(0: Reserved, 1: 0.01", 2: 0.2 mm, 3: 0.1 mm, 4: 0.001")**
                "rain_rate_last":0,                          // most recent rain rate **(count/hour)**
                "rain_15_min":0,                             // total rain count over last 15 min **(counts)**
                "rain_60_min":0,                             // total rain count over last 60 min **(counts)**
                "rain_24_hr":0,                              // total rain count over last 24 hours **(counts)**
                "rain_storm":0,                              // total rain count since last 24 hour long break in rain **(counts)**
                "rain_storm_start_at":1553187540,            // UNIX timestamp of current rain storm start **(seconds)**
                "rainfall_daily":63,                         // total rain count since local midnight **(counts)**
                "rainfall_monthly":63,                       // total rain count since first of the month at local midnight **(counts)**
                "rainfall_year":63,                          // total rain count since first of the user chosen month at local midnight **(counts)** 
                "wind_speed_hi_last_10_min":null,            // maximum wind speed over last 10 min **(mph)**
                "wind_dir_at_hi_speed_last_10_min":null      // gust wind direction over last 10 min **(°degree)**
        },
        {
                "lsid":3422552209,
                "data_structure_type":1,
                "txid":2,
                "wind_speed_last":0.07,
                "wind_dir_last":30.0,
                "rain_size":2,
                "rain_rate_last":0,
                "rain_15_min":0,
                "rain_60_min":0,
                "rain_24_hr":0,
                "rain_storm":0,
                "rain_storm_start_at":1553187660,
                "rainfall_daily":10,
                "rainfall_monthly":10,
                "rainfall_year":10,
                "wind_speed_hi_last_10_min":null,
                "wind_dir_at_hi_speed_last_10_min":null
        },
        {
                "lsid":3724542100,
                "data_structure_type":1,
                "txid":3,
                "wind_speed_last":0.00,
                "wind_dir_last":0.0,
                "rain_size":0,
                "rain_rate_last":0,
                "rain_15_min":0,
                "rain_60_min":0,
                "rain_24_hr":0,
                "rain_storm":0,
                "rain_storm_start_at":1553143540,
                "rainfall_daily":0,
                "rainfall_monthly":0,
                "rainfall_year":0,
                "wind_speed_hi_last_10_min":null,
                "wind_dir_at_hi_speed_last_10_min":null
        }]
}

###### Second Broadcast Packet (with next 3 ISS Sensors):

{

        "did":"001D0A700002",
        "ts":1532031640,
        "conditions": [
        {
                "lsid":4261413012,
                "data_structure_type":1,
                "txid":4,
                "wind_speed_last":0.00,
                "wind_dir_last":0.0,
                "rain_size":0,
                "rain_rate_last":0,
                "rain_15_min":0,
                "rain_60_min":0,
                "rain_24_hr":0,
                "rain_storm":0,
                "rain_storm_start_at":1553143540,
                "rainfall_daily":0,
                "rainfall_monthly":0,
                "rainfall_year":0,
                "wind_speed_hi_last_10_min":null,
                "wind_dir_at_hi_speed_last_10_min":null
        },
        {
                "lsid":2902458513,
                "data_structure_type":1,
                "txid":5,
                "wind_speed_last":0.00,
                "wind_dir_last":0.0,
                "rain_size":0,
                "rain_rate_last":0,
                "rain_15_min":0,
                "rain_60_min":0,
                "rain_24_hr":0,
                "rain_storm":0,
                "rain_storm_start_at":1553143540,
                "rainfall_daily":0,
                "rainfall_monthly":0,
                "rainfall_year":0,
                "wind_speed_hi_last_10_min":null,
                "wind_dir_at_hi_speed_last_10_min":null
        },
        {
                "lsid":3187671185,
                "data_structure_type":1,
                "txid":6,
                "wind_speed_last":0.00,
                "wind_dir_last":0.0,
                "rain_size":0,
                "rain_rate_last":0,
                "rain_15_min":0,
                "rain_60_min":0,
                "rain_24_hr":0,
                "rain_storm":0,
                "rain_storm_start_at":1553143540,
                "rainfall_daily":0,
                "rainfall_monthly":0,
                "rainfall_year":0,
                "wind_speed_hi_last_10_min":null,
                "wind_dir_at_hi_speed_last_10_min":null
        }]
}

###### Third Broadcast Packet (with remaining 2 ISS Sensors):

{

        "did":"001D0A700002",
        "ts":1532031640,
        "conditions": [
        {
                "lsid":4261413012,
                "data_structure_type":1,
                "txid":7,
                "wind_speed_last":0.00,
                "wind_dir_last":0.0,
                "rain_size":0,
                "rain_rate_last":0,
                "rain_15_min":0,
                "rain_60_min":0,
                "rain_24_hr":0,
                "rain_storm":0,
                "rain_storm_start_at":1553143540,
                "rainfall_daily":0,
                "rainfall_monthly":0,
                "rainfall_year":0,
                "wind_speed_hi_last_10_min":null,
                "wind_dir_at_hi_speed_last_10_min":null
        },
        {
                "lsid":2902458513,
                "data_structure_type":1,
                "txid":8,
                "wind_speed_last":0.00,
                "wind_dir_last":0.0,
                "rain_size":0,
                "rain_rate_last":0,
                "rain_15_min":0,
                "rain_60_min":0,
                "rain_24_hr":0,
                "rain_storm":0,
                "rain_storm_start_at":1553143540,
                "rainfall_daily":0,
                "rainfall_monthly":0,
                "rainfall_year":0,
                "wind_speed_hi_last_10_min":null,
                "wind_dir_at_hi_speed_last_10_min":null
        }]

}

# Appendix

#### Examples of Possible Error Responses with Improperly Formatted Requests

###### HTTP Request

     curl -X GET -H "application/json "http://10.189.36.37:80/v1/current_condition

###### Response string

{

    "data":null,
    "error":{
                "code":404
                "message":"HTTP Page Not Found"
    }
}

###### HTTP Request

    curl -X GET -H "application/json" http://10.189.36.37:80/+v1/current_condition

###### Response string

{

    "data":null,
    "error":{
                "code":400
                "message":"HTTP Bad Request"
    }
}

###### HTTP Request

     curl -X GET -H "application/json" http://10.189.36.37:80/+v1/current_condition Host: weatherlinklive-700017Accept:*/*Accept-Language: en-usConnection:keep-alive

###### Response string

{

    "data":null,
    "error":{
                "code":414
                "message": "HTTP URI Too Long"
    }
}

###### HTTP Request - (When there are no ISS Transmitter configured, but Real-Time broadcast request is made)

    curl -X GET -H "application/json" http://10.189.36.37:80/v1/real_time
 
(or)

    curl -X GET -H "application/json" http://10.189.36.37:80/v1/real_time?duration=xxx

###### Response string

{

    "data":null,
    "error":{
                "code":409
                "message": "No ISS Transmitters. Real Time broadcast not enabled"
    }
}

#### Current Conditions HTTP Request -- Helper Module

```
import time
import socket
import os
import json
from multiprocessing import Process
import requests

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
    try:            
        make_request_using_socket('http://192.168.1.15:80/v1/current_conditions')
        time.sleep(5)
    except ConnectionRefusedError:
        print("Encountered 'ConnectionRefusedError'. Please Retry")
    except TimeoutError:        
        print("Encountered 'TimeoutError'. Please Retry")		    
          
if __name__ == "__main__":
    main()    
```

#### Real-Time UDP Broadcast Request -- Helper Module

```
from socket import *
import struct
import time
import requests
import json

urllist = []

if __name__ == "__main__":
    #while 1:   
        UDP_IP = '192.168.1.15'
        UDP_PORT = 22222
        comsocket = socket(AF_INET, SOCK_DGRAM)
        comsocket.bind(('',22222))
        comsocket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
        resp = requests.get('http://192.168.1.15:80/v1/real_time?duration=20')
        start_time = time.time()
        while 1:
            print("HTTP Response Code:", resp)
            data, wherefrom = comsocket.recvfrom(2048)
            elapsed_time = time.time()
            json_data = json.loads(data.decode("utf-8"))        
            if json_data["conditions"] == None:
                print (json_data["error"])
            else:
                print (json_data)
        
        comsocket.close()        
```
