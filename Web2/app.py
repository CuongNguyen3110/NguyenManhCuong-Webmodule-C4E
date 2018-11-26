import mlab
from movie import Movie
from resource import Resource
from random import randint

from faker import Faker

faker = Faker()

mlab.connect()

movie_list = Movie.objects()

# m = Movie.objects().with_id("5bf80156e7179a56e215531a")
# print(m.title)
# m.delete()

# for m in movie_list:
#     print(m.title)
#     print(m.image)
#     print(m.year)

# resource_list = Resource.objects()

# r = Resource.objects().with_id("5bf7ffe90dfd061ae040a0dc")
# if r is None:
#     print("Not Found")
# else:
#     print("Found")
#     r.delete()

# r = Resource.objects()[0]
# r.delete()

# for r in resource_list:
#     print(r.name, r.city, r.yob, r.height, r.weight, sep=" ")

# m = Movie(title="Batman", year=2005, image="https://www.dccomics.com/sites/default/files/GalleryChar_1920x1080_BM_Cv38_54b5d0d1ada864.04916624.jpg")
# m.save()

# r = Resource(name="Nguyen Quang Huy", city="Phú Thọ", yob=1989, height=172, weight=90)
# r.save()

# for _ in range(100):
#     name = faker.name()
#     city = faker.state()
#     yob = randint(1953, 2000)
#     height = randint(150, 200)
#     weight = randint(40,100)
#     r = Resource(name=name, city=city, yob=yob, height=height, weight=weight)
#     r.save()

# records = Resource.objects(name="Katherine Lopez")
# print(len(records))
# for r in records:
#     print(r.city)
#     print(r.weight)
#     print(r.height)

# records = Resource.objects(height__gt=170, name__icontains="John")
# print(len(records))

# records = Resource.objects()

# for r in records:
#     r.update(set__available=False)

r = Resource.objects().with_id("5bf80cd00dfd061ad83fe7b3")
r.update(set__available=True)