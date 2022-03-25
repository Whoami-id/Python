class InvalidEmailError(Exception):
    pass


def send_email(email, subject, content):
    if not "@" in email:
        raise InvalidEmailError("Email does not contain an @")

try:
    send_email("hallo", "betreff", "inhalt")
except InvalidEmailError:
    print("Bitte gebe eine gültige E-Mail ein")
