DataBase Schema

1. User
-   Using the existing build-in Django User Model

2. Post 
-   title
-   text
-   author : References User, ON DELETE CASCADE
-   created_at : DateTime, auto_now_add is True
-   votes : Integer, Default = 0

2. Comment 
-   text
-   author : References User, ON DELETE CASCADE
-   created_at : DateTime, auto_now_add is True
-   post : References Post, ON DELETE CASCADE