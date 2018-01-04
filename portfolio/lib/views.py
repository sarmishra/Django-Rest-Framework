# for API
from .serializers import MemberSerializer, BookSerializer, BooksDetailSerializer, ReturnDateSerializer, IssueDetailSerializer
from .models import Member, Book, BooksDetail, ReturnDate, IssueDetail
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django .shortcuts import redirect

# For login
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.conf import settings




# list of all member or create new one
# members/
class MemberList(APIView):

    def get(self, request):
        print request.user
        if ( request.user.is_authenticated()):

            members = Member.objects.all()
            books = Book.objects.all()
            serializerBook = BookSerializer(books, many=True)
            serializerMember = MemberSerializer(members, many=True)
            return Response({'members':serializerMember.data,'books':serializerBook.data})

    def post(self):

        pass



# list of all book or create new one
# books/
class BookList(APIView):

    def get(self, request):
        print request.user
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self):

        pass


# list of all books details or create new one
# details/
class BooksDetailList(APIView):

    def get(self, request):
        details = Book.objects.all()
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




def get_auth_token(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        # the password verified for the user
        if user.is_active:
            token, created = Token.objects.get_or_create(user=user)
            request.session['auth'] = token.key
            return redirect('/login/', request)
    return redirect(settings.LOGIN_URL, request)
