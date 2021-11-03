acatool
=======

_A tool for quickly identifying the French academie that a place belongs to._

This tool is purely there to avoid doing two google searches, one for the
departement that the town is in, then one for the academie that that
departement is in. Uses geo.api.gouv.fr along with some conversion tables
for departements taken from Wikipedia.

)(note that Caen and Rouen have since been merged into Normandie.)_

# Quick install

In your Terminal:

```
git clone https://github.com/tomcontileslie/acatool
cd acatool
sudo python3 setup.py install
```

# How to use acatool

The `acatool` command takes a single string as argument, referring to a village/town/city name.

```
$ acatool "orsay"
Request commune: orsay
Commune interpretation: Orsay
Departement: 91
Academie: Versailles
Academic region: Île-de-France
```
