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