#This example plot
#https://plot.ly/~GermanJimenez/4/

import plotly
import os

def collatzStopTime(n):
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
                'y': [collatzStopTime( n ) for n in range(1,limit)],
                }

collatzTraceStyles = {
                "type":"scatter",
                "name":"Collatz Stop times",
                "line":{"color":"orange",
                        "width":2,
                        "dash":"solid",
                        "opacity":0.2
                        }
                }

#Collatz algorithm stop times averages-----------------------------------

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
                "name":"Stop times averages (%s)" % rang,
                "line":{"opacity": 0.3,
                        "color":"gray",
                        "width":3,
                        "dash":"solid"
                        },
                }
#-------------------------------------------------------------------------------

#response = plotly.signup(username, email) #Signup

#loggin
username = 'MyUsername'
email='MyEmail'
key = 'MyKey'

py = plotly.plotly(username, key)

response = py.plot(collatzTrace,collatzAverages)
response = py.style(collatzTraceStyles,collatzAveragesStyles)

url = response['url']
filename = response['filename']

if url:
    #os.system('firefox %s' % url)
    #os.system('explorer %s' % url)
    os.system('google-chrome %s' % url)

#This example plot
#https://plot.ly/~GermanJimenez/4/
