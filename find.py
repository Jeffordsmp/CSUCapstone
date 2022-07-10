# Imports
import json
import database
import forms
db = database.DataBase()

# Inserts Survay Responces Into SQL Table
def insertAll():
    # Get the JSON data
    f = open('results.json')
    x = json.load(f)

    # Number used for ID in SQL tabel
    count = 0

    #Loop through JSON Object
    for i in x['responses']:
        count = count + 1
        v = i['answers']

        # Get the values from Each Question
        num = ((((v['7f97009b'])['textAnswers'])['answers'])[0])['value']
        ani = ((((v['467a25f4'])['textAnswers'])['answers'])[0])['value']
        col = ((((v['565f9430'])['textAnswers'])['answers'])[0])['value']

        # Insert this Responce's Awnser's to SQL
        db.insert(count, num, col, ani)


def letsPrint():
    f = open('results.json')

    x = json.load(f)
    count = 0

    for i in x['responses']:
        count = count + 1
        v = i['answers']
        num = ((((v['7f97009b'])['textAnswers'])['answers'])[0])['value']
        ani = ((((v['467a25f4'])['textAnswers'])['answers'])[0])['value']
        col = ((((v['565f9430'])['textAnswers'])['answers'])[0])['value']
        y = [count, num, col, ani]
        print(y)



class Update:

    # Refresh SQL table with new Survay Responces
    def refreshAPI(self):
        
        # Refresh JSON file with Updated Responces
        forms.FormsAPI().update()

        # Refresh SQL Table with Updated JSON file
        db.clear()
        insertAll()
        return
    
    def refreshJSON(self):
        db.clear()
        insertAll()
        return


    def printJSON(self):
        letsPrint()
        return
