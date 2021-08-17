import requests 
import json
import pandas as pd
import matplotlib as plt

url = requests.get({('https://website.com/id', headers={'Authorization': 'access_token myToken'}))
... 

responseDict = json.loads(url.read())
dateTime = responseDict['STATION'][0]['OBSERVATIONS']['date_time']
airT = responseDict['STATION'][0]['OBSERVATIONS']['air_temp_set_1']
ksea = pd.Series(airT,index=pd.to_datetime(dateTime))

weather = pd.DataFrame(
    {
        "A": dateTime,
        "B": airT,
        "C": ksea, 
    }

)
print(weather.head())