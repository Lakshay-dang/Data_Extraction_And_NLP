# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd
import numpy as np
import nltk
nltk.download("popular")
df=pd.read_csv("Sheet1.csv")

df

input1=df["URL_ID"]
input2=df['URL']

df.info()
len(df)

for u in range(0,len(df)):
  if(u==0):
    lis1='AI in healthcare to Improve Patient Outcomes'
  U=df["URL"][u]
  UU=df["URL_ID"][u]
  U=str(U)
  url = U
  try:
    page = urlopen(url)
  except:
    print("skip")
  html = page.read().decode("utf-8")
  soup = BeautifulSoup(html, "html.parser")
  a=soup.find_all('h1', attrs={'class': 'entry-title'})
  for i in a:
    lis1=i.text
  #print(lis1)
  #print(lis1)
  lis2=''
  for x in soup.find_all('div',attrs={"class":"td-post-content"}):
    foo_descendants = x.descendants
    for d in foo_descendants:
      if d.name == 'p':
        lis2=lis2+d.text
  final= lis1+"\n"+lis2
  
  name=str(UU)+"."+"txt"
  #print(name)
  if(len(final)<3):
    final="Cannot find this url"

  #print(u,final)
  file = open(name, "a")
  a = file.write(final)
  file.close()

StopWords_Currencies="AFGHANI  | Afghanistan ,ARIARY | Madagascar ,BAHT | Thailand ,BALBOA | Panama ,BIRR | Ethiopia ,BOLIVAR | Venezuela ,BOLIVIANO  | Bolivia ,CEDI | Ghana ,COLON  | Costa Rica ,C”RDOBA  | Nicaragua,DALASI | Gambia ,DENAR | Macedonia (Former Rep.) ,DINAR | Algeria ,DIRHAM  | Morocco ,DOBRA | S„o Tom and,DONG | Vietnam ,DRAM | Armenia ,ESCUDO  | Cape Verde ,EURO  | Belgium ,FLORIN | Aruba ,FORINT | Hungary ,GOURDE | Haiti ,GUARANI | Paraguay ,GULDEN | Netherlands Antilles ,HRYVNIA  | Ukraine ,KINA | Papua New Guinea ,KIP | Laos ,KONVERTIBILNA MARKA  | Bosnia-Herzegovina ,KORUNA  | Czech Republic ,KRONA | Sweden ,KRONE | Denmark ,KROON | Estonia,KUNA | Croatia ,KWACHA | Zambia ,KWANZA | Angola ,KYAT | Myanmar ,LARI | Georgia ,LATS | Latvia ,LEK | Albania ,LEMPIRA | Honduras ,LEONE | Sierra Leone ,LEU | Romania ,LEV | Bulgaria ,LILANGENI  | Swaziland ,LIRA | Lebanon ,LITAS | Lithuania ,LOTI | Lesotho ,MANAT | Azerbaijan ,METICAL | Mozambique ,NAIRA | Nigeria ,NAKFA | Eritrea ,NEW LIRA | Turkey ,NEW SHEQEL  | Israel ,NGULTRUM  | Bhutan ,NUEVO SOL | Peru ,OUGUIYA  | Mauritania ,PATACA | Macau ,PESO  | Mexico ,POUND  | Egypt ,PULA  | Botswana ,QUETZAL | Guatemala ,RAND | South Africa ,REAL  | Brazil ,RENMINBI  | China ,RIAL | Iran ,RIEL | Cambodia ,RINGGIT | Malaysia ,RIYAL | Saudi Arabia ,RUBLE | Russia ,RUFIYAA | Maldives ,RUPEE  | India ,RUPEE  | Pakistan ,RUPIAH  | Indonesia ,SHILLING  | Uganda ,SOM | Uzbekistan ,SOMONI  | Tajikistan ,SPECIAL DRAWING RIGHTS  | International Monetary Fund ,TAKA | Bangladesh ,TALA | Western Samoa ,TENGE | Kazakhstan ,TUGRIK  | Mongolia ,VATU | Vanuatu ,WON  | Korea, South ,YEN | Japan ,ZLOTY | Poland"

lis_stopWords=['StopWords_Auditor','StopWords_DatesandNumbers','StopWords_Generic','StopWords_GenericLong','StopWords_Geographic','StopWords_Names']

stopword=[]

for i in lis_stopWords:
  j=str(i)
  j=j+".txt"
  try:
    f=open(j,"r+") 
  except:
    f=open(j,"r+",encoding='ISO-8859-1')
  v=f.read()
  k=v.splitlines()
  for m in k:
    m=str(m)
    m=m.split('|')
    stopword.append(m[0])

StopWords_Currencies=StopWords_Currencies.split(" ,")
for i in StopWords_Currencies:
  i=str(i)
  i=i.split("|")
  stopword.append(i[0])

from nltk.corpus import stopwords
import string
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()
def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    
    y = []
    for i in text:
        if i.isalnum():
            y.append(i)
    
    text = y[:]
    y.clear()
    
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
            
    text = y[:]
    
            
    return text

Positive_Score_lis=[]
Negative_Score_lis=[]
Polarity_Score_lis=[]
Subjectivity_Score_lis=[]
AVG_SENTENCE_LENGTH_lis=[]
perc_complex_words_lis=[]
Fog_Index_lis=[]
AVG_NUMBER_OF_WORDS_PER_SENTENCE_lis=[]
complex_word_count_lis=[]
total_word_count_cleaned_lis=[]
avg_syllable_word_count_lis=[]
count_pro_lis=[]
Average_Word_length_lis=[]
for i in range(37,151):
  j=str(i)
  j=j+".txt"
  print(j)
  if(j=="44.txt" or j=='57.txt' or j=='144.txt'):
    Positive_Score_lis.append("N/A")
    Negative_Score_lis.append("N/A")
    Polarity_Score_lis.append("N/A")
    Subjectivity_Score_lis.append("N/A")
    AVG_SENTENCE_LENGTH_lis.append("N/A")
    perc_complex_words_lis.append("N/A")
    Fog_Index_lis.append("N/A")
    AVG_NUMBER_OF_WORDS_PER_SENTENCE_lis.append("N/A")
    complex_word_count_lis.append("N/A")
    total_word_count_cleaned_lis.append("N/A")
    avg_syllable_word_count_lis.append("N/A")
    count_pro_lis.append("N/A")
    Average_Word_length_lis.append("N/A")
  else:
    f=open(j,"r+") 
    v=f.read()
    ###COUNT_PRO
    count_pro=0
    words=v.split(" ")
    list_pro=['I', 'we','my', 'ours', 'us']
    for word in words:
      if word in list_pro:
        count_pro=count_pro+1
    print('count_pro',count_pro)
    #AVG_SENTENCE_LENGTH
    #before clean
    sents=0
    for dot in v:
      if(dot=="."):
        sents=sents+1
    Words=v.split(" ")
    count_words=len(Words)
    AVG_SENTENCE_LENGTH=count_words/(sents+1)
    print("AVG_SENTENCE_LENGTH",AVG_SENTENCE_LENGTH)
    AVG_NUMBER_OF_WORDS_PER_SENTENCE=AVG_SENTENCE_LENGTH
    print('AVG_NUMBER_OF_WORDS_PER_SENTENCE',AVG_SENTENCE_LENGTH)


    #########
    words=v.split(" ")

    complex_words = []
    for word in words:
      vowels = 'aeiou'
      syllable_count_word = sum( 1 for letter in word if letter.lower() in vowels)
      if syllable_count_word > 2:
        complex_words.append(word)


    syllable_count = 0
    syllable_words =[]
    for word in words:
      if word.endswith('es'):
        word = word[:-2]
      elif word.endswith('ed'):
        word = word[:-2]
      vowels = 'aeiou'
      syllable_count_word = sum( 1 for letter in word if letter.lower() in vowels)
      if syllable_count_word >= 1:
        syllable_words.append(word)
        syllable_count += syllable_count_word
    perc_complex_words=(len(complex_words)*100)/len(words)
    complex_word_count=len(complex_words)
    print("complex_word_count",len(complex_words))
    print("perc_complex_words",perc_complex_words)
    Fog_Index = 0.4 * (AVG_SENTENCE_LENGTH + perc_complex_words)
    print("Fog_Index",Fog_Index)
    avg_syllable_word_count = syllable_count / len(syllable_words)
    print("SYLLABLE_PER_WORD",avg_syllable_word_count)
    ############
    v=transform_text(v)
    total_word_count_cleaned=len(v)
    print('total_word_count_cleaned',total_word_count_cleaned)
    for word in v:
      if word in stopword:
        v.remove(word)
    p='positive-words'+".txt"
    n='negative-words' + '.txt'
    pp=open(p,"r+") 
    nn=open(n,"r+", encoding = "ISO-8859-1")
    p=pp.read()
    n=nn.read()
    positive_list=p.splitlines()
    negative_list=n.splitlines()
    pos=0
    neg=0
    for i in v:
      if i in positive_list:
        pos=pos+1
      if i in negative_list:
        neg=neg+1
    Negative_Score=-1*neg
    Positive_Score=pos
    Polarity_Score = (Positive_Score - Negative_Score)/ ((Positive_Score + Negative_Score) + 0.000001)
    Subjectivity_Score = (Positive_Score + Negative_Score)/ ((len(v)) + 0.000001)
    print("N",Negative_Score)
    print('P',Positive_Score)
    print('Polarity',Polarity_Score)
    print('Subjectivity',Subjectivity_Score)
    ########
    word_len=0
    for charac in v:
      word_len=word_len+len(charac)
    Average_Word_length=word_len/len(v)
    print('Average_Word_length',word_len/len(v))
    
    Positive_Score_lis.append(Positive_Score)
    Negative_Score_lis.append(Negative_Score)
    Polarity_Score_lis.append(Polarity_Score)
    Subjectivity_Score_lis.append(Subjectivity_Score)
    AVG_SENTENCE_LENGTH_lis.append(AVG_SENTENCE_LENGTH)
    perc_complex_words_lis.append(perc_complex_words)
    Fog_Index_lis.append(Fog_Index)
    AVG_NUMBER_OF_WORDS_PER_SENTENCE_lis.append(AVG_NUMBER_OF_WORDS_PER_SENTENCE)
    complex_word_count_lis.append(complex_word_count)
    total_word_count_cleaned_lis.append(total_word_count_cleaned)
    avg_syllable_word_count_lis.append(avg_syllable_word_count)
    count_pro_lis.append(count_pro)
    Average_Word_length_lis.append(Average_Word_length)
    f.close()

input_=input1.tolist()

input__=input2.tolist()

Output = pd.DataFrame(list(zip(input_,
input__,
Positive_Score_lis,
Negative_Score_lis,
Polarity_Score_lis,
Subjectivity_Score_lis,
AVG_SENTENCE_LENGTH_lis,
perc_complex_words_lis,
Fog_Index_lis,
AVG_NUMBER_OF_WORDS_PER_SENTENCE_lis,
complex_word_count_lis,
total_word_count_cleaned_lis,
avg_syllable_word_count_lis,
count_pro_lis,
Average_Word_length_lis)),
               columns =["URL_ID",
"URL",
'POSITIVE SCORE',
'NEGATIVE SCORE',
'POLARITY SCORE',
'SUBJECTIVITY SCORE',
'AVG SENTENCE LENGTH',
'PERCENTAGE OF COMPLEX WORDS',
'FOG INDEX',
'AVG NUMBER OF WORDS PER SENTENCE',
'COMPLEX WORD COUNT',
'WORD COUNT',
'SYLLABLE PER WORD',
'PERSONAL PRONOUNS',
'AVG WORD LENGTH'
])

Output.head(151)

from google.colab import files
Output.to_csv('Output.csv') 
files.download('Output.csv')
