# Create your views here.
#coding:utf-8
from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.http import HttpResponse
from django.db.models import Q
import sys
import rdkit
from rdkit.Chem import MACCSkeys
from rdkit import Chem
reload(sys)
sys.setdefaultencoding('utf8')
import rdkit
from rdkit.Chem import MACCSkeys
from rdkit import DataStructs
def product_list(request, category_slug=None):
    def checkchinese(check_str):
        for ch in check_str.decode('utf-8'):
            if u'\u4e00' <= ch <= u'\u9fff':
                aaaaaaaaaaaaaaaaaaaaaaa = 1
            else:
                return False
        return True
    a = request.GET.get('aaa', '').strip()
    if checkchinese(a):

        Product.objects.filter(herbname = a).update(xiangsidu=1)
        products = Product.objects.filter(herbname=a)
    else:
        a = a.encode('utf8')
        m1=Chem.MolFromSmiles(a)
        fp1 = MACCSkeys.GenMACCSKeys(m1)
        for i in range(10):
            j=i+1
            tempproduct=Product.objects.get(slug=j)
            tempmol=tempproduct.description.strip()
            m2 = Chem.MolFromSmiles(tempmol)
            fp2 = MACCSkeys.GenMACCSKeys(m2)
            tempxiangsidu = DataStructs.FingerprintSimilarity(fp1,fp2)
            Product.objects.filter(slug=j).update(xiangsidu=tempxiangsidu)
        products = Product.objects.order_by('-xiangsidu')
        # products = Product.objects.filter()
    category = None
    categories = Category.objects.filter()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                  'categories': categories,
                  'products': products})
#查询结果展示
def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                )
    return render(request,
                  'shop/product/detail.html',
                  {'product': product})
#查询结果中点击进入查看详细信息
def index(request):
    return render(request, 'shop/index.html')
#查询界面