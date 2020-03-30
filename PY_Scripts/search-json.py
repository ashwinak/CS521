##For a given user defined key, print value of another key##

import json
with open('shiva.json') as json_file:
    try:
        data = json.load(json_file)
        store = []
        jsonID = raw_input ("Enter the ID: ")
        for p in data['paragraphs']:
            txt = [p['id'],p['text']]
            #print len(txt)
            #for indexj,jsonstr in enumerate(txt):
            #print indexj,jsonstr
            if jsonID == txt[0]:
                print "\n####The text for " + txt[0] + " is::-> \n\n" + txt[1] + "\n\n"
                break
            else:
                continue
    except KeyError:
        print "###Cannot find the ID " + jsonID + "\n"
    except KeyboardInterrupt:
        print "\n ###User interrupted program####"