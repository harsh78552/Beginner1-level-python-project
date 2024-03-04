email = input("Enter your email account: ")
check = 0
if len(email) >= 6:
    if email[0].isalpha():
        if '@' in email and email.count('@') == 1:
            if ('.' in email[-4:] or '.' in email[-3:]) and email.count('.') == 1:
                for character in email:
                    if character == " ":
                        check = 1
                    elif character.isdigit():
                        continue
                    elif character == "_" or character == "@":
                        continue
                    elif character == '#' or character == '!' or character == '$' or character == '%' or character == '^' or character == '&' or character == '*' or character == '(' or character == ')' or character == '+' or character == '+' or character == '/' or character == ':' or character == ';' or character == ',' or character == '<' or character == '>' or character == '?':
                        print("Invalid Email: Special Character are not allowed.")
                if check == 1:
                    print("Invalid Email: Space not allowed.")
            else:
                print("Invalid Email: only one . allowed.")
        else:
            print("Invalid Email: Only one @ allowed.")
    else:
        print("Invalid Email: First character must be alphabetic.")
else:
    print("Invalid Email: Email address should be at least 6 character long.")
