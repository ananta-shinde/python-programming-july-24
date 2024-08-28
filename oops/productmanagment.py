
class Product:
    id = None
    name = None
    price = None
    category = None
    description = None

class ProductManager:
    __productList = []

    def getProductCount(self):
        return len(self.__productList)

    def getProductList(self):
        return self.__productList
    def addProductToList(self,product):
        self.__productList.append(product)


class Admin:
    name = None
    username = None
    password = None
    productManager = ProductManager()


    def getProductList(self):
        return self.productManager.getProductList()

    def createProduct(self):
        product = Product()
        product.id = self.productManager.getProductCount()+1
        product.name = input("Enter product name :")
        product.price = float(input("Enter product price :"))
        product.description = input("Enter product description :")
        self.productManager.addProductToList(product)





admin = Admin()
admin.createProduct()
print(admin.getProductList())
