## MEDIUM CLONE USING DJANGO 4 - LAST TRAIL

## 1. SETUP THE PROJECT

#### 1. Create project

        modified:   README.md
        new file:   config/__init__.py
        new file:   config/asgi.py
        new file:   config/settings.py
        new file:   config/urls.py
        new file:   config/wsgi.py
        new file:   manage.py

#### 2. Create blog app

        modified:   README.md
        new file:   apps/blog/__init__.py
        new file:   apps/blog/admin.py
        new file:   apps/blog/apps.py
        new file:   apps/blog/migrations/__init__.py
        new file:   apps/blog/models.py
        new file:   apps/blog/tests.py
        new file:   apps/blog/views.py

#### 3. Register the blog app to the project

        modified:   README.md
        modified:   config/settings.py        

        # Note: error

        ModuleNotFoundError: No module named 'blog'

#### 4. Create path for the apps

        modified:   README.md
        modified:   config/settings.py

        :)

#### 5. Hello World!

        modified:   README.md
        new file:   apps/blog/urls.py
        modified:   apps/blog/views.py
        modified:   config/settings.py
        modified:   config/urls.py
        new file:   templates/blog/index.html

#### 6. Add html template, add path and load static files

        modified:   config/settings.py
        new file:   static/css/bootstrap.min.css
        new file:   static/css/bootstrap.min.css.map
        new file:   static/css/style.css
        new file:   static/css/tagify.css
        new file:   static/js/bootstrap.bundle.min.js
        new file:   static/js/bootstrap.bundle.min.js.map
        new file:   static/js/tagify.js
        new file:   static/js/tagify.polyfills.min.js
        new file:   static/js/tinymce.min.js
        modified:   templates/blog/index.html

#### 7. Template inheritance

        modified:   README.md
        new file:   templates/blog/components/hero.html
        new file:   templates/blog/components/posts_latest.html
        new file:   templates/blog/components/posts_trend.html
        modified:   templates/blog/index.html
        new file:   templates/inc/navbar.html

#### 8. Base template

        modified:   README.md
        new file:   templates/base.html
        modified:   templates/blog/index.html

#### 9. Dynamic page title with block super

        modified:   README.md
        modified:   templates/base.html
        modified:   templates/blog/index.html

## 2. USER MANAGEMENT

#### 1. Create account app and register it to the project

        modified:   README.md
        new file:   apps/account/__init__.py
        new file:   apps/account/admin.py
        new file:   apps/account/apps.py
        new file:   apps/account/migrations/__init__.py
        new file:   apps/account/models.py
        new file:   apps/account/tests.py
        new file:   apps/account/views.py
        modified:   config/settings.py

#### 2. Login - part 1: Create views, urls, templates

        modified:   README.md
        new file:   apps/account/urls.py
        modified:   apps/account/views.py
        modified:   config/urls.py
        new file:   templates/account/login.html
        new file:   templates/blog/account/login.html
        modified:   templates/inc/navbar.html

#### 3. Login - part 2: Add logic to login_view and log the user in

        modified:   README.md
        modified:   apps/account/views.py
        modified:   templates/account/login.html

        Note:

        1. User successfully logged in.

        But no message to inform the user.

        :)?

#### 4. Login - part 3: Add django messages

        modified:   README.md
        modified:   templates/base.html
        new file:   templates/inc/messages.html

        :)

#### 5. Login - part 4: Add conditional to navbar to show/hide menus

        modified:   README.md
        modified:   templates/inc/navbar.html

        :)

#### 6. Logout

        modified:   README.md
        modified:   apps/account/urls.py
        modified:   apps/account/views.py
        modified:   templates/inc/navbar.html

        :)

#### 7. Register - part 1: Create Profile model

        modified:   README.md
        modified:   apps/account/admin.py
        new file:   apps/account/migrations/0001_initial.py
        modified:   apps/account/models.py

#### 8. Register - part 2: Create views, ulrs, templates, and links

        modified:   README.md
        modified:   apps/account/urls.py
        modified:   apps/account/views.py
        new file:   templates/account/register.html
        modified:   templates/inc/navbar.html

#### 9. Register - part 3: Add logic to register_view 

        modified:   README.md
        modified:   apps/account/views.py

        Note:

        1. Successfully register new user.
        2. User profile also created automatically.
        3. But no avatar.

        :)

#### 10. Register - part 4: Create path for media files

        modified:   README.md
        modified:   apps/account/views.py
        modified:   config/settings.py
        modified:   config/urls.py

## 3. BLOG POSTS MANAGEMENT

#### 1. CREATE blog post - part 1: Create models: Abstract, Category, Tag, and BlogPost

        modified:   README.md
        modified:   apps/blog/admin.py
        new file:   apps/blog/migrations/0001_initial.py
        modified:   apps/blog/models.py
        modified:   config/settings.py

#### 2. CREATE blog post - part 2: Create BlogPostModelForm model forms

        modified:   README.md
        new file:   apps/blog/forms.py

#### 3. CREATE blog post - part 3: Create views, urls, templates

        modified:   README.md
        modified:   apps/blog/urls.py
        modified:   apps/blog/views.py
        deleted:    templates/blog/account/login.html
        new file:   templates/blog/create_blog_post.html
        modified:   templates/inc/navbar.html

#### 4. CREATE blog post - part 4: Fetch BlogPostModelForm instances to template from create_blog_post_view 

        modified:   README.md
        modified:   apps/blog/views.py
        modified:   templates/blog/create_blog_post.html

#### 5. CREATE blog post - part 5: Adding class attributes to BlogPostModelForm

        modified:   README.md
        modified:   apps/blog/forms.py
        modified:   templates/blog/create_blog_post.html

#### 6. CREATE blog post - part 6: Styling the form using crispy bootstrap5
 
        modified:   apps/blog/forms.py
        modified:   config/settings.py
        modified:   templates/blog/create_blog_post.html

#### 7. CREATE blog post - part 7: Modified BlogPostModelForm and use TinyMCE widget for form content

        modified:   apps/blog/forms.py
        modified:   templates/blog/create_blog_post.html

        Note:

        1. TinyMCE does not work in Edge browser.
        1. It works in Chome and Mozzilla

#### 7. CREATE blog post - part 7: Add logic to create_blog_post_view

        modified:   README.md
        modified:   apps/account/migrations/0001_initial.py
        modified:   apps/blog/migrations/0001_initial.py
        modified:   apps/blog/views.py
        modified:   config/settings.py
        new file:   media/post/car.PNG
        new file:   media/post/car_2E77E2U.PNG
        new file:   media/post/car_IICQLZ1.PNG
        new file:   media/post/car_ORDHHsG.PNG
        new file:   media/post/car_gM14JGy.PNG
        new file:   media/post/car_pBDHz1u.PNG
        modified:   templates/blog/create_blog_post.html

        Note:

        1. Blog post created.
        2. Tag created.
        3. Can add >1 tag.
        4. But tag is not active by default.
        5. If changed image, old image does not remove.

        :)?

#### 8. READ blog post - part 1: Read and show all posts to index page

        modified:   README.md
        modified:   apps/blog/views.py
        modified:   config/settings.py
        new file:   media/post/banner01.jpg
        new file:   media/post/banner02.jpg
        new file:   media/post/banner02.jpg.400x300_q85_crop.jpg
        new file:   media/post/car_pBDHz1u.PNG.400x300_q85_crop.png
        modified:   templates/blog/components/posts_latest.html

        Note:

        1. Thumbnail not show up.
        2. User image (how to show it)?

        :)?

#### 9. READ blog post - part 2: Read and show all categories and tags to index page

        modified:   README.md
        modified:   apps/blog/models.py
        modified:   apps/blog/views.py
        modified:   templates/blog/components/posts_latest.html

#### 10. READ blog posts by user- part 3: Define views, urls, templates

        modified:   README.md
        modified:   apps/blog/urls.py
        modified:   apps/blog/views.py
        new file:   templates/blog/posts_by_user.html

#### 11. READ blog posts by user- part 4: Show all posts by a user

        modified:   README.md
        modified:   apps/account/models.py
        modified:   apps/blog/views.py
        new file:   media/avatar/darling2.PNG
        new file:   media/avatar/ing.jpeg
        modified:   templates/blog/components/posts_latest.html
        modified:   templates/blog/posts_by_user.html

        Note:

        1. It works: show all posts by a user.

        :)

#### 12. READ detail blog posts - part 5: Show post detail 

        modified:   apps/blog/models.py
        modified:   apps/blog/urls.py
        modified:   apps/blog/views.py
        modified:   config/settings.py
        new file:   media/post/banner02.jpg.1000x300_q85_crop.jpg
        new file:   media/post/banner03.jpg
        new file:   media/post/banner03.jpg.1000x300_q85_crop.jpg
        new file:   media/post/banner03.jpg.400x300_q85_crop.jpg
        new file:   media/post/car_pBDHz1u.PNG.1000x300_q85_crop.png
        modified:   templates/blog/components/posts_latest.html
        new file:   templates/blog/post_detail.html

        :)

#### 13. READ blog posts by category - part 6: Show all posts by a category

        modified:   README.md
        modified:   apps/blog/admin.py
        modified:   apps/blog/models.py
        modified:   apps/blog/urls.py
        modified:   apps/blog/views.py
        modified:   templates/blog/components/posts_latest.html
        modified:   templates/blog/post_detail.html
        new file:   templates/blog/posts_by_category.html
        modified:   templates/blog/posts_by_user.html

        :)

#### 14. READ blog posts by tag - part 6: Show all posts by a tag

        modified:   README.md
        modified:   apps/blog/models.py
        modified:   apps/blog/urls.py
        modified:   apps/blog/views.py
        modified:   templates/blog/components/posts_latest.html
        new file:   templates/blog/posts_by_tag.html

        :)

#### 15. VIEWED-COUNT blog posts - part 1: Counting the viewed blog post 

        modified:   README.md
        modified:   apps/blog/views.py
        modified:   templates/blog/components/posts_latest.html

        :)

#### 16. EDIT profile - part 1: Create ProfileModelForm

        modified:   README.md
        new file:   apps/account/forms.py

#### 17. EDIT profile - part 2: Create views, urls, templates and logic

        new file:   apps/account/migrations/0002_profile_info.py
        modified:   apps/account/models.py
        modified:   apps/account/urls.py
        modified:   apps/account/views.py
        new file:   apps/blog/migrations/0002_alter_blogpost_options_alter_category_options_and_more.py
        new file:   media/avatar/darling2_m2yCYDN.PNG
        new file:   templates/account/profile_edit.html
        modified:   templates/inc/navbar.html

        :)

#### 18. EDIT profile - part 3: Define get_all_posts_url and get_profile_edit_url and modified navbar

        modified:   apps/account/models.py
        modified:   templates/inc/navbar.html

        Note: Links works.

        :)

#### 19. TRENDING POSTS - Show all trending posts

        modified:   README.md
        modified:   apps/blog/views.py
        new file:   media/avatar/darling2_m2yCYDN.PNG.30x30_q85_crop.png
        new file:   media/avatar/ing.jpeg.30x30_q85_crop.jpg
        modified:   templates/blog/components/posts_trend.html
        new file:   templates/blog/components/posts_trend_component.html

        :) :) :)

#### 20. FAV POSTS - Add fav posts and show all fav posts

        modified:   README.md

        # Step 1: Create UserPostFav model, run migration, and register to admin
        modified:   apps/blog/models.py
        new file:   apps/blog/migrations/0003_userpostfav.py
        modified:   apps/blog/admin.py

        # Step 2: Create fav_update, include it in index.html, add block script to base template, and static file
        new file:   templates/inc/fav_update.html
        modified:   templates/blog/index.html
        modified:   templates/base.html
        new file:   static/js/axios.min.js

        # Step 3: Create views, urls, templates, link
        modified:   apps/blog/urls.py
        modified:   apps/blog/views.py
        new file:   templates/blog/posts_fav.html
        new file:   templates/blog/components/posts_fav_component.html
        modified:   templates/inc/navbar.html

        # Step 4: Create user_fav_view, url, get_fav_url
        modified:   apps/account/models.py
        modified:   apps/account/urls.py
        modified:   apps/account/views.py
        
        # Step 5: if user.is_authenticated load post.slug
        modified:   templates/blog/components/posts_latest.html


        Note: IT WORKS AT LAST!

        1. To add fav post: logged in + click the icon.
        2. To check my fav posts: click dropdown navbar + cliv menu Favs

        :)

#### 21. UPDATE Blog Post - Update a blog post 

        modified:   README.md
        modified:   apps/blog/models.py
        modified:   apps/blog/urls.py
        modified:   apps/blog/views.py
        new file:   media/post/banner02_nZjpk0S.jpg
        new file:   media/post/banner02_nZjpk0S.jpg.1000x300_q85_crop.jpg
        new file:   media/post/banner02_nZjpk0S.jpg.400x300_q85_crop.jpg
        modified:   templates/blog/components/posts_latest.html
        modified:   templates/blog/post_detail.html
        new file:   templates/blog/update_blog_post.html

        Note:

        1. Update works.
        2. But there are a lot of tags come up when update a post...? 
           I don't know about JS ..(:

        :)? 