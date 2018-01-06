# for API
from rest_framework.permissions import IsAuthenticated,AllowAny

from .serializers import MemberSerializer, BookSerializer, BooksDetailSerializer, ReturnDateSerializer, IssueDetailSerializer
from .models import Member, Book, BooksDetail, ReturnDate, IssueDetail
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django .shortcuts import redirect
from rest_framework.decorators import api_view



# For login
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.conf import settings


# list of all member or create new one
# members/
class MemberList(APIView):
    permission_classes = (AllowAny,)
    def get(self, request):
        members = Member.objects.all()
        books = Book.objects.all()
        serializerBook = BookSerializer(books, many=True)
        serializerMember = MemberSerializer(members, many=True)
        return Response({'members':serializerMember.data,'books':serializerBook.data})

    def post(self):

        pass




# list of all book or create new one
# books/
# @api_view(['GET','POST'])
class BookList(APIView):

    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




#Retrieve, update or delete a code Book.
#csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def BookList_id(request, pk,):
    try:
        snippet = Book.objects.get(pk=pk)
    except snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BookSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
    # data = JSONParser().parse(request)
        serializer = BookSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




# list of all books details or create new one
# details/
class BooksDetailList(APIView):

    def get(self, request):
        details = BooksDetail.objects.all()
        serializer = BooksDetailSerializer(details, many=True)
        return Response(serializer.data)

    def post(self):

        pass




# list of all returns dates  or create new one
# dates/
class ReturnDateList(APIView):

    def get(self, request):
        dates = ReturnDate.objects.all()
        serializer =ReturnDateSerializer(dates, many=True)
        return Response(serializer.data)

    def post(self):

        pass




# list of all books issue details or create new one
# issue/
class IssueDetailList(APIView):

    def get(self, request):
        issue = IssueDetail.objects.all()
        serializer = IssueDetailSerializer(issue, many=True)
        return Response(serializer.data)

    def post(self):

        pass




#Login Viwes

# def home(request):
# 	template_name='lib/home.html'
# 	return render(request,template_name)
#




# Dashboard After login
@login_required
def dashboard(request):
    template_name = 'lib/dashboard.html'
    return render(request, template_name)




# def get_auth_token(request):
#     username = request.POST.get('username')
#     password = request.POST.get('password')
#     user = authenticate(username=username, password=password)
#     if user is not None:
#         # the password verified for the user
#         if user.is_active:
#             token, created = Token.objects.get_or_create(user=user)
#             request.session['auth'] = token.key
#             return redirect('/login/', request)
#     return redirect(settings.LOGIN_URL, request)
