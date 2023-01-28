from django.shortcuts import render
from rest_framework.generics import *
from rest_framework.response import Response
import pickle


model = pickle.load(open('model/modell.pkl','rb'))

# Create your views here.
class MlDataPredict(CreateAPIView):
    
    def post(self,request):
        quantity = float(request.data.get('quantity'))
        volumn = float(request.data.get('volumn'))
        distfromIndia = float(request.data.get('dist'))
        
        fv = [[quantity,volumn,distfromIndia]]
        p = model.predict(fv)
        
        return Response({'Predicted Price':p})