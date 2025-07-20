from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Customer
from .serializer import CustomerSerializer


# Create your views here.

class RegisterCustomer(APIView):
    def post(self, request):
        data = request.data
        salary = data.get("monthly_income")

        approved_limit= round(36* int(salary)/100000) * 100000

        customer = Customer.objects.create(
            first_name=data["first_name"],
            last_name= data["last_name"],
            age=data["age"],
            phone_number= data["phone_number"],
            monthly_income= salary,
            approved_limit=approved_limit
        )

        serializer= CustomerSerializer(customer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)