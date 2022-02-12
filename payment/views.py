from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect
from zeep import Client
from datetime import timedelta, datetime
from decouple import config


MERCHANT = config('MERCHANT')
client = config('client')
CallbackURL = config('CallbackURL')


@login_required
def send_request(request):
    description = "تراكنش شما:"
    amount = 500000
    email = request.user.email
    result = client.service.PaymentRequest(MERCHANT, amount, description, email, CallbackURL=CallbackURL)
    if result.Status == 100:
        return redirect('https://www.zarinpal.com/pg/StartPay/' + str(result.Authority))
    else:
        return HttpResponse('Error code: ' + str(result.Status))


@login_required
def verify(request):
    if request.GET.get('Status') == 'OK':
        result = client.service.PaymentVerification(MERCHANT, request.GET['Authority'], amount)
        if result.Status == 100:
            user = request.user
            user.special_user += datetime.now() + timedelta(days=30)
            user.save()
            return HttpResponse('Transaction success.\nRefID: ' + str(result.RefID))
        elif result.Status == 101:
            return HttpResponse('Transaction submitted : ' + str(result.Status))
        else:
            return HttpResponse('Transaction failed.\nStatus: ' + str(result.Status))
    else:
        return HttpResponse('Transaction failed or canceled by user')
