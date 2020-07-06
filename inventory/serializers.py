
'''
    File contains serializers for translating Django Objects into text
    Author: Sobit Neupane
    Date: 2nd July, 2020
'''
from rest_framework import serializers

from .models import Product, Godown, PlyThickness, PlySize, BeetName, \
                    BeetSize, Plywood, WaterProof, Beet, Others, OthersName


class ProductSerializer(serializers.ModelSerializer):
    '''
    fields: name
    '''
    class Meta:
        model = Product
        fields = ('name',)

class GodownSerializer(serializers.ModelSerializer):
    '''
    fields: name
    '''
    class Meta:
        model = Godown
        fields = ('name',)

class PlyThicknessSerializer(serializers.ModelSerializer):
    '''
    fields: name, image
    '''
    class Meta:
        model = PlyThickness
        fields = '__all__'

class PlySizeSerializer(serializers.ModelSerializer):
    '''
    fields: name
    '''
    class Meta:
        model = PlySize
        fields = '__all__'

class BeetNameSerializer(serializers.ModelSerializer):
    '''
        fields: name,image
    '''
    class Meta:
        model = BeetName
        fields = '__all__'

class OthersNameSerializer(serializers.ModelSerializer):
    '''
        fields: name,image
    '''
    class Meta:
        model = OthersName
        fields = '__all__'

class BeetSizeSerializer(serializers.ModelSerializer):
    '''
        fields: name
    '''
    class Meta:
        model = BeetSize
        fields = '__all__'

class PlywoodSerializer(serializers.ModelSerializer):
    '''
        fields: thickness,size,quantity,price,godown
    '''
    class Meta:
        model = Plywood
        fields = '__all__'

class WaterProofSerializer(serializers.ModelSerializer):
    '''
        fields: thickness,size,quantity,price,godown
    '''
    class Meta:
        model = WaterProof
        fields = '__all__'

class BeetSerializer(serializers.ModelSerializer):
    '''
        fields: name,size,quantity,price,godown
    '''
    class Meta:
        model = Beet
        fields = '__all__'

class OthersSerializer(serializers.ModelSerializer):
    '''
        fields: name,size,quantity,price,godown,image
    '''
    class Meta:
        model = Others
        fields = '__all__'



# class productLineSerializer(serializers.ModelSerializer):
#     lineName = serializers.CharField()

#     class Meta:
#         model  = productLine
#         # fields = ('lineName','image','details',)
#         fields = ('lineName','image',)
