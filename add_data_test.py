from db import session
from models.explos_model import Explos
from models.hostage_model import Hostage

# {
# "email": "jeremy37@example.org",
# "username": "jonesalejandra",
# "ip_address": "215.67.111.124",
# "created_at": "2024-10-15T05:29:13.450066",
# "location": {
# "latitude": 8.5478895,
# "longitude": -135.24204,
# "city": "Port Josephburgh",
# "country": "PA"
# },
# "device_info": {
# "browser": "Mozilla/5.0",
# "os": "iOS",
# "device_id": "c4a3ce0d-4f4f-4bc9-9e94-b135e32cfe81"
# },
# "sentences": [
# "Public quickly explos hear sing.",
# "Difference nothing environmental shake decide.",
# "Natural southern what nice."
# ]
# }
# def add_data():
#     new_Hos = Hostage(email="jeremy37@example.org",username="dsfv",
#                       ip_address="215.67.111.124",created_at="2015-",
#                       latitude=12.02,longitude=452.01,city="sv,",
#                       country="wcwcs",browser="ugb",os="cwee",device_id="cdcdc",sentences="chascnancasn naison isni snisOI")
#
#     session.add(new_Hos)
#     session.commit()
def add_data1():
    new_Hos = Explos(email="jeremy37@example.org",username="dsfv",
                      ip_address="215.67.111.124",created_at="2015-",
                      latitude=12.02,longitude=452.01,city="sv,",
                      country="wcwcs",browser="ugb",os="cwee",device_id="cdcdc",sentences="chascnancasn naison isni snisOI")

    session.add(new_Hos)
    session.commit()
