"""
Die hauptlogik hinter dem chatbot.
Der input wird durch den while-loop geschickt und gibt eine ausgabe aus.
Am anfang benutzt man noch das terminal.
"""

# importiert das dictionary
from dictionary_folder.conversations_all_languages import *

while True:
    # macht den input lowercase wegen Case-Sensitivity, spart code
    prompt1 = input().lower()

    # checkt nach möglichen treffern im dictionary
    if prompt1 in QA_DIC:
        print(QA_DIC[prompt1]) # hier printet es die antwort falls es gefunden wurde
    else:
        print("Ihre eingabe konnte nicht verstanden werden\nYour input couldn't be understood") # falls nicht, kommt das
