class EmailValidator:
    def __init__(self):
        pass

    def is_name_valid(self, name):
        pass

    def is_mail_valid(self, mail):
        pass

    def is_domain_valid(self, domain):
        pass

    def validate(self, email):
        pass


mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("pe77er@gmail.com"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.bg"))