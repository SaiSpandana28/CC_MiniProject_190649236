
from flask import Flask, render_template, request, jsonify
from cassandra.cluster import Cluster
import json
import requests
import requests_cache
requests_cache.install_cache('covid_api_cache', backend='sqlite', expire_after=36000)

cluster = Cluster(contact_points =['3.88.175.145'],port = 9042)
session = cluster.connect()
app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>Hello, World!</h1>"

# Returns the overall stats per country including the Total Confirmed etc
@app.route('/summary', methods =['GET'])
def getsummarycountry():
    url='https://api.covid19api.com/summary'
    resp=requests.get(url)
    if resp.ok:
       resp=resp.json()
       response = [item for item in  resp["Countries"]]
       return jsonify(response)
    else:
        print(resp.reason)
    
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
      resp =resp.json()
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

#Retrieves a record from the database
@app.route('/country/<country>', methods =['GET'])
def getstats(country):
    rows = session.execute("""Select * From covid19.stats where country = '{}' ALLOW FILTERING""".format(country))
    for b in rows:
        return('<h1>{} has {} cases as on {} and has id {} </h1>'.format(country,b.confirmed,b.date,b.id))
            
    return('<h1> ID does not exist in the table </h1>')

# Deletes a record from the database
@app.route('/delete/<id>', methods=['GET','DELETE'])
def get_delete(id):
    rows = session.execute("""Delete from covid19.stats where id = {}""".format(id))
    return  'Deleted info of a id'

# Updates a record from the database given id , confirmes and the corresponding date as format
@app.route('/update/<id>/<confirmed>/<date>', methods =['GET','POST'])
def updatestats(id,confirmed,date):
     rows = session.execute("""Update covid19.stats set confirmed = {} , date='{}' where id = {} """.format(confirmed,date,id))
     return 'update successful'

#inserts a record in the database
@app.route('/insert/', methods =['GET','POST'])
def insert():
    id = request.json.get('id', '')
    confirmed = request.json.get('confirmed', '')
    country = request.json.get('country', '')
    date = request.json.get('date', '')
    death = request.json.get('death', '')
    newconfirmed = request.json.get('newconfirmed', '')
    newdeath = request.json.get('newdeath', '')
    newrecovered = request.json.get('newrecovered','')
    recovered = request.json.get('recovered', '')
    rows = session.execute("""Insert into covid19.stats(id,confirmed,country,date,death,newConfirmed,newDeath,newRecovered,recovered) values ({},{},'{}','{}',{},{},{},{},{}) """.format(id,confirmed,country,date,death,newconfirmed,newdeath,newrecovered,recovered))
    return 'Inserted stats successfully'
   
if __name__ == '__main__':
   app.run(host='0.0.0.0', port =80)
