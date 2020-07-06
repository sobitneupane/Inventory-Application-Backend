
'''
Author: Sobit Neupane
Date: 2nd July, 2020
'''

from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'product', views.ProductViewSet)
router.register(r'godown', views.GodownViewSet)
router.register(r'plythickness', views.PlyThicknessViewSet)
router.register(r'plysize', views.PlySizeViewSet)
router.register(r'beetname', views.BeetNameViewSet)
router.register(r'beetsize', views.BeetSizeViewSet)
router.register(r'plywood', views.PlywoodViewSet)
router.register(r'waterproof', views.WaterProofViewSet)
router.register(r'beet', views.BeetViewSet)
router.register(r'others', views.OthersViewSet)
router.register(r'othersname', views.OthersNameViewSet)
# router.register(r'addplywood', views.addPlywood, basename="addplywood")

urlpatterns = [
    # path('', views.index, name='index'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('addplywood', views.addPlywood, name="addplywood"),
    path('addwaterproof', views.addWaterProof, name="addwaterproof"),
    path('addbeet', views.addBeet, name="addbeet"),
    path('addothers', views.addOthers, name="addothers"),
    path('addbeetname', views.addBeetName, name="addbeetname"),
    path('addothersname', views.addOthersName, name="addothersname"),
    path('formdetails', views.FormViewSet, name="formdetails"),
    path('deletedetails', views.deleteDetails, name='deletedetails'),
    path('deletetype', views.deleteProductType, name='deletetype'),
    path('updatedetails', views.updateDetails, name="updatedetails")
]

# path('laticreteapp/productLine/', views.productLineList.as_view(), name= 'productLineList')
