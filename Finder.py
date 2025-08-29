import os
import sys
import time


try:

    try:

        import requests   #  ____________________
        import colorama   # /  import librarys  /
        import colored

    except:
        pass

except ImportError:
    time.sleep(3)
    sys.exit()

from colorama import Fore , init
from colored import fg , bg


init()


class start:

    def first(url , damin , method):

        _url = url
        _damin = damin
        _method = method



        if _method == "first":

            _url = url
            _damin = open(damin).read().split("\n")
            _method = method

            print(Fore.GREEN + '[ + ]' + ' ' + 'your Target ( url ) >> ' + Fore.YELLOW + _url) # | print url target |
            print('\n')

            try:
                _r = requests.get("http://" + _url)

                if (
                    _r.status_code == 404 or #  _______________
                    _r.status_code == 401 or # [ status erorrs ]
                    _r.status_code == 402 or
                    _r.status_code == 403):

                    time.sleep(3)
                    sys.exit()

            except KeyboardInterrupt:
                time.sleep(3)
                sys.exit()

            for __dmn in _damin:

                __url = ("http://" + __dmn + "." + _url)

                try:

                    try:
                        __r = requests.get(__url)
                        print(Fore.GREEN + "[ 200 ]" + " " + "Found one login page ( Url )> " + fg('black') + bg('green') + __url + "\033[00m")   # for response 200 [ OK ]

                    except:
                        print(Fore.RED + "[ 404 ]" + " " + "Not found ( Url )> " + fg('black') + bg('red') + __url + "\033[00m")       # for response 404 [ not fond ]


                except KeyboardInterrupt:
                    time.sleep(3)
                    sys.exit()



    def second(url , damin , method):

        try:

            _url = url
            _damin = damin
            _method = method

            if _method == "second":

                _url = url
                _damin = open(damin).read().split("\n")
                _method = method

                print(Fore.GREEN + '[ + ]' + ' ' + 'your Target ( url ) >> ' + Fore.YELLOW + _url) # | print url target |

                try:
                    _r = requests.get("http://" + _url)

                    if (
                        _r.status_code == 404 or #  _______________
                        _r.status_code == 401 or # [ status erorrs ]
                        _r.status_code == 402 or
                        _r.status_code == 403):

                        time.sleep(3)
                        sys.exit()

                except KeyboardInterrupt:
                    time.sleep(3)
                    sys.exit()

                for __dmn in _damin:

                    __url = ("http://" + _url + __dmn)

                    try:

                        try:
                            __r = requests.get(__url)
                            if __r.status_code == 200:
                                print(Fore.GREEN + "[ 200 ]" + " " + "Found one login page! ( Url )> " + fg('red') + bg('black') + __url + "\033[00m")
                            else:
                                print(Fore.RED + "[ 404 ]" + " "  + "Not found ( Url )> " + fg('red') + bg('black') + __url + "\033[00m")

                        except:
                            time.sleep(3)
                            sys.exit()



                    except KeyboardInterrupt:
                        time.sleep(3)
                        sys.exit()
        except:
            time.sleep(3)
            sys.exit()

try:
    try:
        if(sys.argv[0]):

            ___method___ = sys.argv[1]
            ___url___ = sys.argv[2]

            if ___method___ == "first":

                try:

                    if(sys.argv[3]):
                        ___damin___ = sys.argv[3]
                        start.first(___url___ , ___damin___ , ___method___) # first
                except:
                    ___damin___ = "dir1.txt"
                    start.first(___url___ , ___damin___ , ___method___) # first



            if ___method___ == "second":

                try:

                    if(sys.argv[3]):
                        ___damin___ = sys.argv[3]
                        start.second(___url___ , ___damin___ , ___method___) # first
                except:
                    ___damin___ = "dir2.txt"
                    start.second(___url___ , ___damin___ , ___method___) # first



        # if ___method___ == "first":
        #     if ___damin___ == "":

        #         ___damin___ = "dir1.txt"

        #         start.first(___url___ , ___damin___ , ___method___) # first


        # start.first(___url___ , ___damin___ , ___method___) # first

        # if ___method___ == "second":
        #     if ___damin___ == "":

        #         ___damin___ = "dir2.txt"

        #         start.second(___url___ , ___damin___ , ___method___) # first


        #     start.second(___url___ , ___damin___ , ___method___) # first




    except:

        print("\033[92m" + '''

               Admin Panel Directory Finder!
            ==================================
           |            By JaakeSec           |
            ==================================

                    [ first ]:
                        find = 'admin.google.com'

                    [ second ]:
                        find = 'google.com/admin'


                    [ Run ]:
                        python Finder.py --method --url --dir1

                        [ Example ]:
                            python Finder.py first google.com dir1

        ''')

except KeyboardInterrupt:
    time.sleep(3)
    sys.exit()





pass
