from django.urls import path,include
from rest_framework import routers
from rest_framework_nested import routers

from . import views

router = routers.SimpleRouter()
router.register('course',views.CourseViewSet),
router.register('class',views.ClassViewSet)
router.register('section',views.SectionViewSet)

course_router = routers.NestedSimpleRouter(router, r'course', lookup='course')
course_router.register(r'class', views.CourseClassViewSet, base_name='course-class')

examTerm_router = routers.NestedSimpleRouter(router, r'class', lookup='class')
examTerm_router.register(r'term', views.ClassExamTermViewSet, base_name='class-term')

section_router = routers.NestedSimpleRouter(router, r'class', lookup='class')
section_router.register(r'section', views.ClassSectionViewset, base_name='class-section')


urlpatterns = [
	path('',include(router.urls)),
    path('',include(course_router.urls)),
    path('',include(examTerm_router.urls)),
    path('',include(section_router.urls)),
]