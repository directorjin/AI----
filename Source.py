# 0 part
speechKey = '74a7729fe2ba4d9ba250393acbd98c63'
transTextKey = "27128296ac2f48188c3b7a9553103b70"

pip install
SpeechRecognition
conda install - c
anaconda pyaudio - -yes

# 1 part
import requests, http.client, urllib.request, urllib.parse, urllib.error, base64, json, urllib
from xml.etree import ElementTree

textToTranslate = input('Please enter some text: \n')
fromLangCode = input('What language is this?: \n')
toLangCode = input('To what language would you like it translated?: \n')

try:
    # Connect to server to get the Access Token
    apiKey = transTextKey
    params = ""
    headers = {"Ocp-Apim-Subscription-Key": apiKey}
    AccessTokenHost = "api.cognitive.microsoft.com"
    path = "/sts/v1.0/issueToken"

    conn = http.client.HTTPSConnection(AccessTokenHost)
    conn.request("POST", path, params, headers)
    response = conn.getresponse()
    data = response.read()
    conn.close()
    accesstoken = "Bearer " + data.decode("UTF-8")

    # Define the request headers.
    headers = {
        'Authorization': accesstoken
    }

    # Define the parameters
    params = urllib.parse.urlencode({
        "text": textToTranslate,
        "to": toLangCode,
        "from": fromLangCode
    })

    # Execute the REST API call and get the response.
    conn = http.client.HTTPSConnection("api.microsofttranslator.com")
    conn.request("GET", "/V2/Http.svc/Translate?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    translation = ElementTree.fromstring(data.decode("utf-8"))
    print(translation.text)
    conn.close()

except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

# 2 part
import IPython
import http.client, urllib.parse, json
from xml.etree import ElementTree

# Get the input text
myText = translation.text
# The Speech API requires an access token (valid for 10 mins)
apiKey = speechKey
params = ""
headers = {"Ocp-Apim-Subscription-Key": apiKey}
AccessTokenHost = "api.cognitive.microsoft.com"
path = "/sts/v1.0/issueToken"

# Use the API key to request an access token
conn = http.client.HTTPSConnection(AccessTokenHost)
conn.request("POST", path, params, headers)
response = conn.getresponse()
data = response.read()
conn.close()
accesstoken = data.decode("UTF-8")

# Now that we have a token, we can set up the request
body = ElementTree.Element('speak', version='1.0')
body.set('{http://www.w3.org/XML/1998/namespace}lang', 'en-us')
voice = ElementTree.SubElement(body, 'voice')
voice.set('{http://www.w3.org/XML/1998/namespace}lang', 'en-US')
voice.set('{http://www.w3.org/XML/1998/namespace}gender', 'Male')
voice.set('name', 'Microsoft Server Speech Text to Speech Voice (en-US, JessaRUS)')
voice.text = myText
headers = {"Content-type": "application/ssml+xml",
           "X-Microsoft-OutputFormat": "riff-16khz-16bit-mono-pcm",
           "Authorization": "Bearer " + accesstoken,
           "X-Search-AppId": "07D3234E49CE426DAA29772419F436CA",
           "X-Search-ClientID": "1ECFAE91408841A480F00935DC390960",
           "User-Agent": "TTSForPython"}

# Connect to server to synthesize a wav from the text
conn = http.client.HTTPSConnection("speech.platform.bing.com")
conn.request("POST", "/synthesize", ElementTree.tostring(body), headers)
response = conn.getresponse()
data = response.read()
conn.close()

# Play the wav
IPython.display.Audio(data, autoplay=True)

# part 3
import speech_recognition as sr

# Read the audio file
r = sr.Recognizer()
with sr.AudioFile('audio1.wav') as source:
    audio = r.listen(source)

# transcribe speech using the Bing Speech API
try:
    transcription = r.recognize_bing(audio, key=speechKey)
    print("Here's what I heard:")
    print('"' + transcription + '"')

except sr.UnknownValueError:
    print("The audio was unclear")
except sr.RequestError as e:
    print(e)
    print("Something went wrong :-(; {0}".format(e))

# part 4
import requests, http.client, urllib.request, urllib.parse, urllib.error, base64, json, urllib
from xml.etree import ElementTree

try:
    # Connect to server to get the Access Token
    apiKey = transTextKey
    params = ""
    headers = {"Ocp-Apim-Subscription-Key": apiKey}
    AccessTokenHost = "api.cognitive.microsoft.com"
    path = "/sts/v1.0/issueToken"

    conn = http.client.HTTPSConnection(AccessTokenHost)
    conn.request("POST", path, params, headers)
    response = conn.getresponse()
    data = response.read()
    conn.close()
    accesstoken = "Bearer " + data.decode("UTF-8")

    # Define the request headers.
    headers = {
        'Authorization': accesstoken
    }

    # Define the parameters
    params = urllib.parse.urlencode({
        "text": transcription,
        "to": fromLangCode,
        "from": toLangCode
    })

    # Execute the REST API call and get the response.
    conn = http.client.HTTPSConnection("api.microsofttranslator.com")
    conn.request("GET", "/V2/Http.svc/Translate?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    translation = ElementTree.fromstring(data.decode("utf-8"))
    print(translation.text)
    conn.close()

except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

# part 5
print("입력한 것 : ")
print(textToTranslate)
print("번역된 것 : ")
print(translation.text)
money = 1
if textToTranslate == translation.text:
    print("\n결과가 같습니다")
else:
    print("\n결과가 같지 않습니다")