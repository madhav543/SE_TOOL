from xml.dom.minidom import parseString
import os
import sys
#apk_name = input("apk name :: ")
#os.system("apktool d "+apk_name+".apk -f -o ./"+apk_name)
#os.chdir(apk_name)

list1 = []
data = ''
with open(sys.argv[1],'r') as f:
    data = f.read()
dom = parseString(data)
nodes_1 = dom.getElementsByTagName('uses-permission')
nodes_2 = dom.getElementsByTagName('uses-permission-sdk-23')
file1 = open("output_1.txt",'w')
# Iterate over all the uses-permission nodes
for node_1 in nodes_1:
    #print (node_1.getAttribute('android:name'))
    file1.write(node_1.getAttribute('android:name')+'\n')
    list1.append(node_1.getAttribute('android:name')+'\n')
for node_2 in nodes_2:
    #print (node_2.getAttribute('android:name'))
    file1.write(node_2.getAttribute('android:name')+'\n')
    list1.append(node_1.getAttribute('android:name')+'\n')
