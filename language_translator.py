#Imports 
import supported_languages
import tkinter as tk
import tkinter.scrolledtext as st
from tkinter import font, messagebox, ttk

import language_tool_python #grammar checker for voice input
import speech_recognition as sr
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import LanguageTranslatorV3
from ttkthemes import ThemedStyle
from ttkwidgets.autocomplete import AutocompleteCombobox

authenticator = IAMAuthenticator('API-key') #IBM variable for api authentication. Replace with your Api key
language_translator = LanguageTranslatorV3(version='2018-05-01',authenticator=authenticator)
language_translator.set_service_url('URL') #Replace with your URL

# Initialize recognizer class (for recognizing the speech)

r = sr.Recognizer()
#============================================================================================================================
#GUI
window =tk.Tk()
window.resizable(False,False)#resizable(x-dim,y-dim)
Font_tuple = ("Geneva",'15' ,'bold')
#Setting Theme
style=ThemedStyle(window)
style.set_theme("equilux")
window.config(bg="#1a1b26")
window.iconbitmap(r'translator_icon.ico')
s=ttk.Style()
s.configure('.', font=('Helvetica', 12,'bold'),foreground='#6697f3')
# title
window.title("LANGUAGE TRANSLATOR")

#Functions
#----------------------------------------------------------------------------------------------------------------
def translation_process():
    try:
        text_showed.insert(tk.INSERT,language_translator.translate(text=text_entered.get("1.0",'end-1c'),target=language_choose.get() ).get_result()['translations'][0]['translation']+'\n')
    except :
        messagebox.showerror("showerror", "Error! Language not supported")# shows error message 
    #text_showed.configure(state ='disabled')# Making the text read only


def clear():
    text_entered.delete("1.0", "end")
    text_showed.delete("1.0", "end")

# Optional 
def voice_input():
    with sr.Microphone() as source:
        audio_text = r.listen(source)
        try:
            translation_vtext= r.recognize_google(audio_text)
            tool = language_tool_python.LanguageTool('en-US')
            text_vin = translation_vtext
            correct_text=tool.correct(text_vin)
            text_entered.insert(tk.INSERT,correct_text)
        except:
            messagebox.showerror("showerror","Sorry, I did not get that")

#-----------------------------------------------------------------------------------------------------------------
#Label
ttk.Label(window,text='Enter the text to be translated ',font=Font_tuple,background='#1a1b26',foreground='#6697f3').grid(column=0,row=0,pady=5)

#Input box
text_entered=st.ScrolledText(window,wrap = tk.WORD,width = 40,height = 7,font = ("Helvetica",10))
text_entered.grid(column = 0, pady = 10, padx = 10)
text_entered.focus()# Placing cursor in the text area
text_entered.config(bg='#1a1b26',fg='#6697f3')

#Voice Button (optional)
voiceButton=ttk.Button(window,text='Voice input',command=voice_input)
voiceButton.grid(column=0, pady = 10)

#Clear Button
clear_action=ttk.Button(window,text='Clear',command=clear)
clear_action.grid(column=0, pady = 10)


#Label
ttk.Label(window,text='Select language',font=Font_tuple,background='#1a1b26',foreground='#6697f3').grid(column=0,pady=10)

#Drop down menu with autocomplete
language_var=tk.StringVar()
language_choose_values=supported_languages.supported_lang_list #From the supported languages script
language_choose=AutocompleteCombobox(window,width=20,textvariable=language_var,completevalues=language_choose_values,font=Font_tuple)
language_choose.grid(column=0,row=4)
language_choose.current()

#Translate button
action=ttk.Button(window,text='Translate',command=translation_process)
action.grid(column=0,row=5,pady=10)


#Label 
ttk.Label(window,text='Translated Text:',font=Font_tuple,background='#1a1b26').grid(column=0,row=6)

#Output box
text_showed=st.ScrolledText(window,width = 40,height = 7,font = ("Helvetica",10))
text_showed.grid(column = 0, pady = 10, padx = 10)
text_showed.config(bg='#1a1b26',fg='#6697f3')

window.mainloop()
#=============================================================================================================================
