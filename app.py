from flask import Flask, render_template, request
from nltk.sentiment import SentimentIntensityAnalyzer
from tqdm.notebook import tqdm
from nltk.corpus import stopwords
import nltk

# nltk.download('stopwords')
sia = SentimentIntensityAnalyzer()

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('home.html')

@app.route('/', methods = ['POST'])
def my_form_post():
    stop_words = stopwords.words('english')
    
    #convert to lowercase
    text1 = request.form['text1'].lower()
    
    text_final = ''.join(c for c in text1 if not c.isdigit())
    
    #remove punctuations
    #text3 = ''.join(c for c in text2 if c not in punctuation)
        
    #remove stopwords    
    processed_doc1 = ' '.join([word for word in text_final.split() if word not in stop_words])

    sa = SentimentIntensityAnalyzer()
    dd = sa.polarity_scores(text=processed_doc1)
    compound = round((1 + dd['compound'])/2, 2)
    if dd['pos'] > 0.5:
        return render_template('home.html',text1=text_final, final= compound, message = '😀')
    elif dd['neg'] > 0.5:
        return render_template('home.html',text1=text_final, final= compound, message = '🙁')
    else:
        return render_template('home.html',text1=text_final, final= compound, message = '😐')

    return render_template('home.html')

if __name__=="__main__":
    app.run(debug=True)