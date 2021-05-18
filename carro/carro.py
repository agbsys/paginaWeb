class Carro:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carro = self.session.get("carro")
        if not carro:
            carro = self.session["carro"]={}
        else:
            self.carro = carro
    
    def agregar(self, productos):
        if str(productos.id) not in self.carro.keys():
            self.carro[producto.id]={
                "producto_id":productos.id,
                "descripcion":productos.descripcion,
                "precio":str(productos.precio),
                "cantidad":1,
                "imagen":productos.imagen.url
            }
        else:
            for key, value in self.carro.items():
                if key==str(productos.id):
                    value["cantidad"]=value["cantidad"]+1
                    break
            self.guardarCarro()

    def guardarCarro(self):
        self.session["carro"]=self.carro
        self.session.modified=True

    def eliminarProducto(self, productos):
        if str(productos.id) in self.carro.keys():
            del self.carro[productos.id]
            self.guardarCarro()

    def restar_producto(self, productos):
        if str(productos.id) in self.carro.keys():
            for key, value in self.carro.items():
                if key==str(productos.id):
                    value["cantidad"]=value["cantidad"]-1
                    if value["cantidad"]==0:
                        del self.carro[productos.id]
                    break
            self.guardarCarro()

    def limparCarro(self):
        self.carro = self.session["carro"]={}
        self.session.modified=True