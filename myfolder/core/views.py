from turtle import title
from django.shortcuts import render,redirect
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Course
from .serializers import CourseSerializer, GetAllCourseSerializer
from .forms import CourseForm
from django.http import Http404, HttpResponse
from django.db.models import Q
from django.core.paginator import Paginator

class Homepage(View):
    def get(self,request):
        return render(request, 'index.html')

class GetAllCourseAPIView(APIView):
    def get(self,request):
        list_course = Course.objects.all()
        mydata = GetAllCourseSerializer(list_course, many=True)
        return Response(data= mydata.data, status = status.HTTP_200_OK)

    def post(self,request):
        mydata = CourseSerializer(data=request.data)
        if not mydata.is_valid():
            return Response('sai du lieu', status=status.HTTP_400_BAD_REQUEST)
        title = mydata.data['title1']
        content = mydata.data['content1']
        price = mydata.data['price1']
        cs = Course.objects.create(title=title, price=price,content=content) 
        return Response(data=cs.id, status=status.HTTP_200_OK)

class Example(View):
    def get(self,request):
        return render(request, 'example.html')

class list(View):
    def get(self,request):
        mylists = Course.objects.all()
        query = request.GET.get('q')
        if query:
            mylists = mylists.filter(Q(title__icontains=query)|
                                    Q(content__icontains=query)|
                                    Q(price__icontains=query))
        paginator = Paginator(mylists,2)
        page = request.GET.get('page')
        try:
            mylists = paginator.page(page)
        except:
            mylists = paginator.page(1)
        context = {'mylists': mylists}
        return render(request, 'list.html', context)

class create(View):
    def get(self,request):
        myform = CourseForm(request.POST or None, request.FILES or None)
        if myform.is_valid():
           instance = myform.save(commit=False)
           instance.save()
           return redirect('list')

        context = {'form':myform}
        return render(request, 'mycreate.html',context)

def mycreate(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    if not request.user.is_authenticated():
        return HttpResponse('You dont login')
    

    myform = CourseForm(request.POST or None, request.FILES or None)
    if myform.is_valid():
        instance = myform.save(commit=False)
        instance.save()
        return redirect('list')

    context = {'form':myform}
    return render(request, 'mycreate.html',context)
