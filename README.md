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