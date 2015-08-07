from random import randint, sample
from requests import get


def gnaw_backend_resources(backend_resources):
    targetedResourcesCount = randint(0, len(backend_resources))
    print("Gnawwwing ", targetedResourcesCount, " resources.")
    targetedResources = sample(backend_resources,
                               targetedResourcesCount)
    for resource in targetedResources:
        print("GNAW:", resource)
        r = get('http://' + resource + '/off')
