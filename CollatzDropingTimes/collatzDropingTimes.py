#plot.ly Example
#This https://plot.ly/~GermanJimenez/0

import plotly
import os

def collatzStopingTime(n):
    c = 0
    while n != 1:
        if n % 2 == 0: n /= 2
        else: n = ( 3 * n ) + 1
        c += 1
    return c

def average(l):
    return sum(l)/len(l)

limit = 2000

#Collatz algorithm stoping times-------------------------------------

#Coordinates
collatzTrace = {
                'x': range( 1, limit ),
                'y': [collatzStopingTime( n ) for n in range(1,limit)]
                }
#Styles
collatzTraceStyles = {
                "type":"scatter",
                "name":"Collatz stoping times",
                "line":{"color":"orange",
                        "width":2,
                        "dash":"solid",
                        "opacity":0.2
                        }
                }

#Collatz algorithm stoping times averages-----------------------------------

rang = limit/100
la = [collatzTrace['y'][x:x+rang] for x in range(0, len(collatzTrace['y']), rang)]
xs = range(1,limit+2,rang)

ys = [average(l) for l in la]
ys.append(ys[len(ys)-1])

#Coordinates
collatzAverages = {
                'x': xs,
                'y': ys,
                }

#Styles
collatzAveragesStyles = {
                "type":"scatter",
                "name":"Stoping times averages (%s)" % rang,
                "line":{"opacity": 0.3,
                        "color":"gray",
                        "width":3,
                        "dash":"solid"
                        },
                }
#-------------------------------------------------------------------------------

#response = plotly.signup(username, email) #Signup

#loggin
username = str(raw_input("Username: "))
email =  str(raw_input("e-mail: "))
key =  str(raw_input("Key: "))

py = plotly.plotly(username, key)

response = py.plot(collatzTrace,collatzAverages)
py.style(collatzTraceStyles,collatzAveragesStyles)

url = response['url']
filename = response['filename']

if url:
    os.system('firefox %s' % url)
    #os.system('explorer %s' % url)
    #os.system('google-chrome %s' % url)

#This https://plot.ly/~GermanJimenez/0