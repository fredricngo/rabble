#Table: 'Users'

Columns

'User_id' (autoincrementing integer)
'Username' (string)
'First_Name' (string)
'Last_Name' (string)
'E-mail' (string)
'Biography' (string)
'Profile_Picture' (string)
'Interests' (string)
Constraints

Unique: ('Username')
#Table: 'Privilege'

Columns
'Privilege_id' (autoincrementing integer)
'privilege_type' (string)
#Table: 'Community

Columns

'Community_id' (autoincrementing integer)
'Community_name' (string)
Constraints

Unique: ('Community_name')
#Table: 'subRabble'

Columns

'subRabble_id' (autoincrementing integer)
'Community_id' (integer)
'subRabble_name' (string)
'Description' (string)
'Is_private' (boolean)
Constraints

Unique: ('subRabble_name', 'Community_id')
Foreign Key: 'Community_id' refers to community.community_id
#Table: 'Post'

Columns

'Post_id' (autoincrementing integer)
'Title' (string)
'Body' (string)
'Comment_count' (integer)
'subRabble_id' (integer)
'User_id' (integer)
'Poster_username' (string)
'Like_count' (integer)
'Timestamp' (string)
'Is_anonymous' (boolean)
Constraints - Foreign Key: 'subRabble_id' refers to subRabble.subRabble_id

Foreign key: 'user_id' refers to user.user_id
#Table: 'Reactions'

Columns:

'Reaction_id' (autoincrementing integer)
'Reaction_type' (string)
'User_id' (integer)
'Post_id' (integer)
'Username'(string)
'Timestamp' (string)
Constraints:

Foreign key: 'user_id' refers to user.user_id
Foreign key: 'post_id' refers to post.post_id
#Table: 'Comments'

Columns:
'Comment_id' (autoincrementing integer)
'Post_id' (integer)
'User_id' (integer)
'Body' (string)
'Username' (string)
'Like_Count' (integer)
'Comment_Count' (integer)
'Timestamp' (string)
'Is_anonymous' (boolean)
Constraints:
Foreign key: 'post_id' refers to post.post_id
Foreign key: 'user_id' refers to user.user_id
#Table: 'Conversations'

Columns:

'Title' (string)
'Conversation_id' (autoincrementing integer)
'Community_id' (integer)
Constraints:

Foreign key: 'community_id' refers to community.community_id
#Table: 'Messages'

Columns:

'Timestamp' (string)
'Body' (string)
'Sender' (username)
'User_id' (integer)
'Conversation_id' (integer)
'Message_id' (autoincrementing integer)
Constraints:

Foreign key: 'user_id' refers to user.user_id
Foreign key: 'conversation_id' refers to conversation.conversation_id
#Table: 'Invitations'

Columns:

'Invitation_id' (autoincrementing integer)
'Invitation Type' (string)
'Sender_Username' (string)
'User_id' (integer)
'Receiver_Email' (string)
'Community/subRabble_identifier' (string)
'Status' (string)
Constraints:

Foreign key: 'User_id' refers to user.user_id
#Table: 'Community Membership'

Columns:

'User_id' (integer)
'Community_id' (integer)
Constraints:

Foreign key: 'User_id' refers to user.user_id
Foreign key: 'Community_id' refers to community.community_id
#Table: 'Conversation Membership'

Columns:

'User_id' (integer)
'Conversation_id' (integer)
Constraints:

Foreign key: 'User_id' refers to user.user_id
Foreign key: 'conversation_id' refers to conversation.conversation_id
#Table: 'User Privilege Log'

Columns:

'User_id' (integer)
'Community_id' (integer)
'Privilege_id' (integer)
Constraints:

Foreign key: 'User_id' refers to user.user_id
Foreign key: 'community_id' refers to community.community_id
Foreign key: 'privilege_id' refers to privilege.privilege_id
#Table: 'Follow Log'

Columns:

'Followed' (integer)
'Following' (integer)
Constraints: Foreign key: 'followed' refers to user.user_id Foreign key: 'following' refers to user.user_id

#Table: 'Comment Thread'

Columns:

'Original' (integer)
'Reply' (integer)
Constraints:

Foreign key: 'original' refers to comment.comment_id
Foreign key: 'reply' refers to comment.comment_id
#Table: 'SubRabble Membership'

Columns:

'User_id' (integer)
'subRabble_id' (integer)
Constraints: Foreign key: 'user_id' refers to user.user_id Foreign key: 'following' refers to user.user_id