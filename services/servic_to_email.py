def check_email(data):
    sentences = data['sentences']
    new_sen = ""
    for i in sentences:
        new_sen += i
    new_sen.replace('.',' ')

    if "hostage" in new_sen:
        return "hostage"
    elif"explos" in new_sen:
        return "explos"
    else:
        return