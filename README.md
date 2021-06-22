## Language Translator with GUI
******
🙋‍♂️Hi, I am Kedar Khedkar, a python developer.
In this project, I have made a **Language Translator** using **IBM Watson API**.
It has features like
1. Voice Input (only for English language)
2. Autocomplete drop-down list for language selection
3. 50 languages supported for translation

### Installing Dependencies
*********
Run this in terminal
`pip install tk`
`pip install ttkthemes`
`pip install ttkwidgets`
`pip install PyJWT==1.7.1 ibm_watson wget`
`pip install PyAudio`
`pip install language-tool-python`

### Access API
***********
You can access the api by creating IBM Watson account through this *[link](https://ibm.co/3vMLNJQ)* and get your own *Api key* and *Url*.
For api [documentation](https://cloud.ibm.com/apidocs/language-translator?code=python#translate).

### Code
**********
There are two scripts in the repository `supported_languages.py` and `language_translator.py`
`language_translator.py` is main script and `supported_languages.py` is used to extract the supported languages for translation and used.

In `supported_languages.py`, we have extracted the supporting languages from api and saved in a list, and that list is imported in `language_translator.py`
Replace *Api key* and *Url* with your own api key and url.


