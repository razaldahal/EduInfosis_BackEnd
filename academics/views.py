from django.shortcuts import render
from rest_framework import viewsets,status
from django.core.exceptions import ValidationError
from rest_framework.response import Response

from .models import *
from exam.models import ExamTerm
from .serializers import *

class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
class CourseViewSet(viewsets.ModelViewSet):
    queryset=Course.objects.all()
    serializer_class=CourseSerializer
    
    def create(self,request):
        serializer=self.get_serializer(data=request.data)
        if serializer.is_valid():
            data=serializer.data 
            obj,created =Course.objects.get_or_create(
            	name=data['name'],
                code=data['code'],
                defaults={'description':data['description']}
                
                )
            if not created:
            	raise ValidationError({
	        	    'Detail':['Course Already Exist']
	       		    })
            else:
                return Response(data,status=status.HTTP_201_CREATED)
      

        else:
            return Response({'Detail':[serializer.errors]},status=status.HTTP_400_BAD_REQUEST)

    # def retrieve(self,request,pk):
    #     try:
    #         instance = Course.objects.get(id=pk)
    #     except Exception as error:
    #         return Response(error)
    #     dict={
    #         'name':instance.name,
    #         'description':instance.description,
    #         'code':instance.code,
    #         'department':instance.department#.name
    #     }
    #     return Response(dict)

    def list(self,request):
        courses = self.queryset
        course_list =[]

        for course in courses:
            dct ={
            'id':course.id,
            'name':course.name,
            'code':course.code,
            'description':course.description
            }
            course_list.append(dct)

        return Response(course_list)


class CourseClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    
    http_method_names = ['get', 'post', 'delete']

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()

        if self.request.method == 'POST':
            serializer_class = ClassPostSerializer
        return serializer_class(*args, **kwargs)
    
   
    def create(self,request, course_pk):
        
        serializer=self.get_serializer(data=request.data)
        
        if serializer.is_valid():
            data=serializer.data
           # course = False
            try:
                course = Course.objects.get(id=course_pk)
            except:
                raise serializers.ValidationError({'Detail':['No such course']})
            else:
                _class, created = Class.objects.get_or_create(course=course, name=data['name'], 
                                    defaults={'description':data['description']})
                if not created:
                    raise serializers.ValidationError({'Detail': ['{} class already exists'.format(_class.name)]})

               # data = ClassSerializer(_class).data
                return Response(data)
        else:
            raise serializers.ValidationError({'Detail':[serializer.errors]})
        
    def list(self, request, course_pk, pk=None):
        #print("hdsjshdb")
        queryset = self.queryset.filter(course_id=course_pk).all()
       # print(queryset)
         # output = self.get_serializer(queryset, many=True).data
        output = []
        for _class in queryset:
            dct = {
               "id":_class.id,
               "name":_class.name,
               "description":_class.description,
               "course":_class.course.name
               }
            output.append(dct)
        return Response(output)

class ClassExamTermViewSet(viewsets.ViewSet):
    queryset = ExamTerm.objects.all()
    serializers = ExamTermGetSerializer()

    def list(self, request, class_pk, pk=None):
        queryset = self.queryset.filter(_class=class_pk).all()
        output = []
        for term in queryset:
            dct = {
               "id":term.id,
               "name":term.name,
               "start_date":term.start_date,
               "end_date":term.end_date,
  
               }
            output.append(dct)
        return Response(output,status=status.HTTP_200_OK)


class SectionViewSet(viewsets.ViewSet):
    queryset = Section.objects.all()
    serializers = SectionSerializer()
    def create(self,request):
        serializer = SectionSerializer(data=request.data)
        if serializer.is_valid():
            data=serializer.data 
            try:
                __class = Class.objects.get(id=data['_class'])
            except:
                raise serializers.ValidationError({
                    "Detail":[ " Class With This IdNot Exist On Database"]
                })
            if __class:
                obj,created =Section.objects.get_or_create(
                                                name=data['name'],
                                                _class_id=data['_class'])
                if not created:
                    raise serializers.ValidationError({
                        'Detail':['Section Already Exist']
                        })
            else:
                return Response(data,status=status.HTTP_201_CREATED)
      

        return Response({'Detail':[serializer.errors]},status=status.HTTP_400_BAD_REQUEST)


class ClassSectionViewset(viewsets.ViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

    def list(self,request,class_pk,pk=None):
        queryset = self.queryset.filter(_class=class_pk).all()
        output = []
        for section in queryset:
            temp ={
                "id":section.id,
                "name":section.name,
                "class":section._class.name
            }
            output.append(temp)
        return Response(output,status=status.HTTP_200_OK)