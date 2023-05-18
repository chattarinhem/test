from django.db import models
from rest_framework import serializers
from .models import Todo
from rest_framework import viewsets
from .models import Todo
from .serializers import TodoSerializer
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from todos.views import TodoViewSet



class Todo(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'completed')


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


router = routers.DefaultRouter()
router.register(r'todos', TodoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
