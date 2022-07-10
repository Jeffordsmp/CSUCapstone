# CSUCapstone

This is my final project for CSU Gloabl

## Project Overview

This project will first take responses from a Google Forms Survay

[HERE IS THE GOOGLE SURVAY](https://forms.gle/A6QcZTDptSNuhZeeA)

The results from that survay are then stored into an SQL database that is hosted on AWS RDS

The data from there is then displayed using Plotly

This is what the Plotly Dashboard looks like

![plotly dash](/images/dash-img.png)

[**Here is a youtube video where I go through the project**](https://www.youtube.com/watch?v=pDXfJmG8MB8)


## What the Files do

### app.py

This is the main file 

It has the Plotly and Dash code

It aslo calls to start the other files

### client_secrets.json

This is a file with Google API log-in information

I have removed all of the content from it

### database.py

This is where the SQL conncetions and Commands are run

### find.py

This is the file that loops through the JSON file and Calls the database class to insert rows of data

### forms.py

This file calls the google forms API

### results.json

This is where the API results are kept

### token.json

This is another file that had Google authentication keys
