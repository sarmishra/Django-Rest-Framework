
from rest_framework import serializers
from .models import Member, Book, BooksDetail, ReturnDate, IssueDetail



#Members and IssueDetails are nested serialization for get operation only
class IssueDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = IssueDetail
        fields = '__all__'


class MemberSerializer(serializers.ModelSerializer):

    tracks = IssueDetailSerializer(many=True)
    class Meta:
        model = Member
        fields = ('id', 'name', 'rollnumber', 'uniqueCode', 'tracks')




#Book and Bookdetails nested serialization for POST method access
class BooksDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = BooksDetail
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    tracks = BooksDetailSerializer(many=True)

    class Meta:
        model = Book
        fields = ('id', 'name', 'remaining', 'author', 'tracks')

    def create(self, validated_data):
        tracks_data = validated_data.pop('tracks')
        book = Book.objects.create(**validated_data)
        for track_data in tracks_data:
            BooksDetail.objects.create(book=book, **track_data)
        return book


class ReturnDateSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReturnDate
        fields = '__all__'



