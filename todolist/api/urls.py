"""
URL Routing for the To-do List API.

/tasks - returns a list of all the Task items. CREATE and READ operations can be performed here.
/tasks/<id> - returns a single Task item using the id primary key. UPDATE and DELETE operations
            can be performed here.
"""

from .views import TaskViewSet, UserViewSet
from rest_framework.routers import DefaultRouter

app_name = 'api'

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename="task")
router.register(r'users', UserViewSet, basename="user")

urlpatterns = router.urls
