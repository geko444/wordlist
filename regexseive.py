import re

regex = r"\b(?:([a-y])(?!.*\1))*\b"
wordslist = open('wordlist.txt').read()
test_str = ("rearoused\n"
            "prejudicing\n"
            "sissyish\n"
            "grippiest\n"
            "parodos\n"
            "caswell\n"
            "epiphenomenalism\n"
            "fiend\n"
            "mistruster\n"
            "nondelusive\n"
            "sakhalin\n"
            "revitalized\n"
            "trilobed\n"
            "airwaybill\n"
            "decolorize\n"
            "scandian\n"
            "marathonian\n"
            "barbitone\n"
            "prerejoicing\n"
            "pavement")

matches = re.finditer(regex, wordslist)

f = open('seivedwords.txt', 'w')

for matchNum, match in enumerate(matches):
    matchNum = matchNum + 1
    if len(match.group()) != 0:
        f.write('{}\n'.format(match.group()))
        print match.group()

f.close()
