# -*- coding: utf-8 -*-
import csv
import json

speakers = {}

with open('cfp.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for r in reader:
        speakers[r['Your name']] = \
            {
                "bio": r['Bio'],
                "company": r['Company'],
                "companyLogo": "TODO",
                "socials": r['Social links'],
                "name": r['Your name'],
                "photoUrl": "TODO",
                "country": r['Where you will be travelling from?'],
                # r['Position'],
                "talk_title": r['Title of your talk/workshop'],
                "talk_desc": r['Short description of your talk/workshop:'],
                "talk_for_who": r['For whom is this suitable?'],
                "talk_topic": r['Which field is most relevant to your topic?'],
            }
empty = {
    "bio": "TODO",
    "company": "TODO",
    "companyLogo": "TODO",
    "socials": "TODO",
    "name": "TODO",
    "photoUrl": "TODO",
    "country": "TODO",
    # r['Position'],
    "talk_title": "TODO",
    "talk_desc": "TODO",
    "talk_for_who": "TODO",
    "talk_topic": "TODO",
}

# print(speakers.keys())
# WTF !!!
speakers['Sofia Huts'] = speakers['Sofia']
speakers['Petr Nálevka'] = speakers['Petr Nalevka']
speakers['Vigneshwer Dhinakaran'] = speakers['Vigneshwer']

# MISSING
speakers['Jindrich Sarson'] = empty
speakers['Jana Moudrá'] = empty
speakers['Daniel Stenberg '] = empty
speakers['Nik Page'] = empty

speakers_final = []
talks = {}

with open('speakers.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    speaker_c = 1
    talk_c = 100
    for r in reader:
        # print(r["Name"], r["Firma"], r["Název talku/workshopu"],
        #       r["Topic"], speakers[r["Name"]])
        speakers_final.append(speakers[r["Name"]])
        talks[str(talk_c)] = {
            "complexity": speakers[r["Name"]]["talk_for_who"],
            "description": speakers[r["Name"]]["talk_desc"],
            "id": talk_c,
            "language": "English",
            "speakers": [speaker_c],
            # r["Topic"]
            "tags": [speakers[r["Name"]]["talk_topic"]],
            "title": r["Název talku/workshopu"]
            # speakers[r["Name"]]["talk_title"],
        }
        speaker_c += 1
        talk_c += 1

json.dump(speakers_final, open("speakers.json", "w"))
json.dump(talks, open("talks.json", "w"))
