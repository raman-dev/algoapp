from django.shortcuts import render
from .forms import PermutationInputForm
from django.http import HttpResponse,JsonResponse
from .johnson_trotter import gen_permutations

# Create your views here.
def index(request):
    context = {
        'permutation_form':PermutationInputForm(),
    }
    return render(request,'algoapp/index.html',context=context)

def get_permutation(request,perm_input=None):
    if request.method == 'GET':
        if perm_input != None:
            permutations = gen_permutations(perm_input)
            return JsonResponse({'permutations':str(permutations),'status':'ok'})
        else:
            print('input == None')
            return JsonResponse({'status':'no_content'})
def test_d3(request):
    return render(request,'algoapp/testd3.html')