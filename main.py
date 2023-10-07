import pandas as pd
import smtplib

data = pd.read_csv('scores.csv')
MY_EMAIL = "youremail@email.com"
PASSWORD = "yourpassword"
info = data.to_dict(orient="records")


file_path = "script.txt"
for n in range(len(info)):
    with open(file_path) as letter_file:
        score = info[n]['score']
        if score == 'na':
            with open("noscore.txt") as letter:
                contents = letter.read()
                contents = contents.replace("[parent]", str(info[n]['parent']))
                contents = contents.replace("[student]", str(info[n]['student']))
        else:
            contents = letter_file.read()
            contents = contents.replace("[parent]", str(info[n]['parent']))
            contents = contents.replace("[student]", str(info[n]['student']))
            contents = contents.replace("[score]", str(info[n]['score']))

    with smtplib.SMTP("smtp-mail.outlook.com", port=587) as connection:
        #This is the host location for outlook, if your provider is different you will need a different host
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=info[n]['pemail'],
            msg=f"Subject: Student subject test score at Your School \n\n{contents}"
        )