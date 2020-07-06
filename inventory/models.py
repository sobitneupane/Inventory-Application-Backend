'''
File containing the database models for inventory app
Author: Sobit Neupane
Date: 2nd July, 2020
'''

from django.db import models


class Product(models.Model):
    '''
    Product Model contians the name of major products like plywood, beet,etc
    '''
    name = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.name


class Godown(models.Model):
    '''
    Contains the name of Godowns like A, B
    '''
    name = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return self.name


class PlyThickness(models.Model):
    '''
    contains thickness and image of plywood like 6mm, 10mm
    '''
    name = models.CharField(max_length=20, primary_key=True)
    image = models.ImageField(upload_to="ply/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ply Thickness"
        verbose_name_plural = "Ply Thickness"


class PlySize(models.Model):
    '''
    contains dimension of plywood like 5*3, 6*4
    '''
    name = models.CharField(max_length=20, primary_key=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ply Size"
        verbose_name_plural = "Ply Size"


class BeetName(models.Model):
    '''
    contains name of Beet like Dori Beet with its image
    '''
    name = models.CharField(max_length=100, primary_key=True)
    image = models.ImageField(upload_to="beet/")

    def __str__(self):
        return self.name


class OthersName(models.Model):
    '''
    contains name of Beet like Dori Beet with its image
    '''
    name = models.CharField(max_length=100, primary_key=True)
    image = models.ImageField(upload_to="others/")

    def __str__(self):
        return self.name


class BeetSize(models.Model):
    '''
    contains size of Beet like 1/2" , 1"
    '''
    name = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return self.name


class Plywood(models.Model):
    '''
    contains detail of specific plywood
    '''
    thickness = models.ForeignKey(PlyThickness, on_delete=models.CASCADE)
    size = models.CharField(
        max_length=20)  #models.ForeignKey(PlySize, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField()
    godown = models.ForeignKey(Godown, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.thickness.name + " Size:" + self.size + " Godown:" +
                   self.godown.name)


class WaterProof(models.Model):
    '''
    contains detail of specific waterproof plywood
    '''
    thickness = models.ForeignKey(PlyThickness, on_delete=models.CASCADE)
    size = models.CharField(
        max_length=20)  #models.ForeignKey(PlySize, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField()
    godown = models.ForeignKey(Godown, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.thickness.name + " Size:" + self.size + " Godown:" +
                   self.godown.name)


class Beet(models.Model):
    '''
    contains detail of specific beet
    '''
    name = models.ForeignKey(BeetName, on_delete=models.CASCADE)
    size = models.CharField(max_length=50)
    quantity = models.IntegerField()
    price = models.FloatField()
    godown = models.ForeignKey(Godown, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name.name + " Size:" + self.size + " Godown:" +
                   self.godown.name)


class Others(models.Model):
    '''
    contains details of other products like kabja, dhoka
    '''
    name = models.ForeignKey(
        OthersName,
        on_delete=models.CASCADE)  #models.CharField(max_length=100)
    size = models.CharField(max_length=20)
    quantity = models.IntegerField(default=0)
    price = models.FloatField(default=0.0)
    godown = models.ForeignKey(Godown, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="others/")

    def __str__(self):
        return str(self.name.name + " Size:" + self.size + " Godown:" +
                   self.godown.name)
