"""
URL Routing for the To-do List API.

/tasks - returns a list of all the Task items. CREATE and READ operations can be performed here.
/tasks/<id> - returns a single Task item using the id primary key. UPDATE and DELETE operations
            can be performed here.
"""

from .views import TaskViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')
urlpatterns = router.urls