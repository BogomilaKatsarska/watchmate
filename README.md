1. Admin Access http://127.0.0.1:8000/dashboard/

2. Accounts
  Registration: http://127.0.0.1:8000/api/account/register/
  Login: http://127.0.0.1:8000/api/account/login/
  Logout: http://127.0.0.1:8000/api/account/logout/

3. Stream Platforms(like Netflix)
  Create Element & Access List: http://127.0.0.1:8000/api/watch/stream/
  Access, Update & Destroy Individual Element: http://127.0.0.1:8000/api/watch/stream/<int:streamplatform_id>/

4. Watch List(like movies, TV series, etc.
  Create & Access List: http://127.0.0.1:8000/api/watch/
  Access, Update & Destroy Individual Element: http://127.0.0.1:8000/api/watch/<int:movie_id>/

5. Reviews(each user can post only one review per movie
  Create Review For Specific Movie: http://127.0.0.1:8000/api/watch/<int:movie_id>/reviews/create/
  List Of All Reviews For Specific Movie: http://127.0.0.1:8000/api/watch/<int:movie_id>/reviews/
  Access, Update & Destroy Individual Review: http://127.0.0.1:8000/api/watch/reviews/<int:review_id>/

6. User Review
  Access All Reviews For Specific User: http://127.0.0.1:8000/api/watch/user-reviews/?username=example


NOTE: First you need to create admin - he/she has rights to create stream platform.
      Then create some movies - their models depend on the stream platforms.
      Then, you can create other users - then review section can be tested.
