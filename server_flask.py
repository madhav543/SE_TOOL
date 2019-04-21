
from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit
import os
import subprocess
app = Flask(__name__)
app.config['SECRET_KEY'] = 'yalamanchili Engineers'
socketio = SocketIO(app)

@socketio.on('my event')
def handle_my_custom_event(apk_name):
    apk = str(apk_name)
    #subprocess.call(str(cmd),shell=True)
    #print('received data: ' + str(cmd))
    print('python3 app2.py '+apk+'/AndroidManifest.xml')
    os.system("apktool d "+apk+".apk -f -o ./"+apk)
    os.system("echo 'python3 app2.py '+apk+'/AndroidManifest.xml' ")
    #os.system('python3 server.py')
    os.system('python3 app2.py '+apk+'/AndroidManifest.xml')
    os.system('python3 r.py')
    f = open('result.txt','r')
    msg = f.read()
    emit('response',msg)



if __name__ == '__main__':
    socketio.run(app)


