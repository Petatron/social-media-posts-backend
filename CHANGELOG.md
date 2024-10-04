### [PETA-100-Set-up-Postgres-in-local](https://github.com/Petatron/social-media-posts-backend/tree/PETA-100-Set-up-Postgres-in-local)

- Created Docker file to automate the creation of the user and database permissions. The `setup.sql` is to grant access to our database to the new user in DB.
- Created `Makefile` to store Docker installation and other used commands.

### [PETA-104-Set-up-Github-CI-actions](https://github.com/Petatron/social-media-posts-backend/tree/PETA-104-Set-up-Github-CI-actions)

- Created Django GitHub workflow.
- Update `Makefile` to quick generate project environment.

### [PETA-101-Create-User-and-Superuser](https://github.com/Petatron/social-media-posts-backend/tree/PETA-101-Create-User-and-Superuser)

- Created `User` model that contains `UserManager`

### [PETA-102-Create-UserSerializer-and-UserViewset](https://github.com/Petatron/social-media-posts-backend/tree/PETA-102-Create-UserSerializer-and-UserViewset)

- Fix the UserSerializer fields issue that inside class UserSerializer.
- Created `UserSerializer` and `UserViewser` in User.
- Added user into routes.

### [PETA-103-Create-User-Registration-Feature](https://github.com/Petatron/social-media-posts-backend/tree/PETA-103-Create-User-Registration-Feature)

- Created `class RegisterViewSet` inside core/auth/viewset by using `djangorestframework-simplejwt` to implement JWT authentication.
- Add JWT auth URL into routes and fixed the URL issue.

### [PETA-105-Implement-user-login-and-refresh-features](https://github.com/Petatron/social-media-posts-backend/tree/PETA-105-Implement-user-login-and-refresh-features)

- Implement user login feature
- Implement refresh login token feature

### [PETA-106 create post model](https://github.com/Petatron/social-media-posts-backend/pull/10) and abstract class

- Create Abstract package
- Update user package to utilize abstract class

### [PETA-112 implement post model](https://github.com/Petatron/social-media-posts-backend/pull/12)

- Updated User table structure to fix the database table issue. Added `bio` and `avatar` filed to the database table.
- Created migrations for the Post model.
- Implement the Post model.

### [PETA-113 added post serializer](https://github.com/Petatron/social-media-posts-backend/pull/13)

### [PETA-115 implement post viewsets](https://github.com/Petatron/social-media-posts-backend/pull/15)

- Created Post viewsets.
- Fixed API authorization issue by adding `JWTAuthentication` into PostViewsets
- Added default page number

### [PETA-118-Create-permission-for-POST](https://github.com/Petatron/social-media-posts-backend/pull/16)

- Added user permission for send a post.
- The anonymous user: This user has no account on the API and can’t really be identified.
- The registered and active user: This user has an account on the API and can easily perform some actions.
- The admin user: This user has all rights and privileges.

### [PETA-117 added to_representation](https://github.com/Petatron/social-media-posts-backend/pull/17)

- Added method to show user details in API

### [PETA-108 create delete and update features](https://github.com/Petatron/social-media-posts-backend/pull/18)

- Added update and delete post method into API

### [PETA-109 Implement create like/unlike feature](https://github.com/Petatron/social-media-posts-backend/pull/21)

- [Adding the posts_liked field to the User model](https://www.educative.io/courses/full-stack-django-and-react/adding-the-like-feature#Adding-the-postsliked-field-to-the-User-model)
- [Adding the like, remove_like, and has_liked methods](https://www.educative.io/courses/full-stack-django-and-react/adding-the-like-feature#Adding-the-like-removelike-and-hasliked-methods)
- [Adding the likes_count and has_liked fields to PostSerializer](https://www.educative.io/courses/full-stack-django-and-react/adding-the-like-feature#Adding-the-likescount-and-hasliked-fields-to-PostSerializer)
- [Adding like and remove like actions to PostViewSet](https://www.educative.io/courses/full-stack-django-and-react/adding-the-like-feature#Adding-like-and-remove-like-actions-to-PostViewSet)

### [PETA-110 Implement create comment feature](https://github.com/Petatron/social-media-posts-backend/pull/22)
- Create comment models