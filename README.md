## Language Translator with GUI
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)<br>
🙋‍♂️Hi, I am Kedar Khedkar, a python developer.
In this project, I have made a **Language Translator** using **IBM Watson API**.<br>
It has features like:<br>
1. Voice Input (only for English language)
2. Autocomplete drop-down list for language selection
3. 50 languages supported for translation

[![image.png](https://i.postimg.cc/3RCrSJNV/image.png)](https://postimg.cc/9R0jz2GY)
### Installing Dependencies
*********
Run this in terminal<br>

`pip install tk`<br>
`pip install ttkthemes`<br>
`pip install ttkwidgets`<br>
`pip install PyJWT==1.7.1 ibm_watson wget`<br>
`pip install PyAudio`<br>
`pip install SpeechRecognition`<br>
`pip install language-tool-python`<br>

### Access API
***********
You can access the api by creating IBM Watson account through this *[link](https://ibm.co/3vMLNJQ)* and get your own *Api key* and *Url*. <br>
For api [documentation](https://cloud.ibm.com/apidocs/language-translator?code=python#translate).

### Code
**********
There are two scripts in the repository `supported_languages.py` and `language_translator.py`.<br>
`language_translator.py` is main script and `supported_languages.py` is used to extract the supported languages for translation and used.

In `supported_languages.py`, we have extracted the supporting languages from api and saved in a list, and that list is imported in `language_translator.py`<br>
Replace *Api key* and *Url* with your own api key and url.
