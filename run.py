import praw
from time import sleep


client_id = 'XXXX'
client_secret = 'XXXX'
reddit_user = 'XXXX'
reddit_pass = 'XXXX'
user_agent = 'Downvoted comment editor (by /u/impshum)'

test_mode = 1
loop = 1
limit = 100
downvotes = 0
sleep_timer = 86400
verbose = 1
edits = "**/s**"

reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     user_agent=user_agent,
                     username=reddit_user,
                     password=reddit_pass)
x = 1
c = 0
while x:
    for comment in reddit.redditor(reddit_user).comments.new(limit=limit):
        if not comment.saved and comment.downs > 0:
            if verbose:
                print('{}: https://reddit.com{}'.format(comment.downs, comment.permalink))
            if not test_mode:
                new = '{} {}'.format(comment.body, edits)
                comment.edit(new)
                comment.save()
                c += 1
    print(f'Edited {c} comments')
    if not loop:
        x = 0
    else:
        print('Sleeping')
        sleep(sleep_timer)
