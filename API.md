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

Returns a JSON document with the current conditions record along with
the transmitter ID, logical sensor ID, data structure type, device ID
and current timestamp at which the request was made.

#### Sample HTTP Request

[**http://10.189.36.37:80/v1/current\_conditions**](http://10.189.36.37:80/v1/current_conditions)

or in CURL:

**curl -X GET -H \"application/json\"
<http://10.189.36.37:80/v1/current_conditions>**

#### Response string

The data\_structure\_type field can be used to determine what type of
record a JSON object represents. Possible values include:

> 1 = ISS Current Conditions record
>
> 2 = Leaf/Soil Moisture Current Conditions record
>
> 3 = LSS BAR Current Conditions record
>
> 4 = LSS Temp/Hum Current Conditions record

{

    \"data\":
    {
        \"did\":\"001D0A700002\",
        \"ts\":1531754005,
        \"conditions\": \[
        {
                \"lsid":48308, // logical sensor ID **(no unit)**
                \"data\_structure\_type\":1, // data structure type **(no unit)**
                \"txid\":1, // transmitter ID **(no unit)**
                \"temp\": 62.7, // most recent valid temperature **(°F)**
                \"hum\":1.1, // most recent valid humidity **(%RH)**
                \"dew\_point\": -0.3, // **(°F)**
                \"wet\_bulb\":null, // **(°F)**
                \"heat\_index\": 5.5, // **(°F)**
                \"wind\_chill\": 6.0, // **(°F)**
                \"thw\_index\": 5.5, // **(°F)**
                \"thsw\_index\": 5.5, // **(°F)**
                \"wind\_speed\_last\":2,                           // most recent valid wind speed **(mph)**
                \"wind\_dir\_last\":null,                          // most recent valid wind direction **(°degree)**
                "wind\_speed\_avg\_last\_1\_min\":4                // average wind speed over last 1 min **(mph)**
                "wind\_dir\_scalar\_avg\_last\_1\_min":15          // scalar average wind direction over last 1 min **(°degree)**
                \"wind\_speed\_avg\_last\_2\_min\":42606,          // average wind speed over last 2 min **(mph)**
                \"wind\_dir\_scalar\_avg\_last\_2\_min\": 170.7,   // scalar average wind direction over last 2 min **(°degree)**
                \"wind\_speed\_hi\_last\_2\_min\":8,               // maximum wind speed over last 2 min **(mph)**
                \"wind\_dir\_at\_hi\_speed\_last\_2\_min\":0.0,    // gust wind direction over last 2 min **(°degree)**
                \"wind\_speed\_avg\_last\_10\_min\":42606,         // average wind speed over last 10 min **(mph)**
                \"wind\_dir\_scalar\_avg\_last\_10\_min\": 4822.5, // scalar average wind direction over last 10 min **(°degree)**
                \"wind\_speed\_hi\_last\_10\_min\":8,              // maximum wind speed over last 10 min **(mph)**
                \"wind\_dir\_at\_hi\_speed\_last\_10\_min\":0.0,   // gust wind direction over last 10 min **(°degree)**
                \"rain\_size\":2,                                  // rain collector type/size **(0: Reserved, 1: 0.01", 2: 0.2 mm, 3:  0.1 mm, 4: 0.001")**
                \"rain\_rate\_last\":0,                            // most recent valid rain rate **(counts/hour)**
                \"rain\_rate\_hi\":null,                           // highest rain rate over last 1 min **(counts/hour)**
                \"rainfall\_last\_15\_min\":null,                  // total rain count over last 15 min **(counts)**
                \"rain\_rate\_hi\_last\_15\_min\":0,               // highest rain rate over last 15 min **(counts/hour)**
                \"rainfall\_last\_60\_min\":null,                  // total rain count for last 60 min **(counts)**
                \"rainfall\_last\_24\_hr\":null,                   // total rain count for last 24 hours **(counts)**
                \"rain\_storm\":null,                              // total rain count since last 24 hour long break in rain **(counts)**
                \"rain\_storm\_start\_at\":null,                   // UNIX timestamp of current rain storm start **(seconds)**
                \"solar\_rad\":747,                                // most recent solar radiation **(W/m²)**
                \"uv\_index\":5.5,                                 // most recent UV index **(Index)**
                \"rx\_state\":2,                                   // configured radio receiver state **(no unit)**
                \"trans\_battery\_flag\":0,                        // transmitter battery status flag **(no unit)**
                \"rainfall\_daily\":63,                            // total rain count since local midnight **(counts)**
                \"rainfall\_monthly\":63,                          // total rain count since first of month at local midnight **(counts)**
                \"rainfall\_year\":63,                             // total rain count since first of user-chosen month at local midnight **(counts)**
                \"rain\_storm\_last\":null,                        // total rain count since last 24 hour long break in rain **(counts)**
                \"rain\_storm\_last\_start\_at\":null,             // UNIX timestamp of last rain storm start **(sec)**
                \"rain\_storm\_last\_end\_at\":null                // UNIX timestamp of last rain storm end **(sec)**
        },
        {
                \"lsid":3187671188,
                \"data\_structure\_type\":2,
                \"txid\":3,
                \"temp\_1\":null,                                 // most recent valid soil temp slot 1 **(°F)**
                \"temp\_2\":null,                                 // most recent valid soil temp slot 2 **(°F)**
                \"temp\_3\":null,                                 // most recent valid soil temp slot 3 **(°F)**
                \"temp\_4\":null,                                 // most recent valid soil temp slot 4 **(°F)**
                \"moist\_soil\_1\":null,                          // most recent valid soil moisture slot 1 **(\|cb\|)**
                \"moist\_soil\_2\":null,                          // most recent valid soil moisture slot 2 **(\|cb\|)**
                \"moist\_soil\_3\":null,                          // most recent valid soil moisture slot 3 **(\|cb\|)**
                \"moist\_soil\_4\":null,                          // most recent valid soil moisture slot 4 **(\|cb\|)**
                \"wet\_leaf\_1\":null,                            // most recent valid leaf wetness slot 1 **(no unit)**
                \"wet\_leaf\_2\":null,                            // most recent valid leaf wetness slot 2 **(no unit)**
                \"rx\_state\":null,                               // configured radio receiver state **(no unit)**
                \"trans\_battery\_flag\":null                     // transmitter battery status flag **(no unit)**
        },
        {
                \"lsid":48307,
                \"data\_structure\_type\":4,
                \"temp\_in\":78.0,                                // most recent valid inside temp **(°F)**
                \"hum\_in\":41.1,                                 // most recent valid inside humidity **(%RH)**
                \"dew\_point\_in\":7.8,                           // **(°F)**
                \"heat\_index\_in\":8.4                           // **(°F)**
        },
        {
                \"lsid":48306,
                \"data\_structure\_type\":3,
                \"bar\_sea\_level\":30.008,                      // most recent bar sensor reading with elevation adjustment **(inches)**
                \"bar\_trend\": null,                            // current 3 hour bar trend **(inches)**
                \"bar\_absolute\":30.008                         // raw bar sensor reading **(inches)**
        }\]
    },
    \"error\":null
}


# Real Time Data Broadcast through UDP

##### Note:
If there are more than 3 ISS transmitters
registered to the WeatherLink Live, the data will be sent in multiple
UDP packets. Note, data is sent every 2.5 seconds. Broadcast time is
accepted only in SECONDS. Maximum broadcast time is set to **86400**
seconds (24 hours). If the requested broadcast time is more than 24
hours, response code "**400** -- Bad request" is sent.

### Format of Real -- Time Broadcast Request

> ***Live's ip\_addr:port \>/v1/real\_time***
>
> Tells the WW to begin broadcasting UDP data and continue for 1200
> seconds (20 minutes)
>
> The default duration is 20 minutes.
>
> (OR)
>
> ***Live's ip\_addr:port \>/v1/real\_time?duration=xxx***
>
> Tells the WW to begin broadcasting UDP data and continue for 'xxx'
> seconds

#### Sample HTTP Request

***curl -X GET -H \"application/json" http://10.95.35.21:80/v1/real\_time***

#### Response String

#### Sample HTTP Response for UDP Broadcast Request

    {
        \"data\":
        {
                \"broadcast\_port\":22222,
                \"duration\":70
        },
        \"error\":null
    }

##### Note:
Duration returned may be longer than the
duration requested, if the broadcast is already enabled. If there is
another request to extend the broadcast time before the previous request
is completed, then

-   If the new broadcast time requested is less than the time interval
    remaining for the previous broadcast, the new request is ignored.

-   If the new broadcast time requested is greater than the time
    interval remaining for the previous broadcast, then the broadcast
    time is reset to the new time and the data broadcast is continued

#### Sample UDP Broadcast Response

The data\_structure\_type field can be used to determine what type of
record a JSON object represents. Possible values include:

> 1 = ISS Rapid Update record

###### First Broadcast Packet (with 3 ISS Sensors):

{

        \"did\":\"001D0A700002\",
        \"ts\":1532031640,
        \"conditions\": \[
        {
                \"lsid":3187671188, // logical sensor ID **(no unit)**
                \"data\_structure\_type\":1, // data structure type **(no unit)**
                \"txid\":1, // transmitter ID **(no unit)**
                \"wind\_speed\_last\":0.08, // most recent wind speed **(mph)**
                \"wind\_dir\_last\":26.7, // most recent wind direction **(°degree)**
                \"rain\_size\":2, // rain collector size/type **(0: Reserved, 1: 0.01", 2: 0.2 mm, 3: 0.1 mm, 4: 0.001")**
                \"rain\_rate\_last\":0, // most recent rain rate **(count/hour)**
                \"rain\_15\_min\":0, // total rain count over last 15 min **(counts)**
                \"rain\_60\_min\":0, // total rain count over last 60 min **(counts)**
                \"rain\_24\_hr\":0, // total rain count over last 24 hours **(counts)**
                \"rain\_storm\":0, // total rain count since last 24 hour long break in rain **(counts)**
                \"rain\_storm\_start\_at\":1553187540, // UNIX timestamp of current rain storm start **(seconds)**
                \"rainfall\_daily\":63, // total rain count since local midnight **(counts)**
                \"rainfall\_monthly\":63, // total rain count since first of the month at local midnight **(counts)**
                \"rainfall\_year\":63, // total rain count since first of the user chosen month at local midnight **(counts)** 
                \"wind\_speed\_hi\_last\_10\_min\":null, // maximum wind speed over last 10 min **(mph)**
                \"wind\_dir\_at\_hi\_speed\_last\_10\_min\":null // gust wind direction over last 10 min **(°degree)**
        },
        {
                \"lsid":3422552209,
                \"data\_structure\_type\":1,
                \"txid\":2,
                \"wind\_speed\_last\":0.07,
                \"wind\_dir\_last\":30.0,
                \"rain\_size\":2,
                \"rain\_rate\_last\":0,
                \"rain\_15\_min\":0,
                \"rain\_60\_min\":0,
                \"rain\_24\_hr\":0,
                \"rain\_storm\":0,
                \"rain\_storm\_start\_at\":1553187660,
                \"rainfall\_daily\":10,
                \"rainfall\_monthly\":10,
                \"rainfall\_year\":10,
                \"wind\_speed\_hi\_last\_10\_min\":null,
                \"wind\_dir\_at\_hi\_speed\_last\_10\_min\":null
        },
        {
                \"lsid":3724542100,
                \"data\_structure\_type\":1,
                \"txid\":3,
                \"wind\_speed\_last\":0.00,
                \"wind\_dir\_last\":0.0,
                \"rain\_size\":0,
                \"rain\_rate\_last\":0,
                \"rain\_15\_min\":0,
                \"rain\_60\_min\":0,
                \"rain\_24\_hr\":0,
                \"rain\_storm\":0,
                \"rain\_storm\_start\_at\":1553143540,
                \"rainfall\_daily\":0,
                \"rainfall\_monthly\":0,
                \"rainfall\_year\":0,
                \"wind\_speed\_hi\_last\_10\_min\":null,
                \"wind\_dir\_at\_hi\_speed\_last\_10\_min\":null
        }\]
}

###### Second Broadcast Packet (with next 3 ISS Sensors):

{

        \"did\":\"001D0A700002\",
        \"ts\":1532031640,
        \"conditions\": \[
        {
                \"lsid":4261413012,
                \"data\_structure\_type\":1,
                \"txid\":4,
                \"wind\_speed\_last\":0.00,
                \"wind\_dir\_last\":0.0,
                \"rain\_size\":0,
                \"rain\_rate\_last\":0,
                \"rain\_15\_min\":0,
                \"rain\_60\_min\":0,
                \"rain\_24\_hr\":0,
                \"rain\_storm\":0,
                \"rain\_storm\_start\_at\":1553143540,
                \"rainfall\_daily\":0,
                \"rainfall\_monthly\":0,
                \"rainfall\_year\":0,
                \"wind\_speed\_hi\_last\_10\_min\":null,
                \"wind\_dir\_at\_hi\_speed\_last\_10\_min\":null
        },
        {
                \"lsid":2902458513,
                \"data\_structure\_type\":1,
                \"txid\":5,
                \"wind\_speed\_last\":0.00,
                \"wind\_dir\_last\":0.0,
                \"rain\_size\":0,
                \"rain\_rate\_last\":0,
                \"rain\_15\_min\":0,
                \"rain\_60\_min\":0,
                \"rain\_24\_hr\":0,
                \"rain\_storm\":0,
                \"rain\_storm\_start\_at\":1553143540,
                \"rainfall\_daily\":0,
                \"rainfall\_monthly\":0,
                \"rainfall\_year\":0,
                \"wind\_speed\_hi\_last\_10\_min\":null,
                \"wind\_dir\_at\_hi\_speed\_last\_10\_min\":null
        },
        {
                \"lsid":3187671185,
                \"data\_structure\_type\":1,
                \"txid\":6,
                \"wind\_speed\_last\":0.00,
                \"wind\_dir\_last\":0.0,
                \"rain\_size\":0,
                \"rain\_rate\_last\":0,
                \"rain\_15\_min\":0,
                \"rain\_60\_min\":0,
                \"rain\_24\_hr\":0,
                \"rain\_storm\":0,
                \"rain\_storm\_start\_at\":1553143540,
                \"rainfall\_daily\":0,
                \"rainfall\_monthly\":0,
                \"rainfall\_year\":0,
                \"wind\_speed\_hi\_last\_10\_min\":null,
                \"wind\_dir\_at\_hi\_speed\_last\_10\_min\":null
        }\]
}

###### Third Broadcast Packet (with remaining 2 ISS Sensors):

{

        \"did\":\"001D0A700002\",
        \"ts\":1532031640,
        \"conditions\": \[
        {
                \"lsid":4261413012,
                \"data\_structure\_type\":1,
                \"txid\":7,
                \"wind\_speed\_last\":0.00,
                \"wind\_dir\_last\":0.0,
                \"rain\_size\":0,
                \"rain\_rate\_last\":0,
                \"rain\_15\_min\":0,
                \"rain\_60\_min\":0,
                \"rain\_24\_hr\":0,
                \"rain\_storm\":0,
                \"rain\_storm\_start\_at\":1553143540,
                \"rainfall\_daily\":0,
                \"rainfall\_monthly\":0,
                \"rainfall\_year\":0,
                \"wind\_speed\_hi\_last\_10\_min\":null,
                \"wind\_dir\_at\_hi\_speed\_last\_10\_min\":null
        },
        {
                \"lsid":2902458513,
                \"data\_structure\_type\":1,
                \"txid\":8,
                \"wind\_speed\_last\":0.00,
                \"wind\_dir\_last\":0.0,
                \"rain\_size\":0,
                \"rain\_rate\_last\":0,
                \"rain\_15\_min\":0,
                \"rain\_60\_min\":0,
                \"rain\_24\_hr\":0,
                \"rain\_storm\":0,
                \"rain\_storm\_start\_at\":1553143540,
                \"rainfall\_daily\":0,
                \"rainfall\_monthly\":0,
                \"rainfall\_year\":0,
                \"wind\_speed\_hi\_last\_10\_min\":null,
                \"wind\_dir\_at\_hi\_speed\_last\_10\_min\":null
        }\]

}

#### Appendix

##### Possible Error Responses with Improperly Formatted
Requests

###### Sample HTTP Request

**curl -X GET -H \"application/json\"
http://10.189.36.37:80/v1/current\_condition**

###### Response string

{

    \"data\":null,
    \"error\":{
                "code":404
                "message":\"HTTP Page Not Found\"
    }
}

###### Sample HTTP Request

**curl -X GET -H \"application/json\"
http://10.189.36.37:80/+v1/current\_condition**

###### Response string

{

    \"data\":null,
    \"error\":{
                "code":400
                "message":\"HTTP Bad Request\"
    }
}

###### Sample HTTP Request

**curl -X GET -H \"application/json\"
http://10.189.36.37:80/+v1/current\_conditionHost:
weatherlinklive-700017Accept:\*/\*Accept-Language: en-usConnection:
keep-alive**

###### Response string

{

    \"data\":null,
    \"error\":{
                "code":414
                "message": \"HTTP URI Too Long\"
    }
}

###### Sample HTTP Request - When there are no ISS Transmitter configured, but Real-Time broadcast request is made)

**curl -X GET -H \"application/json\"
<http://10.189.36.37:80/v1/real_time> (or)**

**curl -X GET -H \"application/json\"
<http://10.189.36.37:80/v1/real_time?duration=xxx>**

###### Response string

{

    \"data\":null,
    \"error\":{
                "code":409
                "message": \"No ISS Transmitters. Real Time broadcast not enabled\"
    }
}

###### Current Conditions HTTP Request -- Helper Module

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

###### Real-Time UDP Broadcast Request -- Helper Module

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
