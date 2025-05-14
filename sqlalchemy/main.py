from data import db_session
from data.users import User


session = db_session.create_session()

captain = User()
captain.surname = 'Scott'
captain.name = 'Ridley'
captain.age = 21
captain.position = 'captain'
captain.speciality = 'research engineer'
captain.address = 'module_1'
captain.email = 'scott_chief@flask.org'

ultramarine = User()
ultramarine.surname = 'Cage'
ultramarine.name = 'Tit'
ultramarine.age = 49
ultramarine.position = 'admiral'
ultramarine.speciality = 'research engineer'
ultramarine.address = 'module_3'
ultramarine.email = 'tit_ultramarine@flask.org'

kai = User()
kai.surname = 'Angel'
kai.name = 'Kai'
kai.age = 30
kai.position = 'Base'
kai.speciality = 'singer'
kai.address = 'module_2'
kai.email = 'kai_angel@flask.org'

mice = User()
mice.surname = 'mice'
mice.name = '9'
mice.age = 24
mice.position = 'younger captain'
mice.speciality = 'singer'
mice.address = 'module_4'
mice.email = '9mice@flask.org'

session.add(captain)
session.add(ultramarine)
session.add(kai)
session.add(mice)
session.commit()