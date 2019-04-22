# SE_TOOL

ABOUT THE TOOL:
This tool is used to draw permissions from the android app description and these permissions are cross checked with that of the permissions
that are listed in androidmanifest.xml file.
Based on the cross checking, if the permissions that are listed in the manifest file are not matches with that of the required permissions,
we get form the app description then this tool makes us to visualize the security threats by displaying the security threat message.

FILES AND THEIR DESCRIPTION:
server.py is used for launching the stanfordcorenlp server.
app2.py is used to list the permissions that are in the manifest file in text file, output.txt .
description.txt consists of app description.
r.py is used to know whether the app requires READ_CONTACTS permission or not, based on the description.txt file and output.txt file.
why.html is the user interface, where we give the name of apk file as input, then it displays whether there is security threat or not.
server_flask.py automates the process of decoding the apk file to get the source code of manifest file and also runs the above pyhton files
(they are app2.py, r.py).
result.txt store the result from r.py i.e whether there is requirement of READ_CONTACTS permission or not. This text in result.txt is displayed
the browser.

REQUIREMENTS:
Stanfordcorenlp module is required.
app description should be in description.txt .
All the above listed files in the file description should be in the same directory i.e in stanfordcorenlp module.

HOW TO USE:
Start stanfordcorenlp parser (python3 server.py) .
Start server_flask.py (python3 server_flask.py) .
open the why.html, give apk name and click on 'GO' button. 
Result message will be displayed in the browser.

DIFFERENCES BETWEEN THE CURRENT VERSION AND RELEASE-2:
r.py is the sub module of the tool that is done in release-2.
Now, in this all the submodules that are app2.py, r.py are combined.
why.html is the user inteface that is added.
flask_server.py is added, which automates the running of all the submodules and sends the result message that is to be displayed to the browser.
