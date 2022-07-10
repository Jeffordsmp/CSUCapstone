# Imports
from __future__ import print_function
import json
from apiclient import discovery
from httplib2 import Http
from oauth2client import client, file, tools

def refresh():

    # Google Forms API Authentication
    SCOPES = "https://www.googleapis.com/auth/forms.responses.readonly"
    DISCOVERY_DOC = "https://forms.googleapis.com/$discovery/rest?version=v1"
    store = file.Storage('token.json')
    creds = None
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('client_secrets.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = discovery.build('forms', 'v1', http=creds.authorize(
        Http()), discoveryServiceUrl=DISCOVERY_DOC, static_discovery=False)
    form_id = '1xjg1eivlv4jixWrpaCleFrN5RAi6LpehrRplt9JbhiQ'

    # Send API Request to Google Forms
    result = service.forms().responses().list(formId=form_id).execute()

    # Clear data in JSON file
    f = open('results.json', 'r+')
    f.seek(0) 
    f.truncate() 
    f.close()

    # Put API results in JSON file
    f = open('results.json', 'w')
    json.dump(result,f)
    return

class FormsAPI:
    # Update JSON file with new Survay Responces
    def update(self):
        refresh()
        return