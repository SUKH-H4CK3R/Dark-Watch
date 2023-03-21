import pyfiglet
import webbrowser
import time
user_input = ("Dark WaTch")
ascii_banner = pyfiglet.figlet_format(user_input)
print('\033[1;32;40m')
print(ascii_banner)
print('\033[0m')
print('\033[1;32;40m''''
------------------------------
|Scripy by ——————»SUKH H4CK3R|
------------------------------''')

user_input = input('''
1. Track Number to Location
2. YouTubeb Channel
3. Exit
4. If you can see any error then you DM me on Instagram \n
''')
if user_input.lower() == "1":
    # Execute next command here
    print("Wait...\n")
    time.sleep(5)
elif user_input.lower() == "2":
 	#Re-Direct YouTube Channel
 	channel_url = "https://youtube.com/@Sukh_H4CK3R"
 	webbrowser.open(channel_url)
 	exit()
 	time.sleep(5)
elif user_input.lower() == "3":
    # Exit the tool
    print("Exiting tool...")
    exit()
    time.sleep(5)
elif user_input.lower() == "4":
    	insta_url = "https://instagram.com/__king_of_hackers__?igshid=ZDdkNTZiNTM="
    	webbrowser.open(insta_url)
    	exit()
    	print("wait...")
    	time.sleep(5)
else:
    print("Invalid input. Please enter valid number")
    time.sleep(5)
  
 
number = input('\033[94mEnter Number With Country Code That You Want Trace : \n \033[0m')
