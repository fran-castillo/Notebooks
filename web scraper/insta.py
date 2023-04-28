import instaloader
bot= instaloader.Instaloader()
username= input('Username:')
print(bot.download_profile(username, profile_pic_only=True))
