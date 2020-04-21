from flask import Flask, render_template, request, jsonify
import json
import requests
import requests_cache
requests_cache.install_cache('covid_api_cache', backend='sqlite', expire_after=36000)

app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>Hello, World!</h1>"

# Returns the overall stats per country including the Total Confirmed etc
@app.route('/summary', methods =['GET'])
def getsummarycountry():
    url='https://api.covid19api.com/summary'
    resp= requests.get(url)
    if resp.ok:
       resp=resp.json()
       response = [ item for item in resp["Countries"]]
       return jsonify(response)       
    else:
       print(response.reason)

# Gives all the stats of the country from the day the first case was recorded

@app.route('/dayone/country/<country>', methods=['GET'])
def getcasesbycountry(country):
    url ='https://api.covid19api.com/dayone/country/'
    url = url + country
    resp = requests.get(url)
    if resp.ok:
       return jsonify(resp.json())
    else:
        print(resp.reason)


#Lists the set of countries affected by Corona
        
@app.route('/countries', methods =['GET'])
def getcountries():
    url ='https://api.covid19api.com/countries'
    resp=requests.get(url)
    if resp.ok:
       resp =resp.json
       response = [item["Country"] for item in resp]
       return jsonify(response)
    else:
        print(resp.reason)

#Gives the overall stats of corona cases all over the world
        
@app.route('/sum', methods = ['GET'])
def gettotal():
    url = 'https://api.covid19api.com/world/total'
    resp = requests.get(url)
    if resp.ok:
       return jsonify(resp.json())
    else:
      print(resp.reason)

if __name__ == '__main__':
      app.run(host='0.0.0.0', ssl_context='adhoc')
                                                                                               
