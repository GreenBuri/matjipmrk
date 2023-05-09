from django import forms
from .models import Restaurant, Filter

# FilterForm은 프론트와 백엔드(모델:Filter)간의 중간다리 역할을 해준다.
class FilterForm(forms.ModelForm): #forms 도 생성해줍니다.
    class Meta:
        model = Filter #Filter 모델을 기반으로
        fields = '__all__' #Front에 있는 Filter Fomr에서 모든 정보를 DB로 보내겠다.

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name','location','latitude','longitude','foodtype']



