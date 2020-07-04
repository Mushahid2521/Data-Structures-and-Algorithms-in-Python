def uniqueEmails(emails):
    uniq_mails = set()

    for email in emails:
        formatted_email = ''
        splits = email.split('@')

        flag = True
        for c in splits[0]:
            if c=='+':
                flag=False
            if c=='.':
                continue
            if flag:
                formatted_email+=c


        uniq_mails.add(formatted_email+'@'+splits[1])

    return len(list(uniq_mails))

print(uniqueEmails(["test.email+alex@leetcode.com","test.email.leet+alex@code.com"]))

