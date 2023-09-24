email = input("Enter your Email-id:").strip()
user_name = email[:email.index("@")]
domain_name = email[email.index("@")+1:]

format_name = (f"Your user name is: '{user_name}'and your domain name is'{domain_name}'")
print(format_name)

Output:
Enter your Email-id:abhilash3178@gmail.com
Your user name is: 'abhilash3178'and your domain name is'gmail.com'
