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


HOMEWORK #3; 
- Asked general questions about Django concepts: 
    - How tos how one page over another if the user is authenticated? 
    - howt o properly implement user authentication checks in views? 
    - How to redirect unauthenticated users? 
    - How to create and check objects using Django shell 
    - Understanding how to check if a user is the author of a post
    - HOw to do conditional rendering

HOMEWORK #4: 
I implemented the first two endpoints (without the generic views) without assistance
from AI, then asked CoPilot for some help on what views I should use when implementing 
the last two endpoints.

HOMEWORK #5:
I generally followed the course Registrar example code for creating factories and tests, but consulted AI for specific implementation details:
 - Where to properly place the `force_login` details to support the extra authentication tasks I implemented in HW #3
- Debugging issues with accessing and asserting IDs due to how my serializers were defined
-  Specifying the correct arguments for the `reverse()` function, specifically for calls like `response = client.get(reverse("subrabble-detail", args=[subrabble.subrabble_name]))`
Generally, I used it to  help troubleshoot specific implementation issues and understand Django testing concepts better.

