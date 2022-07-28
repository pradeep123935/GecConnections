from django import forms
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, get_connection
 
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Your Name', widget=forms.TextInput(attrs={ 'class': 'form-control' }))
    email = forms.EmailField(label='Your e-mail address', widget=forms.TextInput(attrs={ 'class': 'form-control' }))
    subject = forms.CharField(max_length=100, widget=forms.TextInput(attrs={ 'class': 'form-control' }))
    message = forms.CharField(required=False, widget=forms.Textarea(attrs={ 'class': 'form-control' }))
  
def contact(request):
    submitted = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
             # assert False
            con = get_connection('django.core.mail.backends.console.EmailBackend')
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['cairocoders0711@gmail.com'],
                connection=con
             )
            return HttpResponseRedirect('/contact?submitted=True')
    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            submitted = True
 
    return render(request, 'contact/contact.html', {'form': form, 'submitted': submitted})