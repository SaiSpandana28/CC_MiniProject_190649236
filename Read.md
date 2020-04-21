Name: Dadi Sai Spandana
Student id :190649236

The Project is part of the course work for Cloud Computing

It is an application to track the statistics of countries affected by Coronavirus

Steps to be implemented :

Create a t2.medium instance in AWS and connect to it through the terminal using the .pem key file by following the commands ssh -i key_name.pem ubuntu@public_dns of instance.

TO CONNECT TO AN EXTERNAL API

Once the instance is up and running create a file app.py . The programm is written in a way that it would connect to an external api and retrieve the results and display as a webpage.
The name of the api that this application connects to is Coronavirus COVID19 API 'https://api.covid19api.com/'
The application is implemented with the help of Flask with appropiate requiremts in the file requirements.txt and image details in Dockerfile
The file app.py has the following set of features:

1)It would give the statistics till date of the countries affected including TotalConfirmed , Deaths and the url to execute in the browser is http://ec2-3-89-33-139.compute-1.amazonaws.com/summary
2)It would give the increemental details of the cases in a country from the day the first case was recorded Url to be executed is http://ec2-3-89-33-139.compute-1.amazonaws.com/dayone/country/<countryname>
3)It would give a list of countries affected by Coronavirus. URL is http://ec2-3-89-33-139.compute-1.amazonaws.com/countries
4)It would give the stats of he cases worldwide URL is http://ec2-3-89-33-139.compute-1.amazonaws.com/sum

TO STORE PERSISTENT INFORMATION AND ACCESS FROM CLOUD DATABASE 

The file COVID_Data_Basic.csv is taken and copied into EC2 instance. A docker container is created and the latest version of ccassandra is pulled into it. The file is then copied to the Container.
A connection is made to the cqlsh and the neccesary keyspace[COVID19] and tables are created[COVID19.stat] and the contents of the .csv file are copied and the following operations are performed on the tables
1) GET : Pulls a record from the table for a country with confirmed cases as on a date URL: http://ec2-3-89-33-139.compute-1.amazonaws.com/country/<country>
2) POST : Updates a record in the table for a id with confirmed cases for a date URL: http://ec2-3-89-33-139.compute-1.amazonaws.com/update/<id>/<confirmednumber>/<date> 
3) DELETE :Deletes a record in the table for a particular id  URL: http://ec2-3-89-33-139.compute-1.amazonaws.com/country/<id>

SERVING THE APPLICATION OVER HTTPS:

The name of the api that this application connects to is Coronavirus COVID19 API 'https://api.covid19api.com/'
A new file app2.py is created and it has the following set of features:

1)It would give the statistics till date of the countries affected including TotalConfirmed , Deaths and the url to execute in the browser is https://ec2-3-89-33-139.compute-1.amazonaws.com/summary
2)It would give the increemental details of the cases in a country from the day the first case was recorded Url to be executed is https://ec2-3-89-33-139.compute-1.amazonaws.com/dayone/country/<countryname>
3)It would give a list of countries affected by Coronavirus. URL is https://ec2-3-89-33-139.compute-1.amazonaws.com/countries
4)It would give the stats of he cases worldwide URL is https://ec2-3-89-33-139.compute-1.amazonaws.com/sum

The application servers over https and is implemented by importing the module pyopenssl and adding "ssl_context='adhoc' " in the app.run() command.
