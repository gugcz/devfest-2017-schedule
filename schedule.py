# -*- coding: utf-8 -*-

import csv
import json


def find_session_by_name(name, sp, se):
    if name == "Vitalík":
        name
    for i in sp:
        if i["name"] == name:
            uid = i["id"]
            for k, v in se.items():
                for s in v["speakers"]:
                    if s == uid:
                        return s
    return "TODO {}".format(name)


def main():
    speakers = json.load(open("speakers_final.json"))
    sessions = json.load(open("sessions.json"))

    with open('schedule_d1.csv', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        s = []
        for r in reader:
            s.append({
                "endTime": r['END'],
                "sessions": [
                    [find_session_by_name(r['Name1'], speakers, sessions)],
                    [find_session_by_name(r['Name2'], speakers, sessions)],
                    [find_session_by_name(r['Name3'], speakers, sessions)]
                ],
                "startTime": r["START"],
            })

    with open('schedule_d2.csv', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        w = []
        for r in reader:
            w.append({
                "endTime": r['END'],
                "sessions": [
                    [find_session_by_name(r['Name1'], speakers, sessions)],
                    [find_session_by_name(r['Name2'], speakers, sessions)],
                    [find_session_by_name(r['Name3'], speakers, sessions)],
                    [find_session_by_name(r['Name4'], speakers, sessions)],
                    [find_session_by_name(r['Name5'], speakers, sessions)],
                ],
                "startTime": r["START"],
            })

    d = {
        "schedule": [{
            "date": "TODO",
            "dateReadable": "TODO",
            "timeslots": s,
            "tracks": [{
                "title": "TODO"
            }, {
                "title": "TODO"
            }, {
                "title": "TODO"
            }]
        }, {
            "date": "TODO2",
            "dateReadable": "TODO2",
            "timeslots": w,
            "tracks": [{
                "title": "TODO WS 1"
            }, {
                "title": "TODO WS 2"
            }, {
                "title": "TODO WS 3"
            }, {
                "title": "TODO WS 4"
            }, {
                "title": "TODO WS 5"
            }]
        }]}

    json.dump(d, open("schedule.json", "w", encoding="utf-8"),
              ensure_ascii=False, sort_keys=True, indent=3)

if __name__ == "__main__":
    main()
