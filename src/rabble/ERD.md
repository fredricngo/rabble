Entities
User
Attributes:

Username (string)
First Name (string)
Last Name (string)
E-mail (string)
Bio (string)
Profile Picture (string)
Interests (string)
Community
Attributes:

Community identifier (string)
SubRabble
Attributes:

subRabble identifier (string)
Description (string)
Is Private (boolean)
Post
Attributes:

Title (string)
Body (string)
Comment Count (integer)
Publisher’s Username (string)
Like Count (integer)
Timestamp (string)
Is anonymous (boolean)
Reaction
Attributes:

Reaction Type (string)
Username of User Reacting (string)
Timestamp (string)
Comment
Attributes:

Body (string)
Publisher’s Username (string)
Like Count (integer)
Timestamp (string)
Is Anonymous (boolean)
Privilege
Attributes:

Privilege Type (string, one of "owner", "admin", or "member)
Conversation
Attributes:

Title (string)
Message
Attributes:

Timestamp (string)
Body (string)
Sender (string)
Invitation
Attributes:

Invitation Type (string)
Sender’s Username (string)
Receiver’s Email (string)
Status (string)
Relationships
User and Community
Users (N) belongs to communities (M)
Community and subRabble
A community (1) has subRabbles (N)
SubRabble and Post
A subRabble (1) has posts (N)
Post and Comment
A post (1) has comments (N)
Post and Reaction
A post (1) has reactions (N)
User and Reaction
A user (1) has reactions (N)
User and Comment
A user (1) makes comments (N)
User and Invitation
A user (1) receives invitations (N)
User and Message
A user (1) has messages (N)
User and Conversation
Users (N) have conversations (M)
User and Privileges
users (N) have privileges (N)
Conversation and Message
A conversation (1) has messages (N)
Community and Conversation
A community (1) has conversations (N)
User and User
Users (N) follow users (M)
Comment and Comment
Comments (N) have comments (M)
User and SubRabble
Users (N) belong to Subrabbles (M)
User and Post
A user (1) makes posts (N)