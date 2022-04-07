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

router.get_api_root_view().cls.__name__ = "Middle Earth To Do List"
router.get_api_root_view().cls.__doc__ = \
    """
    'It’s the job that’s never started that takes longest to finish.' — Sam Gamgee.
    Rightly said master Gamgee. Welcome to the To-Do List of the Middle Earth.
    """

urlpatterns = router.urls
