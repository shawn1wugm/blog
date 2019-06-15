from django.shortcuts import render

# Create your views here.

def main(request):
    '''
    Show 'Hello world!' in the main page
    '''
    context = {'like':'templates 很棒  需要多練習'}
    return render(request, 'main/main.html', context)
def about(request):
    '''
    Show 'about' in the main page
    '''
    return render(request, 'main/about.html') 

