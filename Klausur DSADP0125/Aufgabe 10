#Aufgabe 10 Klausur

def sucheWorthaeufigkeit(string, suche):
    wortHaeufigkeit = []

    einzelneWoerter = string.split()

    for wort in einzelneWoerter:
        wort = wort.strip(".,!?").lower()
        einzelneBuchstaben = [*wort]
        for buchstabe in einzelneBuchstaben:
            if buchstabe == suche:
                if wort not in wortHaeufigkeit:
                    wortHaeufigkeit.append(wort)

    return wortHaeufigkeit

testSuche = "n"
testString = "Python ist eine moderne Programmiersprache"

worthaeufigkeit = sucheWorthaeufigkeit(testString, testSuche)
print(worthaeufigkeit)
