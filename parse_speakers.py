# -*- coding: utf-8 -*-
import csv

with open('speakers.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for r in reader:
        print(r["Name"], r["Firma"], r["Název talku/workshopu"], r["Topic"])
