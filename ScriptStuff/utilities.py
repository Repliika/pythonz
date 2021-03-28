def email_clean(email_list) :
    clean_email_list = []
    for email in email_list:
        clean_email_list.append(email.rstrip())
        clean_email_list = set(clean_email_list)
        clean_email_list = list(clean_email_list)
    
    return clean_email_list