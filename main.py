import logbot

webhook_url = 'https://discord.com/api/webhooks/1134890479515865188/7qkSK6JkWukxpFtqsmgi1Jiz0-w8EfWUkENwYOoM0ktW07XPJ1UYAYl4Z1yyijbGmiFj'  

# Create an instance of Logbot  
logbot = logbot.Logbot(webhook_url)

# Monitor syslog 
logbot.monitor_file('/var/log/syslog', level='INFO')

# Monitor auth.log  
logbot.monitor_file('/var/log/auth.log', level='WARNING')

# Run Logbot  
logbot.run()