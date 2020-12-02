#copy rights reserved
# ALL REQUIRED LIBRARIES

from pycorenlp import StanfordCoreNLP
from nltk.corpus import wordnet  #USED FOR FINDING SYNONYMUS WORDS
import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import Text,pos_tag

ps = PorterStemmer()
nlp = StanfordCoreNLP('http://localhost:9000') # connecting to the launched localhost stanford server
stop_words = set(stopwords.words('english'))   # stop_words contains the list of stopwords
txt = "App is used to send messages instantly."
#print(txt)
tokens = word_tokenize(txt) #TOKENIZES THE TEXT
#print(tokens)
text = Text(tokens) # HERE TEXT CONTAINS THE TOKENS
#print(text)
tags = pos_tag(text) # TAGS CONTAINS EACH TOKEN ASSOCIATED WITH THEIR PARTS OF SPEECH
#print(tags)
#print(type(tags[0]))
fil_list1 = [] # FOR STORING ALL THE NOUN RELATED WORDS
fil_list2 = []
r1 = []
r2 = []
count = 0
file = open('result.txt','w')

#FOR STORING THE WORDS THAT ARE  NOUNS IN FIL_LIST1
for i in range(len(tags)):
	if(tags[i][1]=='NN' or tags[i][1]=='NNS' or tags[i][1]=='NNP' or tags[i][1]=='NNPS'):
		#print(ps.stem(tags[i][0]))
		fil_list1.append(ps.stem(tags[i][0]))

# print(tags[0][1])

#BASED ON THE SEMANTIC GRAPH OF READ_CONTACTS PERMISSION PRESENT IN WHYPER PAPER
contacts_list1 = ['number','email','location','birthday','anniversary','messag']
contacts_list2 = ['display','read','search','get','send','share']


# FINDS ANY MATCHING BETWEEN FIL_LIST1 AND CONTACTS_LIST1, IF NO THEN THERE IS NO NEED OF THE PERMISSION
for i in fil_list1:
	if i in contacts_list1:
		r1.append(i)
		count = count+1
if(count == 0):
	print('no read_contact permission is needed')
	file.write('no READ_CONTACTS permission is needed, SECURITY THREAT')
	file.close()
	exit()


#FINDS MATCHING BETWEEN TOKENS AND CONTACT_LIST2, IF NO THEN THERE IS NO NEED OF PERMISISON		
for i in tokens:
	if i in contacts_list2:
		print('requires READ_CONTACTS permission')
		file.write('requires READ_CONTACTS permission, NO SECURITY THREAT')
		file.close()
		exit()

# FINDS SYNONYMUS WORDS OF TOKENS AND COMPARES WITH CONTATCS_LIST2
def get_word_synonyms_from_sent(word, sent):
    word_synonyms = []
    for synset in wordnet.synsets(word):
        for lemma in synset.lemma_names():
            if lemma in sent and lemma != word:
                word_synonyms.append(lemma)
    return word_synonyms

final=[]
for i in tokens:
	iterator = get_word_synonyms_from_sent(i,contacts_list2)
	final = final + iterator

file = open('result.txt','w')
if(len(final)!=0):
	print('requires READ_CONTACTS permission, NO SECURITY THREAT')
	file.write('requires READ_CONTACTS permission, NO SECURITY THREAT')

else:
	print('no READ_CONTACTS permission is needed, SECURITY THREAT')
	file.write('no READ_CONTACTS permission is needed, SECURITY THREAT')

file.close()



