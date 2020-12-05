from django.db import models


# Create your models here.

class Endpoints(models.Model):
    '''
    Endpoints represents the the available endpoints:
    parameters:
    name: Name of the endpoints.
    owner: the name of the model creator.
    created_at: The datatime of the model created.
    '''
    name = models.CharField(max_length=128)
    owner = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True,blank=True)


class MLAlgorithm(models.Model):
    '''
    The MLAgorithm represent the all the algorithms available
    parameters:
    name : name of the MLAlgorithm
    description : the description of the ML algorithm,
    code : The present code of the algorithm updated one.
    version : version of the algorithm.
    owner : the owner of the algorithm.
    created_at : the created date of the algorithmn
    parent_endpoint : the parent endpoints of the algorithmn

    '''
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    code = models.TextField(max_length=50000)
    version = models.CharField(max_length=128)
    owner = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True,blank=True)
    parent_endpoint = models.ForeignKey(Endpoints, on_delete=models.CASCADE)


class MLAlgorithmStatus(models.Model):
    '''
    The MLAlgorithmStatus model represents the status of the avaialble models,
    paraemters:
    status : Status of the model,
    active : the flag which states the model is avtive or inactive,
    created_at : the date time of the model
    created_by : the creator of the model
    parent_mlalgorithm : parent endpoint of the model.
    '''
    status = models.CharField(max_length=128)
    active = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True,blank=True)
    created_by = models.CharField(max_length=128)
    parent_mlalgorithm = models.ForeignKey(MLAlgorithm,on_delete= models.CASCADE)

class MLRequest(models.Model):
    '''
    THe MLRequest model is to get the information about the request received by the model_selection
    Atrributes:
    input_data = The input data that recieves by the model selection
    full_response = the response that receives by the model selection
    response= The response the receive the ML Model
    feedback = the feedback about the model
    created_at = the date of the model created
    parent_mlalgorithm  = the parent_endpoint of the model
    '''

    input_data = models.CharField(max_length=10000)
    full_response = models.CharField(max_length=10000)
    response = models.CharField(max_length = 10000)
    feedback = models.CharField(max_length=10000,blank=True, null=True)
    created_at = models.DateField(auto_now_add = True,blank=True)
    parent_mlalgorithm = models.ForeignKey(MLAlgorithm , on_delete=models.CASCADE)
