#!/bin/bash
# This is meant to use a key to allow it to send to git hub

openssl enc -pbkdf2 -nosalt -aes-256-cbc -in /home/bob/bootcon/bootcon_project_dec.py -out bootcon_project_enc.py -base64 -K 4EA2A56396E4BB2C30897C1B8C090F54E8F2E1308780B8795E6B53A6E74FD814  -iv E69CCC163DA315AC46D66149421B2658

echo [SUCCESS] File Encrypted.
