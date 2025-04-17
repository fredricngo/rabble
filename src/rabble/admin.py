from django.contrib import admin
from .models import User, Community, SubRabble, Post, Reaction, Comment, CommentThread, Conversation, ConversationMembership, Message, Invitation, CommunityMembership, UserPrivilegeLog, FollowLog, SubRabbleMembership
# Register your models here.
admin.site.register(User)
admin.site.register(Community)
admin.site.register(SubRabble)
admin.site.register(Post)
admin.site.register(Reaction)
admin.site.register(Comment)
admin.site.register(CommentThread)
admin.site.register(Conversation)
admin.site.register(ConversationMembership)
admin.site.register(Message)
admin.site.register(Invitation)
admin.site.register(CommunityMembership)
admin.site.register(UserPrivilegeLog)
admin.site.register(FollowLog)
admin.site.register(SubRabbleMembership)