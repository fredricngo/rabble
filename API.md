#RABBLE API DOCUMENTATION 

## POST: /api/subrabbles/!cs-courses/posts
Create a new post in the cs-courses subRabble

```json
{
        "post_title": "chicken jockey",
        "post_body": "CHICKEN JOCKEY",
        "comment_count": 0,
        "author": 8,
        "like_count": 0,
        "timestamp": "2025-04-21T17:54:05.213000Z",
        "is_anon": false,
        "subrabble_id": 1,
        "reactions": []
    }


## PATCH: /api/subrabbles/!<str:identifier>/posts/<int:pk>
Edit an existing post in the cs-courses subRabble 

```json

{
    "post_title": "No, you're NOT a gamer",
    "post_body": "No, you’re NOT a real gamer. I’m so sick of all these people that tho k they’re gamers. No, you’re not. Most of you are not even close to being gamers.",
    "comment_count": 0,
    "author": 8,
    "like_count": 0,
    "timestamp": "2025-04-21T17:52:00.287000Z",
    "is_anon": false,
    "subrabble_id": 1,
    "reactions": []
}
