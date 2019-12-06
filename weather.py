import requests
from pprint import pprint

print('''

          *******                  ***                      *******                 **              
    *       ***              ** ***                   *       ***    *           **             
   *         **             **   ***                 *         **   ***          **             
   **        *              **                       **        *     *           **             
    ***                     **                        ***                        **             
   ** ***           ****    ******      ***          ** ***        ***       *** **      ***    
    *** ***        * ***  * *****      * ***          *** ***       ***     *********   * ***   
      *** ***     *   ****  **        *   ***           *** ***      **    **   ****   *   ***  
        *** ***  **    **   **       **    ***            *** ***    **    **    **   **    *** 
          ** *** **    **   **       ********               ** ***   **    **    **   ********  
           ** ** **    **   **       *******                 ** **   **    **    **   *******   
            * *  **    **   **       **                       * *    **    **    **   **        
  ***        *   **    **   **       ****    *      ***        *     **    **    **   ****    * 
 *  *********     ***** **  **        *******      *  *********      *** *  *****      *******  
*     *****        ***   **  **        *****      *     *****         ***    ***        *****   
*                                                 *                                             
 **                                                **                                           
                                                                                                
                                                        
    ''')

print('                                                                                                    ')
print('                                  Welcome To SafeSide')
print('                                                                                                    ')
print('                                                                                                    ')
print('                  Weather alerts to help keep you on the safe side')
print('                                                                                                    ')
print('''


''')
print('                                                                                                    ')
print('                                                                                                    ')
city = input('                            Enter your city: ')

url='https://weather.cit.api.here.com/weather/1.0/report.json?product=alerts&name={}&app_id=DemoAppId01082013GAL&app_code=AJKnXv84fjrb0KIHawS0Tg'.format(city)

url2='https://openweathermap.org/data/2.5/weather?q={}&appid=b6907d289e10d714a6e88b30761fae22'.format(city)

res = requests.get(url)

res2 = requests.get(url2)

data = res.json()

data2 = res2.json()

# pprint(data2)
# print(data)



print(r''' 
        
                     _   _                       _           _   
                    | | | |                     | |         | |  
 __      _____  __ _| |_| |__   ___ _ __    __ _| | ___ _ __| |_ 
 \ \ /\ / / _ \/ _` | __| '_ \ / _ \ '__|  / _` | |/ _ \ '__| __|
  \ V  V /  __/ (_| | |_| | | |  __/ |    | (_| | |  __/ |  | |_ 
   \_/\_/ \___|\__,_|\__|_| |_|\___|_|     \__,_|_|\___|_|   \__|
''')

pprint(data) 
if 'Type' in data:
    print('               Sorry , City Unavailable')

elif data['alerts']['alerts'] == []:
    print('               Nothing to worry about No extreem weather in ', city)

else: 
    print('               alert :' , data['alerts']['alerts'][0]['description'],'. Stay safe')

print(r''' 
        
                     _   _                                           _  
                    | | | |                                         | |  
 __      _____  __ _| |_| |__   ___ _ __   _ __ ___ _ __   ___  _ __| |_ 
 \ \ /\ / / _ \/ _` | __| '_ \ / _ \ '__| | '__/ _ \ '_ \ / _ \| '__| __|
  \ V  V /  __/ (_| | |_| | | |  __/ |    | | |  __/ |_) | (_) | |  | |_ 
   \_/\_/ \___|\__,_|\__|_| |_|\___|_|    |_|  \___| .__/ \___/|_|   \__|
                                                   | |                   
                                                   |_|   
''')



if data2['cod'] == 500 :
    print('                 Sorry! City unavailable')
else:
    print(                   city,'weather :' )

    humidity = data2['main']['humidity']
    temp = data2['main']['temp']
    pressure = data2['main']['pressure']
    description = (data2['weather'][0]['description'])

    print('humidity :', humidity)
    print('temperature :', temp , 'degrees celcius')
    print('pressure :', pressure)
    print('description :' , description)









    

