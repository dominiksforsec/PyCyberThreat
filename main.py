from stix2 import TAXIICollectionSource
from taxii2client.v20 import Server

server = Server("https://cti-taxii.mitre.org/taxii/", user = 'fk off', password= 'againfkoff', verify=False)
api_root = server.api_roots[0]

for collection in api_root.collections:
    print(collection.title + ": " + collection.id)

