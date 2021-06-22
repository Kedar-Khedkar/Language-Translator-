from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('wBfieaiKFK5oGu5UtBYkaiT3AswMWAibH5lhivnuqZoS')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.eu-gb.language-translator.watson.cloud.ibm.com')
supported_lang_list=[]

languages = language_translator.list_languages().get_result()
for i in range(76):
    if languages['languages'][i]['supported_as_target']==True & languages['languages'][i]['supported_as_source']==True:
        supported_lang_list.append(languages['languages'][i]['language_name'])
supported_lang_list.sort()
print(len(supported_lang_list))