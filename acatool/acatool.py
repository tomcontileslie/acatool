import os
import requests
import csv
import sys
import pkgutil

DATABASE1 = "academies.csv"
DATABASE2 = "regions.csv"
WDIR      = os.path.dirname(os.path.realpath(__file__))
CONVERT   = []
REGIONS   = []
REQUEST   = "NOT SPECIFIED"

file = pkgutil.get_data(__name__, "data/" + DATABASE1)
r = csv.reader(file.decode('utf-8').splitlines())
for line in r:
    if len(line) > 0:
        strs  = set(s for s in line[1:] if s != "")
        strs |= set("0" + s for s in line[1:] if s!= "")
        CONVERT.append((line[0].split('\ufeff')[-1], strs))

file = pkgutil.get_data(__name__, "data/" + DATABASE2)
r = csv.reader(file.decode('utf-8').splitlines())
for line in r:
    if len(line) > 0:
        strs  = set(s for s in line[1:] if s != "")
        REGIONS.append((line[0].split('\ufeff')[-1], strs))

if len(sys.argv) > 1:
    REQUEST = sys.argv[1]

print("Request commune:", REQUEST)

r = requests.get('https://geo.api.gouv.fr/communes?nom=' + REQUEST + "&boost=population")

if len(r.json()) == 0:
    print("No results")
    exit()
else:
    dep = r.json()[0]["codeDepartement"]
    print("Commune interpretation:", r.json()[0]["nom"])
    print("Departement:", dep)

aca = ""
for a, s in CONVERT:
    if dep in s:
        aca = a

if aca == "":
    print("No academy found")
else:
    print("Academie:", aca)
    

reg = ""
for a, s in REGIONS:
    if aca in s:
        reg = a

if reg == "":
    print("No academic region found")
else:
    print("Academic region:", reg)

exit()
