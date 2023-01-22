import nltk
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')

vader = SentimentIntensityAnalyzer()

df = pd.read_csv("C:\Cyber_Cyber\LiveMint\headlines.csv")


f = lambda title: vader.polarity_scores(title)['compound']
df['compoundScore'] = df['Headlines'].apply(f)
df['sentimentAnalysis'] = df['compound'].apply(lambda x: 'positive' if x >= 0 else 'negative')


import spacy
from spacy import displacy

NER = spacy.load("en_core_web_lg")

text1= NER(df.iloc[0, 0])

companyName = []
for index, row in df.iterrows():
    text1= NER(row[0])
    check = False
    for word in text1.ents:
        if word.label_ == 'ORG':
            company_name = word.text
            companyName.append(company_name)
            check = True
            break
    if not check:
        companyName.append("")

df['Company_Name'] = companyName

df.to_csv('Sentiment_analysis.csv',index = False)
