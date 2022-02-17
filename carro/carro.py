class Carro:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carro = self.session.get("carro")
        if not carro:
            carro = self.session["carro"]={}
        #else:
        self.carro = carro
    
    def agregar(self, productos):
        if str(productos.id) not in self.carro.keys():
            self.carro[productos.id]={
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
                    value["precio"] = float(value["precio"]) + productos.precio
                    break
            self.guardarCarro()

    def guardarCarro(self):
        self.session["carro"]=self.carro
        self.session.modified=True

    def eliminarProducto(self, productos):
        productos.id = str(productos.id)
        if productos.id in self.carro:
            del self.carro[productos.id]
            self.guardarCarro()

    def restar_producto(self, productos):
        if str(productos.id) in self.carro.keys():
            for key, value in self.carro.items():
                if key==str(productos.id):
                    value["cantidad"]=value["cantidad"]-1
                    value["precio"] = float(value["precio"]) - productos.precio
                    if value["cantidad"]<1:
                        self.eliminarProducto(productos)
                    break
            self.guardarCarro()

    def limparCarro(self):
        self.carro = self.session["carro"]={}
        self.session.modified=True