from instagrambot import InstaFollower
HEDEF = "yazilimaorg"


bot = InstaFollower()
bot.login()
bot.find_followers(HEDEF)
bot.follow()