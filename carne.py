asada = '''

    Carne Asada Recipe

Ingredients

    2 pounds skirt steak trimmed of excess fat (recipe note #2)

Carne Asada Marinade

    1 jalapeño seeded and minced
    4 cloves garlic minced
    1/2 cup fresh cilantro leaves chopped
    juice of 1 orange
    juice of 1 lime
    juice of 1 lemon
    2 tablespoons apple cider vinegar
    1/3 cup olive oil
    1 teaspoon ground cumin
    1 teaspoon kosher salt
    1/4 teaspoon freshly ground black pepper

Instructions

    In a large glass baking dish whisk together Carne Asada marinade ingredients (jalapeño through black pepper) until combined. Add skirt steak in a single layer, turning to coat with marinade. Cover and refrigerate for at least 1 hour, but no longer than 8 hours (longer will begin to break down the meat - recipe note #3).
    When you're ready to grill: preheat an outdoor grill to medium-high heat. Grill steaks for 7 to 10 minutes per side, turning once for medium-rare. Remove steaks and allow to rest for 5 minutes.
    Slice thinly across the grain and serve.

Notes

    To make this version, we started with a recipe from Daniel Pinhasov and switched it up to make it our own: swapping in apple cider vinegar, reducing the oil a bit and adding a third citrus flavor (lemon) and some cumin. Adding lemon juice to the mix happened by chance. I'd just finished a batch of homemade tonic water which left us with a slew of lemons, limes and oranges, flesh and juice intact, sans zest. And I love the citrus trifecta - now I may always use making tonic water as an excuse to make Carne Asada!
    Ask your butcher or grocery meat counter for 'outside skirt steak' for the most flavorful and juicy results.
    Note that the longer you marinate the skirt steak, the more tender and flavorful it will be come. But be sure to grill it within 8 hours to maintain the texture of the meat.

'''

secret_var='dlbx ncjd epzy vovv'

import smtplib
from email.message import EmailMessage
import mimetypes
import os

def send_email(send_mail, send_pass, rec_mail, subject, body, image_path):

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = send_mail
    msg['To'] = rec_mail
    msg.set_content(body)

    mime_type, _ = mimetypes.guess_type(image_path)
    mime_type, mime_subtype = mime_type.split('/')

    with open(image_path, 'rb') as img:
        msg.add_attachment(img.read(),
                           maintype = mime_type,
                           subtype = mime_subtype,
                           filename=os.path.basename(image_path))
        
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(send_mail, send_pass)
        smtp.send_message(msg)
        print('[SUCCESS]')
