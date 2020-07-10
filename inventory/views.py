'''
Author: Sobit Neupane
Date: 2nd July, 2020
'''
import base64
import json
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.base import ContentFile

from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from .serializers import ProductSerializer, GodownSerializer, PlyThicknessSerializer,\
                         PlySizeSerializer, BeetNameSerializer, BeetSizeSerializer, \
                         PlywoodSerializer, WaterProofSerializer, OthersNameSerializer, \
                         BeetSerializer, OthersSerializer
from .models import Product, Godown, PlyThickness, PlySize, BeetName, \
                    BeetSize, Plywood, WaterProof, Beet, Others, OthersName


def index(request):
    '''
    view of main/index page
    '''
    return HttpResponse("Index Page")


class ProductViewSet(viewsets.ModelViewSet):
    '''
    Model: Product
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class GodownViewSet(viewsets.ModelViewSet):
    '''
    Model: Godown
    '''
    queryset = Godown.objects.all()
    serializer_class = GodownSerializer


class PlyThicknessViewSet(viewsets.ModelViewSet):
    '''
    Model: PlyThickness
    '''
    queryset = PlyThickness.objects.all()
    serializer_class = PlyThicknessSerializer


class PlySizeViewSet(viewsets.ModelViewSet):
    '''
    Model: PlySize
    '''
    queryset = PlySize.objects.all()
    serializer_class = PlySizeSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']

    def get_queryset(self):
        queryset = PlySize.objects.select_related().all()
        name = self.request.query_params.get('name', None)
        if name is not None:
            queryset = queryset.filter(name=name)
        return queryset


class BeetNameViewSet(viewsets.ModelViewSet):
    '''
    Model: BeetName
    '''
    queryset = BeetName.objects.all()
    serializer_class = BeetNameSerializer


class OthersNameViewSet(viewsets.ModelViewSet):
    '''
    Model: BeetName
    '''
    queryset = OthersName.objects.all()
    serializer_class = OthersNameSerializer


class BeetSizeViewSet(viewsets.ModelViewSet):
    '''
    Model: BeetSize
    '''
    queryset = BeetSize.objects.all()
    serializer_class = BeetSizeSerializer


class PlywoodViewSet(viewsets.ModelViewSet):
    '''
    Model: Plywood
    '''
    queryset = Plywood.objects.select_related().all().order_by("size")
    serializer_class = PlywoodSerializer
    filter_backends = [SearchFilter]
    search_fields = ['thickness']

    def get_queryset(self):
        queryset = Plywood.objects.select_related().all().order_by("size")
        thickness = self.request.query_params.get('thickness', None)
        if thickness is not None:
            queryset = queryset.filter(thickness=thickness)
        return queryset


class BeetViewSet(viewsets.ModelViewSet):
    '''
    Model: Beet
    '''
    queryset = Beet.objects.all().order_by("size")
    serializer_class = BeetSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']

    def get_queryset(self):
        queryset = Beet.objects.all().order_by("size")
        name = self.request.query_params.get('name', None)
        if name is not None:
            queryset = queryset.filter(name=name)
        return queryset


class WaterProofViewSet(viewsets.ModelViewSet):
    '''
    Model: WaterProof
    '''
    queryset = WaterProof.objects.all().order_by("size")
    serializer_class = WaterProofSerializer
    filter_backends = [SearchFilter]
    search_fields = ['thickness']

    def get_queryset(self):
        queryset = WaterProof.objects.all().order_by("size")
        thickness = self.request.query_params.get('thickness', None)
        if thickness is not None:
            queryset = queryset.filter(thickness=thickness)
        return queryset


class OthersViewSet(viewsets.ModelViewSet):
    '''
    Model: Others
    '''
    queryset = Others.objects.all().order_by("size")
    serializer_class = OthersSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']

    def get_queryset(self):
        queryset = Others.objects.all().order_by("size")
        name = self.request.query_params.get('name', None)
        if name is not None:
            queryset = queryset.filter(name=name)
        return queryset


def FormViewSet(request):
    '''
        for form details
    '''
    productname = Product.objects.all()
    plysize = PlySize.objects.all()
    plythickness = PlyThickness.objects.all()
    godown = Godown.objects.all()
    beetname = BeetName.objects.all()
    beetsize = BeetSize.objects.all()
    othersname = OthersName.objects.all()

    jn = {}

    lis = []
    for el in productname:
        lis.append(el.name)
    jn["productName"] = lis

    lis = []
    for el in plysize:
        lis.append(el.name)
    jn["plySize"] = lis

    lis = []
    for el in plythickness:
        lis.append(el.name)
    jn["plyThickness"] = lis

    lis = []
    for el in godown:
        lis.append(el.name)
    jn["godown"] = lis

    lis = []
    for el in beetname:
        lis.append(el.name)
    jn["beetName"] = lis

    lis = []
    for el in beetsize:
        lis.append(el.name)
    jn["beetSize"] = lis

    lis = []
    for el in othersname:
        lis.append(el.name)
    jn["othersName"] = lis
    data = json.dumps(jn)
    return HttpResponse(data, content_type='application/json')


def addPlywood(request):
    '''
    add plywood with its details ,i.e. thickness, size, price, quantity and godown
    '''
    thickness = request.GET.get('thickness', None)
    thickness = PlyThickness.objects.get(name=thickness)

    size = request.GET.get('size', None)

    quantity = request.GET.get('quantity', None)
    if quantity is None:
        quantity = 0

    price = request.GET.get('price', None)
    if price is None:
        price = 0.0

    godown = request.GET.get('godown', None)
    godown = Godown.objects.get(name=godown)
    Plywood.objects.create(thickness=thickness,
                           quantity=quantity,
                           price=price,
                           godown=godown,
                           size=size)
    return JsonResponse({'message': 'plywood added successfully'})


def addWaterProof(request):
    '''
    add waterproof plywood with its details ,i.e. thickness, size, price, quantity and godown
    '''
    thickness = request.GET.get('thickness', None)
    thickness = PlyThickness.objects.get(name=thickness)

    size = request.GET.get('size', None)

    quantity = request.GET.get('quantity', None)
    if quantity is None:
        quantity = 0

    price = request.GET.get('price', None)
    if price is None:
        price = 0.0

    godown = request.GET.get('godown', None)
    godown = Godown.objects.get(name=godown)

    WaterProof.objects.create(thickness=thickness,
                              size=size,
                              quantity=quantity,
                              price=price,
                              godown=godown)
    return JsonResponse({'message': 'WaterProof Plywood added successfully'})


def addBeet(request):
    '''
    add beet with its details ,i.e. name, size, price, quantity and godown
    '''
    name = request.GET.get('name', None)
    name = BeetName.objects.get(name=name)

    size = request.GET.get('size', None)
    if size is None:
        size = ' '

    quantity = request.GET.get('quantity', None)
    if quantity is None:
        quantity = 0

    price = request.GET.get('price', None)
    if price is None:
        price = 0.0

    godown = request.GET.get('godown', None)
    godown = Godown.objects.get(name=godown)

    Beet.objects.create(name=name,
                        size=size,
                        quantity=quantity,
                        price=price,
                        godown=godown)
    return JsonResponse({'message': 'Beet added successfully'})


def addOthers(request):
    '''
    add other product with its details ,i.e. name, size, price, quantity and godown
    '''
    name = request.GET.get('name', None)
    name = OthersName.objects.get(name=name)

    size = request.GET.get('size', None)
    if size is None:
        size = ''

    quantity = request.GET.get('quantity', None)
    if quantity is None:
        quantity = 0

    price = request.GET.get('price', None)
    if price is None:
        price = 0.0

    godown = request.GET.get('godown', None)
    godown = Godown.objects.get(name=godown)

    Others.objects.create(name=name,
                          size=size,
                          quantity=quantity,
                          price=price,
                          godown=godown)
    return JsonResponse({'message': 'Other product added successfully'})


@csrf_exempt
def addBeetName(request):
    '''
    add beetname with its details ,i.e. name, image
    '''
    name = request.POST.get('name', None)
    if name is None:
        name = ''

    image = request.POST.get('image', None)
    # forma, imgstr = image.split(';base64,')

    data = ContentFile(base64.b64decode(image), name=name)

    BeetName.objects.create(name=name, image=data)
    return JsonResponse({'message': 'BeetName added successfully'})


@csrf_exempt
def addOthersName(request):
    '''
    add others name with its details ,i.e. name, image
    '''
    name = request.POST.get('name', None)
    if name is None:
        name = ''

    image = request.POST.get('image', None)
    # forma, imgstr = image.split(';base64,')

    data = ContentFile(base64.b64decode(image), name=name)

    OthersName.objects.create(name=name, image=data)
    return JsonResponse({'message': 'Othersname added successfully'})


@csrf_exempt
def deleteProductType(request):
    '''
        Deleting productType of Beet(like DoriBeet) and Others (likeDhoka)
    '''
    pType = request.POST.get('type', None)
    name = request.POST.get('name', None)
    if pType == "beet":
        BeetName.objects.filter(name=name).delete()
    elif pType == "others":
        OthersName.objects.filter(name=name).delete()

    return JsonResponse({'message': 'Deleted Successfully'})


@csrf_exempt
def deleteDetails(request):
    '''
        Deleting details of products
    '''
    pType = request.POST.get('type', None)
    pid = request.POST.get('id', None)
    if pType == "plywood":
        Plywood.objects.filter(id=pid).delete()
    elif pType == "beet":
        Beet.objects.filter(id=pid).delete()
    elif pType == "waterproof":
        WaterProof.objects.filter(id=pid).delete()
    elif pType == "others":
        Others.objects.filter(id=pid).delete()

    return JsonResponse({'message': 'Deleted Successfully'})


@csrf_exempt
def updateDetails(request):
    '''
        Updating Details
    '''
    operationType = request.POST.get('oType', None)
    productType = request.POST.get('pType', None)
    pid = request.POST.get('id', None)
    quantity = request.POST.get('quantity', None)
    print(request.POST)
    if operationType == "add":
        if productType == "plywood":
            Plywood.objects.filter(id=pid).update(quantity=quantity)
        elif productType == "waterproof":
            WaterProof.objects.filter(id=pid).update(quantity=quantity)
        elif productType == "others":
            Others.objects.filter(id=pid).update(quantity=quantity)
        elif productType == "beet":
            Beet.objects.filter(id=pid).update(quantity=quantity)

    # elif operationType = "subtract":
    #     if productType = "plywood":

    #     elif productType = "waterproof":

    #     elif productType = "others":

    #     elif productType = "beet":

    elif operationType == "edit":
        size = request.POST.get('size', None)
        price = request.POST.get('price', None)
        godown = request.POST.get('godown', None)
        godown = Godown.objects.get(name=godown)

        if productType == "plywood":
            thickness = request.POST.get('name', None)
            thickness = PlyThickness.objects.get(name=thickness)
            Plywood.objects.filter(id=pid).update(thickness=thickness.name,
                                                  size=size,
                                                  quantity=quantity,
                                                  price=price,
                                                  godown=godown.name)
        elif productType == "waterproof":
            thickness = request.POST.get('name', None)
            thickness = PlyThickness.objects.get(name=thickness)
            WaterProof.objects.filter(id=pid).update(thickness=thickness,
                                                     size=size,
                                                     quantity=quantity,
                                                     price=price,
                                                     godown=godown)
        elif productType == "others":
            name = request.POST.get('name', None)
            name = OthersName.objects.get(name=name)
            Others.objects.filter(id=pid).update(name=name,
                                                 size=size,
                                                 quantity=quantity,
                                                 price=price,
                                                 godown=godown)
        elif productType == "beet":
            name = request.POST.get('name', None)
            name = BeetName.objects.get(name=name)
            Beet.objects.filter(id=pid).update(name=name,
                                               size=size,
                                               quantity=quantity,
                                               price=price,
                                               godown=godown)
    return JsonResponse({'message': 'Operation Successfull'})
