from django.shortcuts import render
from .forms import RegistrationAccountForm



# Create your views here.
def registrationView(request):
    template_name = 'registration/user_registration.html'
    form = RegistrationAccountForm()
    if request.POST:
        form = RegistrationAccountForm(request.POST)
        if form.is_valid():
            print('form output .......', form.data)
            form.save()
        else:
            print(form.errors)


    context = {
        'form': form
    }

    return render (request, template_name, context)



