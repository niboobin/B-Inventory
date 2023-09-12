from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'application_name' : 'B Inventory',
        'name': 'Muhammad Obin Mandalika',
        'class': 'PBP KKI'
    }

    return render(request, 'main.html', context)