#!/usr/bin/python3

"""
author : sadeceben
github : https://github.com/sadeceben?tab=repositories
"""


import requests
import sys
import time

def main(urls , wordlist):
       n = time.time()
       r_file = open(str(wordlist))
       url = str(urls)
       header = {'User-Agent':'Mozilla/5.0 (Android 4.3; Tablet; rv:50.0) Gecko/50.0 Firefox/50.0'}

       try:
            r = requests.get(url, headers=header)
            if r.status_code != 200:
                  print("Host not found")
                  exit
            else:
                  print("Host Connected")

            for w in r_file:
                  n_url = url + "/" + w.replace("\n","")
                  res = requests.get(n_url, headers=header)
                  if res.status_code == 200:
                        print("200: " + url + "/" + w.replace("\n",""))


            r_file.close()

       except Exception as e:
             print(e)
             r_file.close()

       l = time.time()
       print("Elapsed Time : " + str(l-n))


if __name__ == '__main__':
        main( sys.argv[1] , sys.argv[2] )

