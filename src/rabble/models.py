from django.db import models
from django.contrib.auth.models import AbstractUser

#To Implement: 
#1. User model -- DONE
#2. Community -- DONE
#3. SubRabble -- DONE
#4. Post -- DONE
#5. Reaction -- DONE 
#6. Comment -- DONE
#7. Privilege (through model) -- DONE
#8. Conversation -- DONE
#9. Messages -- DONE
#10.Invitation -- DONE
#11.Community Membership (through model) -- DONE
#13. User Privilege Log (through model) -- DONE
#14. Follow Log (through model) -- DONE
#15. Comment Thread (through model) -- DONE
#16. SubRabble Membership (through model) -- DONE

#check for remaining relationships

class User(AbstractUser):
    #User has already inherited the following classes from AbstractUser:
        #1. username 
        #2. first_name
        #3. last_name 
        #4. email

    #also opting to use CharFields instead of TextFields in order to limit lenght of the fields
    biography = models.CharField(max_length=255, blank=True)
    profile_picture = models.ImageField(upload_to="profile_pictures", blank=True)
    interests = models.CharField(max_length=255, blank=True)
# Create your models here.

class Community(models.Model):
    #didn't add a primary key, Django will automatically add an auto-incrementing primary key field called id
    community_name = models.CharField(max_length=255, unique=True)


class SubRabble(models.Model):
    #no primary key, Django will automatically add an auto-incrementing primary key field called id
    subrabble_name = models.CharField(max_length=255, unique=True)
    community_id = models.ForeignKey(Community, on_delete=models.CASCADE) 
    #if we delete a community, all the sub-rabbles associated with it will also be deleted
    description = models.TextField(blank=True)
    is_private = models.BooleanField(default=False)

class Post(models.Model):
    post_title = models.CharField(max_length=255) 
    post_body = models.TextField()
    comment_count = models.PositiveIntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    like_count = models.PositiveIntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_anon = models.BooleanField(default=False)
    subrabble_id = models.ForeignKey(SubRabble, on_delete=models.CASCADE)

    #Relationship: A post has many reactions 
    reactions = models.ManyToManyField(User, through='Reaction', related_name='reactions')

class Reaction(models.Model):
    class ReactionType(models.TextChoices):
        LIKE = "Like"
        #add more reaction types as needed

    reaction_type = models.CharField(max_length=10, choices=ReactionType.choices)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Foreign key to User
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  # Foreign key to Post
    username = models.CharField(max_length=255)  # Store username for quick access
    timestamp = models.DateTimeField(auto_now_add=True)  # Automatically set timestamp on creation

    def __str__(self):
        return f"{self.username} reacted {self.reaction_type} to Post {self.post.id}"
    
    class Meta: 
        unique_together = ("user", "post", "reaction_type")


class Privilege(models.Model):
    #through table for community membership
    #privilege id is automatically created by Django
    #we want to express the following privileges a user can have: 
    #1. owner
    #2. admin
    #3. member
    #4. banned 
    class PrivilegeType(models.TextChoices):
        OWNER = "Owner"
        ADMIN = "Admin"
        MEMBER = "Member"
        BANNED = "Banned"

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    community_id = models.ForeignKey(Community, on_delete=models.CASCADE)
    privilege_type = models.CharField(max_length=10, choices=PrivilegeType.choices)

    class Meta: 
        unique_together = ("user_id", "community_id")



class Comment(models.Model):
    body = models.TextField()
    publisher = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,)
    username = models.CharField(max_length=255)  # Store username for quick access
    like_count = models.PositiveIntegerField(default=0)
    comment_count = models.PositiveIntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)  # Automatically set timestamp on creation
    is_anon = models.BooleanField(default=False)

    def __str__(self):
        return f"Comment by {self.username} on Post {self.post.id}"
    

class CommentThread(models.Model):
    original = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='original_comment')
    reply = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='reply_comment')

    def __str__(self):
        return f"Reply {self.reply.id} to Comment {self.original.id}"
    

class Conversation(models.Model): 
    title = models.CharField(max_length=255)
    community = models.ForeignKey(Community, on_delete=models.CASCADE)

    def __str__(self):
        return f"Conversation {self.title} in Community {self.community.community_name}"
    

class ConversationMembership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    
    class Meta: 
        unique_together = ("user", "conversation")

    def __str__(self):
        return f"{self.user.username} is a member of Conversation {self.conversation.title}"
    

class Message(models.Model):
    body = models.TextField()
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender.username} in Conversation {self.conversation.title}"


class Invitation(models.Model): 
    class InvitationType(models.TextChoices): 
        COMMUNITY = "Community"
        CONVERSATION = "SubRabble"

    class StatusType(models.TextChoices): 
        PENDING = "Pending"
        ACCEPTED = "Accepted"
        DECLINED = "Declined"
    
    invitation_type = models.CharField(max_length=20, choices=InvitationType.choices)
    sender =  models.ForeignKey(User,on_delete=models.CASCADE, related_name="received_invitations")
    receiver = models.EmailField()
    identifier = models.CharField(max_length=255)  # Could be community name or conversation title
    status = models.CharField(max_length=20, choices=StatusType.choices, default=StatusType.PENDING)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Invitation from {self.sender.username} to {self.receiver} for {self.identifier} ({self.invitation_type})"
    

class CommunityMembership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="conv")
    community = models.ForeignKey(Community, on_delete=models.CASCADE, related_name="conv")

    def __str__(self):
        return f"{self.user.username} is a member of Community {self.community.community_name}"


class UserPrivilegeLog(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    community = models.ForeignKey(Community, on_delete=models.CASCADE)
    privilege = models.ForeignKey(Privilege, on_delete=models.CASCADE)


class FollowLog(models.Model): 
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="follower")
    followed = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followed")

    def __str__(self):
        return f"{self.follower.username} follows {self.followed.username}"
    
class CommentThread(models.Model):
    original = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='original_comment')
    reply = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='reply_comment')

    def __str__(self):
        return f"Reply {self.reply.id} to Comment {self.original.id}"

class SubRabbleMembership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subrabble = models.ForeignKey(SubRabble, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} is a member of SubRabble {self.subrabble.subrabble_name}"