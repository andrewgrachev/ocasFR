from django.http import JsonResponse
from FR.models import wtpersons
from FR.models import wtpersonenters
from FR.models import wtpersonimages


class Persons(object):
    def persons(self):
        res = []
        for i in wtpersons.objects.filter().all():
            persons_i = {
                'id': i.id,
                'name': i.name,
                'folder': i.folder
            }

            res.append(persons_i)
        return JsonResponse(res, safe=False)


class PersonEnters(object):
    def Penters(self):
        res = []
        for n in wtpersonenters.objects.filter().all():
            enters_n = {
                'person_id': n.person_id,
                'date': n.date,
                'id': n.id
            }

            res.append(enters_n)
        return JsonResponse(res, safe=False)

class PersonImages(object):
    def images(self):
        res = []
        for d in wtpersonimages.objects.filter(person_id=502).all():
            images_d = {
                'person_id': d.person_id,
                'image_name': d.image_name,
                'date': d.date,
                'id': d.id
            }

            res.append(images_d)
        return JsonResponse(res, safe=False)
