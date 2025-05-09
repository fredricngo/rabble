# RESUBMISSION.md

## Special Circumstances 

I completed both Homework #2 and Homework #3 before their respective deadlines and pushed all completed work to my Github repository on time. However, I failed to submit the assignments through Gradescope. I can provide Github timestamps as evidence of on-time completion if needed.

## Important Notes for Graders

- Graders need to run `python3 manage.py loaddata rabble-fixture.json` even if only grading HW #2 and HW #3
- All posts in my rabble setup are authored by sam

## Resubmission for Homework #2

Since I did not submit HW #2 through Gradescope, I did not receive any feedback or rubric items. I am resubmitting the complete assignment with all requirements implemented. The code implements all functionality required for HW #2 including:

- Implementation of Django models corresponding to the data design from Project Warm-up #1
- Proper implementation of the User model by adding fields to the existing User class
- Creation of correct migrations for all models
- Proper implementation of model relationships (one-to-many, many-to-many)
- Additionally, I completed the extra task of enabling all models in Django's admin interface by registering them in admin.py

## Resubmission for Homework #3

Since I did not submit HW #3 through Gradescope, I did not receive any feedback or rubric items. I am resubmitting the complete assignment with all requirements implemented. The code implements all functionality required for HW #3 including:

- Creation of a `rabble-fixture.json` file with the required test data:
  - Five users (sam, alex, chris, morgan, and drew) with password "test"
  - One community with identifier "default" and sam as owner/admin
  - Three subRabbles (cs-courses, python, and web-dev)
  - Three posts in cs-courses with at least one authored by alex
  - At least one post with three or more comments

- Implementation of all required views:
  - SubRabbles List View - Updated the index view to display all subRabbles
  - SubRabble Detail View - Shows a single subRabble with its list of posts
  - Post Detail View - Shows a single post with its comments
  - Post Create/Edit Views - Forms for creating and editing posts

- Implementation of all required URL patterns:
  - / - Index page with list of subRabbles
  -/!<subRabble-identifier>/ - subRabble detail page
  - /!<subRabble-identifier>/<post-id>/ - Post detail page
  - /!<subRabble-identifier>/new - Post creation page
  - /!<subRabble-identifier>/<post-id>/edit - Post edit page

* Creation of forms for post creation and editing in forms.py

Additionally, I implemented the extra task to limit actions by user:
- Anonymous users can only see the index page with a login message
- Logged-in users can see all content and create posts
- Only the author of a post can edit it, and only they see the Edit post button

I sincerely apologize for the submission error and thank you for considering my resubmission. The work was completed on time, and I am now ensuring it is properly submitted through the resubmission process.