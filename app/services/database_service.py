from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import desc


class DataBase:

    def __init__(self, flask_app, param):
        self.__db_user = param.get('user')
        self.__db_pwd = param.get('password')
        self.__db_host = param.get('host')
        self.__db_port = param.get('port')
        self.__db_name = param.get('database')
        self.__table_name = param.get('table')
        flask_app.config[
            'SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{self.__db_user}:{self.__db_pwd}@{self.__db_host}:{self.__db_port}/{self.__db_name}'
        flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.__db = SQLAlchemy(flask_app)
        self.__base = automap_base()
        self.__base.prepare(self.__db.engine, reflect=True)
        self.__ibm = self.__base.classes.ibm
        self.__col_names = [col.name for col in self.__base.metadata.tables["ibm"].c]
        self.__current_id = self.get_last_id()

    def get_by_gender(self, gender):
        return self.__db.session.query(self.__ibm).filter_by(gender=gender)

    def get_all(self):
        return self.__db.session.query(self.__ibm).all()

    def get_by_id(self, id):
        return self.__db.session.query(self.__ibm).filter(self.__ibm.id == id).first()

    def delete_by_id(self, id):
        record = self.get_by_id(id)
        if record:
            self.__db.session.query(self.__ibm).filter_by(id=id).delete()
            self.__db.session.commit()
            return True
        else:
            return False

    def insert(self, data):
        new_record = self.__ibm()
        new_record.id = self.__current_id + 1
        new_record.age = data['age']
        new_record.attrition = data['attrition']
        new_record.business_travel = data['business_travel']
        new_record.daily_rate = data['daily_rate']
        new_record.distance_from_home = data['distance_from_home']
        new_record.education = data['education']
        new_record.education_field = data['education_field']
        self.__db.session.add(new_record)
        self.__db.session.commit()
        self.__current_id = self.__current_id + 1
        return new_record.id

    def get_col_names(self):
        return self.__col_names

    def get_last_id(self):
        last_id = self.__db.session.query(self.__ibm.id).order_by(desc(self.__ibm.id)).limit(1).all()[0][0]
        return last_id
