from taxii2client.v20 import Server, Collection
from stix2 import TAXIICollectionSource, Filter
import urllib3

urllib3.disable_warnings() #band aid to avoid warning spam in the output for as long as TLS band-aid exists
#assigns server internet locations to variables
TAXII_mitre_srv = Server("https://cti-taxii.mitre.org/taxii/", user = 'invalid', password = 'fixme', verify = False) #band-aid; need to implement proper TLS for production version
#variable for easier access to root of API
TAXII_api_root = TAXII_mitre_srv.api_roots[0]
#example function of the API
for collection in TAXII_api_root.collections:
    print(collection.title + ": " + collection.id)

