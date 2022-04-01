import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
version = '2018-05-01'

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version=version,
    authenticator=authenticator
)

language_translator.set_service_url(url)

# languages = language_translator.list_languages().get_result()


def englishToFrench(englishText):
    frenchText = language_translator.translate(text=englishText, model_id='en-fi').get_result()['translations'][0]['translation']
    return frenchText

def frenchToEnglish(frenchText):
    englishText = language_translator.translate(text=frenchText, model_id='fi-en').get_result()['translations'][0]['translation']
    return englishText

print(json.dumps(englishToFrench('This is a good movie.'), indent=2, ensure_ascii=False))