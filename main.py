from colorama import Fore
import os
import fade
import time
import sys
op = input(f'{Fore.BLUE}Loign Code:{Fore.WHITE}\n')
if op != '20':
    print(f'{Fore.RED}Wrong')
    time.sleep(1)
    exit(-1)
else:
    print(f'{Fore.GREEN}welcome{Fore.RESET}')
    time.sleep(1)
    os.system('cls')
id = input(f'{Fore.YELLOW}Enter the user id :{Fore.WHITE}\n')
print(f'{Fore.CYAN}processing{Fore.RESET}')
time.sleep(2)
os.system('cls')
banner = f"""

            ─────────────────────────────────────────────────────────────────────────────────────────────────────
                ─██████████████─██████████─████████████████───██████████████─██████████████─██████████████─
                ─██░░░░░░░░░░██─██░░░░░░██─██░░░░░░░░░░░░██───██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─
                ─██░░██████░░██─████░░████─██░░████████░░██───██░░██████░░██─██████░░██████─██░░██████████─
                ─██░░██──██░░██───██░░██───██░░██────██░░██───██░░██──██░░██─────██░░██─────██░░██─────────
                ─██░░██████░░██───██░░██───██░░████████░░██───██░░██████░░██─────██░░██─────██░░██████████─
                ─██░░░░░░░░░░██───██░░██───██░░░░░░░░░░░░██───██░░░░░░░░░░██─────██░░██─────██░░░░░░░░░░██─
                ─██░░██████████───██░░██───██░░██████░░████───██░░██████░░██─────██░░██─────██░░██████████─
                ─██░░██───────────██░░██───██░░██──██░░██─────██░░██──██░░██─────██░░██─────██░░██─────────
                ─██░░██─────────████░░████─██░░██──██░░██████─██░░██──██░░██─────██░░██─────██░░██████████─
                ─██░░██─────────██░░░░░░██─██░░██──██░░░░░░██─██░░██──██░░██─────██░░██─────██░░░░░░░░░░██─
                ─██████─────────██████████─██████──██████████─██████──██████─────██████─────██████████████─
            ──────────────────────────────────────────────────────────────────────────────────────────────────────   
"""
faded_banner = fade.pinkred(banner)
for o in faded_banner:
 time.sleep(0.0001)
 sys.stdout.write(o)
 sys.stdout.flush()
perm = input(f'{Fore.YELLOW}Generate bot Link with permission{Fore.GREEN} ->{Fore.LIGHTBLUE_EX} [1]{Fore.LIGHTMAGENTA_EX}Adminstrator {Fore.LIGHTBLUE_EX}[2]{Fore.LIGHTMAGENTA_EX}No Permission\n{Fore.LIGHTRED_EX}>>>> {Fore.GREEN}')
if perm == '1':
    print(f'{Fore.BLUE}processing')
    time.sleep(2)
    print(f"  {Fore.GREEN}your Link: {Fore.RED}"+"https://discord.com/api/oauth2/authorize?client_id="+id+"&permissions=8&scope=bot")
    time.sleep(3)
    input(f'{Fore.CYAN}press anything...')
if perm == '2':
    print(f'{Fore.BLUE}processing')
    time.sleep(2)
    print(f"  {Fore.GREEN}your Link: {Fore.RED}"+"https://discord.com/api/oauth2/authorize?client_id="+id+"&permissions=0&scope=bot")
    time.sleep(3)
    input(f'{Fore.CYAN}press anything...')
#by hermione
