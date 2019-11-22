from instabotai import ai
import argparse
from multiprocessing import Process, Queue
import pdb
import time
import threading
try:
    input = raw_input
except NameError:
    pass


COOKIES = {}
bot = ai.Bot(do_logout=True)

# Parse info from terminal
parser = argparse.ArgumentParser(add_help=True)
parser.add_argument('-u', type=str, help="username")
parser.add_argument('-p', type=str, help="password")
parser.add_argument('-proxy', type=str, help="proxy")
parser.add_argument('-user', type=str, help="user")
parser.add_argument('-sleep', type=int, help="sleep")
args = parser.parse_args()



class the_proccess(object):
    global username
    username = str(args.u)
    user = str(args.user)
    # Login on user
    ai.Bots.user_login(args.u, args.p)
    # Write info in file to fetch from html

    def write_file(filename, text):
        with open(username + filename + ".txt", "w+") as f:
            f.write(text)

    def open_file(self, filename):
        with open(username + filename + ".txt", "r") as f:
            read = f.read()
            read = read.rstrip('\n')
            return str(read)

    def follow_followers(self):
        user = self.open_file("user")
        times = self.open_file("time")
        times = int(times)
        user = str(user)
        ai.Bots.follow_users_followers_ai(user, times)

    def follow_following(self, user, time):
        user = self.open_file("user")
        times = self.open_file("time")
        times = int(times)
        user = str(user)
        ai.Bots.follow_users_followers_ai(user, times)

    def like_followers(self):
        user = self.open_file("user")
        times = self.open_file("time")
        times = int(times)
        user = str(user)
        ai.Bots.like_followers(user, times)

    def like_following(self):
        user = self.open_file("user")
        times = self.open_file("time")
        times = int(times)
        user = str(user)
        ai.Bots.like_following(user, times)

    def like_hashtags(self):
        user = self.open_file("user")
        times = self.open_file("time")
        times = int(times)
        user = str(user)
        ai.Bots.like_hashtags(user, times)

    def comment_hashtags(self):
        user = self.open_file("user")
        user = self.open_file("comment")
        times = self.open_file("time")
        times = int(times)
        user = str(user)
        comment = str(comment)
        ai.Bots.user_hashtag_comment(user, comment, times)

    def watch_stories(self):
        user = self.open_file("user")
        times = self.open_file("time")
        times = int(times)
        user = str(user)
        ai.Bots.watch_stories(user, times)

    def repost_images(self):
        user = self.open_file("user")
        times = self.open_file("time")
        caption = self.open_file("caption")
        times = int(times)
        user = str(user)
        caption = str(caption)
        ai.Bots.repost_users_images(user, caption, times)

    def unfollow_non_followers(self):
        ai.Bots.unfollow_non_followers()


    def __init__(self):
        # Get user info
        ai.bot.api.get_self_username_info()
        profilepic = ai.bot.api.last_json["user"]["profile_pic_url"]
        followers_count = ai.bot.api.last_json["user"]["follower_count"]
        following_count = ai.bot.api.last_json["user"]["following_count"]
        media_count = ai.bot.api.last_json["user"]["media_count"]
        print(media_count)
        the_proccess.write_file("profilepic", str(profilepic))
        the_proccess.write_file("followers_count", str(followers_count))
        the_proccess.write_file("following_count", str(following_count))
        the_proccess.write_file("media_count", str(media_count))
        self.procs = []
        def terminal():
            self.terminal = input("Which function do you want to use? \n\n 1) The first one. \n\n 2) The second one. \n\n 3) The first one and then the second one. \n\n Please enter the corresponding number and hit enter >>>>> ")

            if self.terminal == str(1):
                    thread1 = threading.Timer(1.0, self.follow_followers)
                    thread1.start()
                    terminal()

            if self.terminal == str(2):
                    thread2 = threading.Timer(1.0, self.follow_following)
                    thread2.start()
                    terminal()

            if self.terminal == str(3):
                    thread3 = threading.Timer(1.0, self.like_followers)
                    thread3.start()
                    terminal()

            if self.terminal == str(4):
                    thread4 = threading.Timer(1.0, self.like_following)
                    thread4.start()
                    terminal()

            if self.terminal == str(5):
                    thread5 = threading.Timer(1.0, self.like_hashtags)
                    thread5.start()
                    terminal()

            if self.terminal == str(6):
                    thread6 = threading.Timer(1.0, self.comment_hashtags)
                    thread6.start()
                    terminal()

            if self.terminal == str(7):
                    thread7 = threading.Timer(1.0, self.repost_images)
                    thread7.start()
                    terminal()

            if self.terminal == str(8):
                    thread8 = threading.Timer(1.0, self.unfollow_non_followers)
                    thread8.start()
                    terminal()

            if self.terminal == str(9):
                    thread9 = threading.Timer(1.0, self.watch_stories)
                    thread9.start()
                    terminal()



        terminal()
a = the_proccess();

# Login
#bot.login(username=args.u, password=args.p, proxy=args.proxy, use_cookie=True)
#ai.Bots.follow_users_hashtag_ai("fitness, programming", 45)
#ai.Bots.follow_users_following_ai(args.user, args.sleep)
#ai.Bots.follow_users_ai("japanheaven", 40)
#ai.Bots.user_hashtag_comment("fitness, models, friends", "wow please follow me back, wow nice profile, awesome profile", 40)
#ai.Bots.like_hashtags("model", 45)
#ai.Bots.repost_users_images("japanheaven, timferris, ariana, sjaaybee", "#models", 40)
