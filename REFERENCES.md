HOMEWORK #1: 
Used Github CoPilot for general reference purposes (i.e, how to display a certain page depending on whether a user is logged in or not)


HOMEWORK #2: 

1. Models wrote manually:
    - User
    - Community 
    - SubRabble 
    - Post 
    - Reaction
    - Privilege
    - CommunityMembership
    - UserPrivilegeLog
 

2. Models generated with GenAI + Descriptions of Adjustments Made: 
    - Comment 
    - Conversation 
    - Messages 
    - Invitation 
    - FollowLog
    - CommentThread
    - SubRabble Membership


While crafting the Comment model, CoPilot made the suggestion of using CharField (and after looking into the documentation I found it was also a useful change) instead of TextField since CharField can set a limit on length of the entry, I then changed other models I had implemented to also use CharField. 

CoPilot also would often make the suggestion to use "related_name" which I did not know about before, but now understand is an extremely useful tool for code readability and for when dealing with foreign keys in a model that reference the same model: 

E.g, 
--models.py, line 189--
class FollowLog(models.Model): 
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="follower")
    followed = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followed")

    def __str__(self):
        return f"{self.follower.username} follows {self.followed.username}"

without the related_name parameters, Django wouldn't know how to differentiate between follower and followed. 

I also asked CoPilot to explain the steps I should take to register my models so that they show up on the admin site. 