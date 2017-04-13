# Simple program that demonstrates how to invoke Azure ML Text Analytics API: key phrases, language and sentiment detection.

import urllib2
import urllib
import sys
import base64
import json


# Azure portal URL.
base_url = 'https://westus.api.cognitive.microsoft.com/'
# Your account key goes here.
account_key = '0d8961f6987148b383030aab16180a95'

headers = {'Content-Type':'application/json', 'Ocp-Apim-Subscription-Key':account_key}
            
# input_texts = '{"documents":[{"id":"1","text":"hello world"},{"id":"2","text":"hello foo world"},{"id":"three","text":"hello my world"},]}'
file_path = '/home/eisandy/testapi/input.json'
f = open(file_path, 'r')
input_texts = f.read()

num_detect_langs = 1;

# Detect key phrases.
batch_keyphrase_url = base_url + 'text/analytics/v2.0/keyPhrases'
req = urllib2.Request(batch_keyphrase_url, input_texts, headers) 
response = urllib2.urlopen(req)
result = response.read()
print result  #-----------------------------------------------Return result from api
obj = json.loads(result)
for keyphrase_analysis in obj['documents']:
    keyPhrasesResult=('Key phrases ' + str(keyphrase_analysis['id']) + ': ' + ', '.join(map(str,keyphrase_analysis['keyPhrases'])))
    print keyPhrasesResult

# Detect language.
language_detection_url = base_url + 'text/analytics/v2.0/languages' + ('?numberOfLanguagesToDetect=' + num_detect_langs if num_detect_langs > 1 else '')
req = urllib2.Request(language_detection_url, input_texts, headers)
response = urllib2.urlopen(req)
result = response.read()
print result
obj = json.loads(result)
for language in obj['documents']:
    languagesResult=('Languages: ' + str(language['id']) + ': ' + ','.join([lang['name'] for lang in language['detectedLanguages']]))
    print languagesResult

# Detect sentiment.
batch_sentiment_url = base_url + 'text/analytics/v2.0/sentiment'
req = urllib2.Request(batch_sentiment_url, input_texts, headers) 
response = urllib2.urlopen(req)
result = response.read()
print result
obj = json.loads(result)
for sentiment_analysis in obj['documents']:
    sentimentResult=('Sentiment ' + str(sentiment_analysis['id']) + ' score: ' + str(sentiment_analysis['score']))
    print sentimentResult

# {"documents":[{"keyPhrases":[""],"id":"1"},{"keyPhrases":["life"],"id":"2"}],"errors":[]}
# Key phrases 1: 
# Key phrases 2: life
# {"documents":[{"id":"1","detectedLanguages":[{"name":"English","iso6391Name":"en","score":1.0}]},{"id":"2","detectedLanguages":[{"name":"English","iso6391Name":"en","score":1.0}]}],"errors":[]}
# Languages: 1: English
# Languages: 2: English
# {"documents":[{"score":0.9708645,"id":"1"},{"score":0.8016357,"id":"2"}],"errors":[]}
# Sentiment 1 score: 0.9708645
# Sentiment 2 score: 0.8016357








# html="""
# <html>
#     <head></head>
#     <body>
#         <label>Key: %s </label>
#         <br>            
#     </body>
# </html>""" % (cgi.escape(result3))

# template = get_template('/home/eisandy/sentest/mytemplate.html')
# self.response.write(template.render({'key_val':result3}))