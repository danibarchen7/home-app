from rest_framework import serializers
from .models import images ,PropertyImage
from Property.models import Properties
from PIL import Image
class PropertyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyImage
        fields = '__all__'


    # def create(self, validated_data):
    #     image_data = validated_data.pop('image')
    #     image = Image.open(image_data)
    #     property_image = PropertyImage.objects.create(image=image, **validated_data)
    #     return property_image
    

    # def create(self, validated_data):
    #     # Get the uploaded image file
    #     image = validated_data.pop('image')

    #     # Create a new PropertyImage instance with the uploaded image
    #     property_image = PropertyImage.objects.create(image=image)

    #     # Set the other fields of the PropertyImage instance
    #     prop = Properties.objects.get(owner=validated_data.get('pid'))
    #     property_image.pid = prop.owner
    #     property_image.test = validated_data.get('test')

    #     # Save the PropertyImage instance
    #     property_image.save()

    #     return property_image

class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = images
        fields = '__all__'