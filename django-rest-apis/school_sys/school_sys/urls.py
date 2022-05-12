from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', include('student.urls')),
    path('tutors/', include('tutor.urls')),
    path('school/', include('school.urls')),
]
