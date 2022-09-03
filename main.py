import pandas as pd
from natasha import *
import json

file = pd.read_csv('test_data.csv', delimiter=',', names=['dlg_id', 'line_n', 'role', 'text'])
file.reset_index()
d0 = []
d1 = []
d2 = []
d3 = []
d4 = []
d5 = []
for index, row in file.iterrows():
    if row['dlg_id'] == '0' and row['role'] == 'manager':
        d0.append(row['text'].lower())
    if row['dlg_id'] == '1' and row['role'] == 'manager':
        d1.append(row['text'].lower())
    if row['dlg_id'] == '2' and row['role'] == 'manager':
        d2.append(row['text'].lower())
    if row['dlg_id'] == '3' and row['role'] == 'manager':
        d3.append(row['text'].lower())
    if row['dlg_id'] == '4' and row['role'] == 'manager':
        d4.append(row['text'].lower())
    if row['dlg_id'] == '5' and row['role'] == 'manager':
        d5.append(row['text'].lower())


d = [d0, d1, d2, d3, d4, d5]

hello_words = ['здравствуйте', 'добрый']
introduce_words = ['зовут']
bye_words = ['всего', 'хорошего', 'до свидания']

answers = []

dialog_dict = {'dialog_id': 0, 'hello_phrase': '', 'introduce_phrase': '', 'manager_name': '',
               'company_name': '', 'bye_phrase': '', 'req': False}

extractor = NamesExtractor()

for en, dialog in enumerate(d):
    dialog_dict['dialog_id'] = en
    for phrase in dialog:
        buff = phrase.split(" ")
        for word in buff:
            if word in hello_words:
                dialog_dict['hello_phrase'] = phrase
            if word in introduce_words:
                dialog_dict['introduce_phrase'] = phrase
                text = phrase.title()
                matches = extractor(text)
                facts = [_.fact.as_json for _ in matches]
                dialog_dict['manager_name'] = facts[0]['first']
                if 'компания' in buff:
                    dialog_dict['company_name'] = buff[(buff.index('компания'))+1]
            if word in bye_words:
                dialog_dict['bye_phrase'] = phrase
            if dialog_dict['hello_phrase'] != '' and dialog_dict['bye_phrase'] != '':
                dialog_dict['req'] = True

    answers.append(dialog_dict)
    dialog_dict = {'dialog_id': 0, 'hello_phrase': '', 'introduce_phrase': '', 'manager_name': '',
                   'company_name': '', 'bye_phrase': '', 'req': False}

with open('anwers.json', 'w', encoding='UTF-8') as file:
    json.dump(answers, file, ensure_ascii=False)