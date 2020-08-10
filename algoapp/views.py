from django.shortcuts import render
from .forms import PermutationInputForm
from django.http import HttpResponse,JsonResponse
from .johnson_trotter_index import gen_permutations
from .quicksort import quicksort
import json

# Create your views here.
def index(request):
    context = {
        'permutation_form':PermutationInputForm(),
    }
    return render(request,'algoapp/index.html',context=context)

def get_qs(request, qs_input=None):
    if request.method == 'GET':
        if qs_input != None:
            action_list = quicksort(qs_input)
            return JsonResponse({'qs_result':json.dumps(action_list),'status':'ok'})
        else:
            return JsonResponse({'status':'no_content'})

def get_permutation(request,perm_input=None):
    if request.method == 'GET':
        if perm_input != None:
            action_list = gen_permutations(perm_input)
            return JsonResponse({'permutations':json.dumps(action_list),'status':'ok'})
        else:
            return JsonResponse({'status':'no_content'})
def test_d3(request):
    return render(request,'algoapp/testd3.html')