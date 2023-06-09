from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from core.base.models import Product, Review, Category
from core.base.serializers import ProductSerializer, CategorySerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth.hashers import make_password
from rest_framework import status
# Create your views here.
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


@api_view(['GET'])
def getCategories(request):
    categories = Category.objects.all()
    if len(categories) == 0:
        return Response("Category is empty", status=status.HTTP_204_NO_CONTENT)
    else:
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



@api_view(['GET'])
def getCategory(request, pk):
    category = Category.objects.get(_id=pk)
    if category is not None: 
        serializer = CategorySerializer(category, many=False)
        return Response(serializer.data)
    else:
        return Response("Category is not found", status=status.HTTP_404_NOT_FOUND)
 
 
        
@api_view(['Post'])
@permission_classes([IsAdminUser])
def createCategory(request):        
    title = request.data['title']
    category = Category.objects.create(
        title = title,
    )    
    serializer = CategorySerializer(category, many=False)
    return Response(serializer.data)         



       
@api_view(['PUT'])
@permission_classes([IsAdminUser])
def updateCategory(request, pk):
    title = request.data
    query = Category.objects.get(_id=pk)
    if query is not None:        
        serializer = CategorySerializer(query, title, partial=True)
        if serializer.is_valid():
            serializer.save()    
            return Response(serializer.data)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   
    else: 
        return Response('Category not found', status=status.HTTP_404_NOT_FOUND) 




@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteCategory(request, pk):
    category = Category.objects.get(_id=pk)
    if category is not None:
        category.delete()
        return Response('Category deleted successfully')
    else: 
        return Response('Category not found', status=status.HTTP_404_NOT_FOUND) 

    
    
@api_view(['GET'])
def getProducts(request):
    query = request.query_params.get('keyword')
    if query == None:
        query = ''
        
    products = Product.objects.filter(name__icontains=query)
    
    page = request.query_params.get('page')
    paginator = Paginator(products, 5)
    
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
        
        
    if page == None:
        page = 1
    
    page = int(page)
    
    serializer = ProductSerializer(products, many=True)
    return Response({'products':serializer.data, 'page':page, 'pages':paginator.num_pages})


@api_view(['GET'])
def getTopProducts(request):
    product = Product.objects.filter(rating__gte=4).order_by('-rating')[0:5]
    serializer = ProductSerializer(product, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def getProduct(request, pk):
    product = Product.objects.get(_id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAdminUser])
def createProduct(request):
    user = request.user
    product = Product.objects.create(
        user = user,
        name = 'sample Name',
        price = 0,
        brand = 'sample Brand',
        countInStock = 0,
        category = 'sample Category',
        description = ''
    )    

    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAdminUser])
def updateProduct(request, pk):
    data = request.data
    product = Product.objects.get(_id=pk)
    
    product.name = data['name']
    product.price = data['price']
    product.brand = data['brand']
    product.countInStock = data['countInStock']
    product.category = data['category']
    product.description = data['description']
    
    product.save()
    
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def deleteProduct(request, pk):
    product = Product.objects.get(_id=pk)
    product.delete()
    return Response('Product deleted successfully')






@api_view(['POST'])
@permission_classes([IsAdminUser])
def uploadImage(request):
    data = request.data
    
    product_id = data['product_id']
    product = Product.objects.get(_id=product_id)
    
    product.image = request.FILES.get['image']
    product.save()
    return Response('Product uploaded successfully')





@api_view(['POST'])
@permission_classes([IsAuthenticated])  
def createdProductReview(request, pk):
    user = request.user
    product = Product.objects.get(_id=pk)
    data = request.data
    
    # (1) Review already exists
    alreadyExists = product.review_set.filter(user=user).exists()
    
    if alreadyExists:
        content = {'detail': 'Review already exists'}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)
    
    # (2) No rating or 0
    elif data['rating'] == 0: 
        content = {'detail': 'please select a rating'}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)
    
    # (3) create a Review
    else:
        review = Review.objects.create(
            user = user,
            product = product,
            name = data['name'],
            rating = data['rating'],
            comment = data['comment']
        )
    
    reviews = product.review_set.all()
    product.numReviews = len(reviews)

    total = 0
    for i in reviews:
        total += i.rating
    
    product.rating = total/len(reviews)
    product.save()
    
    return Response('Review Added ')
