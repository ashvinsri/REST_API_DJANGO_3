from rest_framework import serializers
from myapp.models import Student


class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=['clas','name','city']



# class StudentSerializers(serializers.Serializer):
#     clas=serializers.CharField(max_length=264)
#     name=serializers.CharField(max_length=264)
#     city=serializers.CharField(max_length=264)

#     def create(self,validate_data):
#         return Student.objects.create(**validate_data)

#     def update(self,instance,validated_data):
#         instance.clas=validated_data.get('clas',instance.clas)
#         print(instance.name)
#         instance.name=validated_data.get('name',instance.name)
#         print(instance.name)
#         instance.city=validated_data.get('city',instance.city)
#         instance.save()
#         return instance
    
#     def validate_clas(self,value):
#         if int(value)>=200:
#             raise serializers.ValidationError('Seat Full')
#         return value
