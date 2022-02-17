def importe_total_carro(request):
    total=0
    #if request.user.is_authenticated:
    try:
        if request.session.get('carro', False):    
            for key, value in request.session["carro"].items():
                total = total + (float(value["precio"]))
    except:
        total = 0
    return {"importe_total_carro":total}



