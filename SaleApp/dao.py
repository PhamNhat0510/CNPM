import json
from models import Category,Product

def load_categories():
    # with open("data/category.json",encoding="utf-8") as f:
    #     return json.load(f)
    return Category.query
def load_products(q=None,cate_id=None):
    # with open("data/products.json",encoding="utf-8") as f:
    #     prods=json.load(f)
    #     if q:
    #         prods=[p for p in prods if p["name"].find(q)>=0]
    #     if cate_id:
    #         prods=[p for p in prods if p["cate_id"].__eq__(int(cate_id))]
    #     return prods
    query=Product.query
    if q:
        query=query.filter(Product.name.contains(q))
    if cate_id:
        query=query.filter(Product.cate_id.__eq__(int(cate_id)))
    return query.all()
def get_product_by_id(id):
    return Product.query.get(id)
if __name__=="__main__":
    print(load_categories())