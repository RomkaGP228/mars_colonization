from data.db_session import create_session, global_init
from data.users import User
from data.jobs import Jobs

db_name = input()
global_init(db_name)
db_sess = create_session()
jobs = db_sess.query(Jobs).all()
colonists = db_sess.query(User).all()
for colonist in colonists:
    if colonist.address == 'module_1' and colonist.age < 21:
        colonist.address = 'module_3'
        db_sess.commit()
