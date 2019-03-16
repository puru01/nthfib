from django.shortcuts import render, get_object_or_404  # calc fib if return 404
from fibonacci.models import fibResult
import time
import os
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework import status  # send back status
from rest_framework.views import APIView  # allows normal views to return api data
from rest_framework.response import Response  # 200 response implies it exists in db
from fibonacci.serializers import fibResultSerializer

# Create your views here.
class FibV(APIView):
    def fastFib(n):
        if n == 0:
            return 0
        if n <= 2:
            return int(bool(n))
        k = int(n / 2)
        a = FibV.fastFib(k + 1)
        b = FibV.fastFib(k)
        if n % 2 == 1:
            return a * a + b * b
        return b * (2 * a - b)

    def fibIndex(request):  # get method
        number = 0
        nthFib = 0
        timeTaken = 0
        # fibresult = fibResult.objects.all()
        # serializer = fibResultSerializer(fibresult, many = True)
        # return Response(serializer.data)
        if request.GET.get("number"):
            startTime = time.time()
            number = request.GET.get("number")
            number = int(number)
            nthFib = FibV.fastFib(number)
            endTime = time.time() - startTime
            timeTaken = str(endTime)[0:4]

            obj = fibResult.objects.create(
                number=number, nthFib=nthFib, timeTaken=timeTaken
            )
            obj.save()
        my_dict = {"number": number, "nthFib": nthFib, "timeTaken": timeTaken}

        return render(request, "index.html", context=my_dict)
