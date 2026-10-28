"""Build a feed for a community you choose.

See the course lab page for the demonstration checklist.
"""

from lab_classes import User, Tweet


def build_feed():
    # Create your accounts and posts, then call their methods.
    # Return the two lists: return users, posts
    bayern = User("Bayern Munich")
    halo = User("Halo Studios")

    post1 = Tweet(bayern.username, "Congrats to Harry Kane for winning the Ballon D'or")
    post2 = Tweet(halo.username, "Halo Studios will be not be developing the next Halo Game")
    post3 = Tweet(halo.username, "Activision will be developing the next Halo game :(")
    bayern.follow()
    bayern.follow()
    bayern.unfollow()
    halo.follow()

    # A post gets two likes, then one is removed.
    post1.like()
    post1.like()
    post1.unlike()
    post2.like()

    users = [bayern, halo]
    posts = [post1, post2, post3]

    return users, posts

    


def main():
    # Call build_feed and display the returned objects and hashtags.
    users, posts = build_feed()
    print('Accounts:')
    for user in users:
        print(user)
        print('Followers:', user.followers)

    print()
    print('Posts:')
    for post in posts:
        print(post)
        print('Likes:', post.likes)
        print('Hashtags:', post.hashtags())
        print()


if __name__ == '__main__':
    main()
