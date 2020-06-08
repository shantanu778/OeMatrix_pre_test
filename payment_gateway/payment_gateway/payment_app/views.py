from django.shortcuts import render
from django.template.response import HttpResponse
import braintree
from django.conf import settings
from django.http import JsonResponse
# Create your views here.



def index(request):

    return render(request, 'index.html')


def checkout(request):
    price = request.GET.get("price","")
    print(price)
    #generate all other required data that you may need on the #checkout page and add them to context. 
    if settings.BRAINTREE_PRODUCTION:
        braintree_env = braintree.Environment.Production
    else:
        braintree_env = braintree.Environment.Sandbox

    # Configure Braintree
    braintree.Configuration.configure(
        braintree_env,
        merchant_id=settings.BRAINTREE_MERCHANT_ID,
        public_key=settings.BRAINTREE_PUBLIC_KEY,
        private_key=settings.BRAINTREE_PRIVATE_KEY,
    )
 
    try:
        braintree_client_token = braintree.ClientToken.generate({ "customer_id": user.id })
    except:
        braintree_client_token = braintree.ClientToken.generate({})

    context = {
        'braintree_client_token': braintree_client_token,
        'price':price,
        }
    return render(request, 'checkout.html', context)



def payment(request):
    price= request.POST.get('price','')
    nonce_from_the_client = request.POST['paymentMethodNonce']
    customer_kwargs = {
        "first_name": request.user.first_name,
        "last_name": request.user.last_name,
        "email": request.user.email,
    }
    customer_create = braintree.Customer.create(customer_kwargs)
    customer_id = customer_create.customer.id
    result = braintree.Transaction.sale({
        "amount": price,
        "payment_method_nonce": nonce_from_the_client,
        "options": {
            "submit_for_settlement": True
        }
    })
    print(result)
    return JsonResponse({'message':1})