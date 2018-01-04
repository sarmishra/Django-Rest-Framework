
from rest_framework import serializers
from .models import Member, Book, BooksDetail, ReturnDate, IssueDetail

class MemberSerializer(serializers.ModelSerializer):
    """Should be accessible by authorized user only"""
    class Meta:
        model = Member
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    """should be accessible by anonymos user"""
    class Meta:
        model = Book
        fields = '__all__'

class BooksDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = BooksDetail
        fields = '__all__'


class ReturnDateSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReturnDate
        fields = '__all__'


class IssueDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = IssueDetail
        fields = '__all__'

