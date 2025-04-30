
## Initiaal  Imports 

import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
from googletrans import Translator


class SpeechDetector:

    @staticmethod
    def check_polarity(polarity):
        """
        Classify sentiment polarity into categories:
        - Positive: polarity > 0.1
        - Negative: polarity < -0.1
        - Neutral: otherwise
        """
        if polarity > 0.1: return "Positive"
        elif polarity < -0.1: return "Negative"
        else : return "Neutral"
        

    @staticmethod
    def detect(url):
        """
        Detects the sentiment of a headline (assumed in Bengali) from the given news article URL.
        Steps:
        - Fetch HTML content using requests
        - Parse and extract the headline with BeautifulSoup
        - Translate headline from Bengali to English using googletrans
        - Analyze sentiment using TextBlob
        - Return original headline and detected sentiment category
        """

        # Set headers to mimic a browser request to avoid being blocked
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers)

        # Parse HTML and extract the <h1> tag (usually the headline)
        soup = BeautifulSoup(response.text, 'html.parser')
        headline = soup.find('h1').get_text().replace('\n', ' ').strip()

        # Translate Bengali headline to English
        translator = Translator()
        translation = translator.translate(headline, src='bn', dest='en')
        english_headline = translation.text

        # Perform sentiment analysis on the translated headline
        analysis = TextBlob(english_headline)
        polarity = analysis.sentiment.polarity

        # Return original headline and sentiment category
        return {
            "Headline": headline,
            "Detect": SpeechDetector.check_polarity(polarity=polarity)
        }
