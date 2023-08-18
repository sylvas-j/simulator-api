# model_simulator
for simulating models built

cd ../../users/sylvanus jerome/documents/python_scriptstopwordss/models_simulator

cd ~/Documents/things-n-thingses/python/web-stack/models_simulator_backend
nano models_simulator/settingss/production.py
nano git/models_simulator/models_simulator/settingss/production.py

docker logs -n 20 -f mod-sim-con-web
docker exec -it mod-sim-con-web bash


create dump file
docker exec some-mysql sh -c 'exec mysqldump --all-databases -uroot -p"$MYSQL_ROOT_PASSWORD"' > /some/path/on/your/host/all-databases.sql

retrieve data from dump file
$ docker exec -i some-mysql sh -c 'exec mysql -uroot -p"$MYSQL_ROOT_PASSWORD"' < /some/path/on/your/host/all-databases.sql


Debugging links
http://www.devarchive.org:8181/ nginx
http://www.devarchive.org:8282 gunicorn
http://www.devarchive.org:3307 mysql


Set environment variables
ENV POSTGRES_USER=<your-postgres-username>
ENV POSTGRES_PASSWORD=<your-postgres-password>
ENV POSTGRES_DB=<your-postgres-db-name>
ENV DJANGO_SETTINGS_MODULE=<your-django-settings-module>

Install PostgreSQL
RUN apt-get update && apt-get install -y postgresql postgresql-contrib

Create the database
RUN service postgresql start && \
    su postgres -c "psql -c \"CREATE DATABASE ${POSTGRES_DB};\"" && \
    service postgresql stop


- docker build -t mod-sim .
- docker run --name court -it ubuntu
- docker exec -it court bash


Then commit the changes to a new Docker image instance using the following command.
- docker commit -m "What you did to the image" -a "Author Name" container_id repository/new_image_name


#### Pushing Docker Images to a Docker Repository
- docker login -u docker-registry-username

Note: If your Docker registry username is different from the local username you used to create the image, you will have to tag your image with your registry username. For the example given in the last step, you would type:

- docker tag sammy/ubuntu-nodejs docker-registry-username/ubuntu-nodejs

- docker push docker-registry-username/docker-image-name


cd git/models_simulator
docker compose up


djangorestframework==3.12.4

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework.parsers import FormParser, FileUploadParser
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

import json
from django.utils import timezone
from django.core import serializers
from django.db.models import Q

from django.contrib.auth.models import User
from roomies_admin.models import Country, City
from post_ads.models import PostComponents, Components, Category, Reason, Area, PostImages, Post
from post_ads.serializers import PostImageSerializer
from users.models import UserDetails, ImageGalleryModel
# Create your views here.

def post_view(request):
    return render(request, 'post.html')

def post_display(request):
    return render(request, 'view-post.html')

def post_details(request):
    return render(request, 'post-detail.html')

def post_owner(request):
    return render(request, 'post-owner.html')

# def PostViewTest(request):
#         print('post')
#         if request.method == 'POST':
#             file = request.FILES.get('formm')
#             # print(data)
#             print(file)
#         else:
#             print('outiing')


class PostView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    
    def post(self, request):
        print('post')
        data = self.request.data
        images = self.request.data.getlist('images')
        components = self.request.data.getlist('coms')
        # print(data)
        # print(len(images))
        # taking care of other            

        try:
            cat= Category.objects.filter(id=data['cat']).get()
            cutr= Country.objects.filter(id=data['country']).get()
            reason= Reason.objects.filter(id=data['reason']).get()

            # Insert and get inserted id if com_other is set
            if 'com_other' in data.keys():
                coms = data['com_other'].strip(',').split(',')
                comss = []
                for com in coms:
                    com = Components.objects.create(name=com)
                    comss.append(com.id)
                components.extend(comss)
                components.remove('0')
                # print('components=>',components)

            # Insert and get inserted id if city_other is set        
            if 'city_other' in data.keys():
                city_other = data['city_other']
                city= City.objects.create(name=data['city_other'],country=cutr)
                # print('city_=>',city)
            else:
                city= City.objects.filter(id=data['city']).get()

            # Insert and get inserted id if area_other is set
            if 'area_other' in data.keys():
                # print('this is area')
                area_other = data['area_other']
                city= City.objects.filter(id=data['city']).get()
                cutr= Country.objects.filter(id=data['country']).get()
                area= Area.objects.create(area=data['area_other'],country=cutr, city=city)
                # print('area=>',area)
            else:
                area= Area.objects.filter(id=data['area']).get()


            post = Post.objects.create(
                user=request.user,
                area=area,
                category=cat,
                reason=reason,
                address=data['address'],
                description=data['description'],
                price=data['price'],
                negotiable=data['neg']
                )

            for com in components:
                com = Components.objects.filter(id=com).get()
                com = PostComponents.objects.create(post=post,components=com)

            for image in images:
                PostImages.objects.create(post=post, images=image)


            return Response(
                {'message': 'Post Successful!'},
                status=status.HTTP_201_CREATED
            )
        except:
            return Response(
                {'message': 'Something went wrong!'},
                status=status.HTTP_404_NOT_FOUND
            )


class PostComponentsView(APIView):
    def post(self, request):
        # print('post')
        data = self.request.data
        # print(data)
        if data['city_id'] != '' and data['country_id'] == '':
            data= Area.objects.filter(city=data['city_id']).values('id','area').order_by('area')
        else:
            data= City.objects.filter(country=data['country_id']).values('id','name').order_by('name')
        
        # print(data)
        return Response(
            {'message': 'Gotten','data':data},
            status=status.HTTP_201_CREATED
        )
        
    def get(self, request):
        # print('get')
        cat= Category.objects.all().order_by('name')
        com= Components.objects.all().order_by('name')
        country= Country.objects.all().order_by('name')
        reason= Reason.objects.all().order_by('name')

        cat = serializers.serialize('json', cat)
        com = serializers.serialize('json', com)
        country = serializers.serialize('json', country)
        reason = serializers.serialize('json', reason)
        # print(com)
        
        return Response(
            {'message': 'Gotten','cat':cat,'com':com,'country':country,'reason':reason},
            status=status.HTTP_201_CREATED
        )



class PostSearchView(APIView):
    def search_result(self, lookups):
        post_list=[]
        posts = Post.objects.filter(lookups).values(
            'id','area__area','user__first_name',
            'category__name','reason__name',
            'description','price',
            'negotiable').order_by('category__name')
        for post in posts:
            images= PostImages.objects.filter(post=post['id']).values('images')
            post_list.append([post,images])
        return post_list

    def post(self, request):
        data = self.request.data
        # print(data)
        # post_list=[] 
        if data['price'] and data['area'] and data['cat'] != '':
            # print('alllll')
            lookups= Q(price=data['price'],area__area__icontains=data['area'],category__name__icontains=data['cat'])
            post_list = PostSearchView.search_result(self,lookups)
            # queries = serializers.serialize('json', queries)
            return Response(post_list,status=status.HTTP_201_CREATED)
