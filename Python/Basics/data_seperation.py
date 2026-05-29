# How to separate usernames from the list of emails.
# Split with list comprehension technique is use for this

emails = list(['balkrushna@gmail.com', 'soumya23@gmail.com', 'rahual24@icloud.com'])
emails.extend(['kashish@gmail.com','eva234@gmail.com','priyasable23@gmail.com'])
print(emails)

usernames = [email.split('@')[0] for email in emails]
print(usernames)
for i in usernames:
    print(i)

domains = [email.split('@')[1] for email in emails]
print(domains)


