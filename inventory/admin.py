'''
Admin Panel
'''
from django.contrib import admin

from .models import Product, Godown, PlyThickness, PlySize, BeetName, BeetSize, Plywood, WaterProof, Beet, Others

admin.site.register([
    Product, Godown, PlyThickness, PlySize, BeetName, BeetSize, Plywood,
    WaterProof, Beet, Others
])
