# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 16:00:21 2020

@author: Steven.Nguyen
"""

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import httplib2

from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import run_flow

CLIENT_SECRET = 'N:\Temp\Steven Nguyen\pumpscores\client_secret.json'
SCOPE = 'https://www.googleapis.com/auth/spreadsheets'
STORAGE = Storage('credentials.storage')

# Start the OAuth flow to retrieve credentials
def authorize_credentials():
# Fetch credentials from storage
    credentials = STORAGE.get()
# If the credentials doesn't exist in the storage location then run the flow
    if credentials is None or credentials.invalid:
        flow = flow_from_clientsecrets(CLIENT_SECRET, scope=SCOPE)
        http = httplib2.Http()
        credentials = run_flow(flow, STORAGE, http=http)
    return credentials
creds = authorize_credentials()
client = gspread.authorize(creds)

spreadsheeturl = 'https://docs.google.com/spreadsheets/d/1ug9O5fZo-ZhZaNa_yaKLS_eJEBMcv9yscMwGqjcD1-0/edit#gid=0'
worksheetname = 'PIU Log'

spreadsheet = client.open_by_url(spreadsheeturl)
wrksheet = spreadsheet.worksheet(worksheetname)

row = ["I'm","inserting","a","new","row","into","a,","Spreadsheet","using","Python"]
wrksheet.append_row(row, value_input_option='RAW')