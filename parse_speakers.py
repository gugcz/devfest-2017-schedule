# -*- coding: utf-8 -*-
import csv
import json
import copy


def fill_talk_speaker(r, speakers, speaker_c, talk_c):
    speak = []
    talks = {}

    talks[str(talk_c)] = {
        "complexity": speakers[r["Name"]]["talk_for_who"],
        "description": speakers[r["Name"]]["talk_desc"],
        "id": talk_c,
        "language": "English",
        "speakers": [speaker_c],
        # r["Topic"]
        # "tags": [speakers[r["Name"]]["talk_topic"]],
        "tags": list(map(lambda x: x.strip(), r["Topic"].split(','))),
        "title": r["Název talku/workshopu"],
        # speakers[r["Name"]]["talk_title"],
    }
    for i in list(speakers[r["Name"]].keys()):
        if i.startswith("talk_"):
            del speakers[r["Name"]][i]
    speakers[r["Name"]]["name"] = r["Name"]
    speakers[r["Name"]]["company"] = r["Firma"]
    speakers[r["Name"]]["tags"] = talks[str(talk_c)]["tags"]
    speakers[r["Name"]]["photoUrl"] = speakers[r["Name"]]["photoUrl"].format(
        r["Name"].lower().replace(" ", "_"))
    speakers[r["Name"]]["id"] = speaker_c
    speak.append(speakers[r["Name"]])

    return speak, talks


def socials(s):
    r = {
        "link": s
    }
    if "facebook" in s:
        r.update({
            "icon": "facebook",
            "name": "Facebook"
        })
    if "github" in s:
        r.update({
            "icon": "github",
            "name": "GitHub"
        })
    if "twitter" in s:
        r.update({
            "icon": "twitter",
            "name": "Twitter"
        })
    if "linkedin" in s:
        r.update({
            "icon": "linkedin",
            "name": "LinkedIn"
        })
    if "plus" in s:
        r.update({
            "icon": "gplus",
            "name": "Google+"
        })
    if "icon" not in r:
        r.update({
            "icon": "website",
            "name": "Website"
        })
    return r


def main():
    speakers = {}

    with open('cfp.csv', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for r in reader:
            speakers[r['Your name']] = \
                {
                    "bio": r['Bio'],
                    "company": r['Company'],
                    "companyLogo": "TODO",
                    "socials": list(map(socials, r['Social links'].split())),
                    "name": r['Your name'],
                    "photoUrl": "/images/people/{}.jpg",
                    "country": r['Where you will be travelling from?'],
                    "featured": True,
                    "shortBio": "TODO",
                    "title": r['Position'],
                    "tags": [],
                    "talk_title": r['Title of your talk/workshop'],
                    "talk_desc": r['Short description of your talk/workshop:'],
                    "talk_for_who": r['For whom is this suitable?'],
                    "talk_topic": r[
                        'Which field is most relevant to your topic?'],
                }
    empty = {
        "bio": "TODO",
        "company": "TODO",
        "companyLogo": "TODO",
        "socials": [{
            "icon": "twitter",
            "link": "TODO",
            "name": "Twitter"
        }],
        "name": "TODO",
        "photoUrl": "TODO",
        "country": "TODO",
        "featured": True,
        "shortBio": "TODO",
        "tags": ["TODO"],
        "title": "TODO",
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
    speakers['Vít Listík'] = speakers['Vit Listik']
    speakers['Neha Sharma'] = speakers['Neha']

    # MISSING
    speakers['Jindrich Sarson'] = copy.deepcopy(empty)
    speakers['Jana Moudrá'] = copy.deepcopy(empty)
    speakers['Daniel Stenberg '] = copy.deepcopy(empty)
    speakers['Nik Page'] = copy.deepcopy(empty)

    speakers_final = []
    talks = {}

    speaker_c = 1
    talk_c = 100

    with open('speakers.csv', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for r in reader:
            # print(r["Name"], r["Firma"], r["Název talku/workshopu"],
            #       r["Topic"], speakers[r["Name"]])

            s, t = fill_talk_speaker(r, speakers, speaker_c, talk_c)
            speakers_final += s
            talks.update(t)
            speaker_c += 1
            talk_c += 1

    talk_c = 200

    with open('ws_speakers.csv', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for r in reader:
            s, t = fill_talk_speaker(r, speakers, speaker_c, talk_c)
            speakers_final += s
            talks.update(t)
            speaker_c += 1
            talk_c += 1

    json.dump(speakers_final, open("speakers.json", "w", encoding="utf-8"),
              ensure_ascii=False, sort_keys=True)
    json.dump(talks, open("talks.json", "w", encoding="utf-8"),
              ensure_ascii=False, sort_keys=True)


if __name__ == "__main__":
    main()
