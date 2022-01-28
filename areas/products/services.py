from models import Category, Product

def getTrendingCategories():
    return Category.query.order_by(Category.CategoryID.desc()).paginate(1,4,False).items

def getCategory(id):
    return Category.query.filter(Category.CategoryID ==id).first()

def getProduct(id):
    return Product.query.filter(Product.ProductID ==id).first()
