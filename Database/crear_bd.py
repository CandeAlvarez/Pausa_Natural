from __future__ import print_function
import sqlalchemy as sa
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_mixins import ActiveRecordMixin, ReprMixin, ModelNotFoundError, AllFeaturesMixin

'''
lst_basicos = ['Lechuga','Zanahoria','Rúcula','Tomate','Cherry','Remolacha','Choclo','Brócoli','Repollo','Pepino','Semillas','Apio','Cebolla','Verdeo']        
lst_adicionales = ['Huevo','Palta','Lentejas','Pollo','Queso','Arroz Blanco','Arroz Integral','Quinoa','Fideos','Croutons','Kanikama','Cuscus','Nueces','Trigo']
'''
hash_basicos = {
    'Lechuga': False,
    'Zanahoria': False,
    'Rúcula': False,
    'Tomate': False,
    'Cherry': False,
    'Remolacha': False,
    'Choclo': True,
    'Brócoli': True,
    'Repollo': False,
    'Pepino': False,
    'Semillas': False,
    'Apio': False,
    'Cebolla': False,
    'Verdeo': False,
}

hash_adicionales = {
    'Huevo': True,
    'Palta': False,
    'Lentejas': True,
    'Pollo': True,
    'Queso': False,
    'Arroz Blanco': True,
    'Arroz Integral': True,
    'Quinoa': True,
    'Fideos': True,
    'Croutons': True,
    'Kanikama': False,
    'Cuscus': True,
    'Nueces': False,
    'Trigo': True,
}

lst_cubiertos = ['Completo','Sólo Cubiertos','Sólo Aderezos','Especial','No']

Base = declarative_base()


class BaseModel(Base, ActiveRecordMixin, ReprMixin):
    __abstract__ = True
    __repr__ = ReprMixin.__repr__
    pass

class Cliente(BaseModel):
    __tablename__ = 'cliente'
    alias = sa.Column(sa.String, primary_key=True)    
    nombre = sa.Column(sa.String,nullable=False)
    apellido = sa.Column(sa.String,nullable=False)
    direccion = sa.Column(sa.String)
    telefono = sa.Column(sa.String)
    cubiertos = sa.Column(sa.String)
    pedidos = sa.orm.relationship('Pedido',cascade="all, delete-orphan")
    #Por la relacion many-to-one entre Pedido y Cliente
    id_cubierto = sa.Column(sa.String, sa.ForeignKey('cubierto.nombre'),nullable=False)
    cubierto = sa.orm.relationship('Cubierto')


class Asociacion (BaseModel):
    __tablename__ = 'asociacion'
    extend_existing = True
    ingrediente = sa.Column('id_ingrediente', sa.String,  sa.ForeignKey('ingrediente.nombre'), primary_key=True)
    pedido = sa.Column('id_pedido', sa.Integer,  sa.ForeignKey('pedido.id'), primary_key=True)
    cantidad = sa.Column(sa.Integer)

association_table = sa.Table(
    'asociacion', Base.metadata,
    sa.Column('id_ingrediente', sa.String, sa.ForeignKey('ingrediente.nombre'), primary_key=True),
    sa.Column('id_pedido', sa.Integer, sa.ForeignKey('pedido.id'), primary_key=True),
    extend_existing=True
)

class Cubierto(BaseModel):
    __tablename__ = 'cubierto'
    nombre = sa.Column(sa.String, primary_key=True)
    

class Ingrediente(BaseModel):
    __tablename__ = 'ingrediente'
    nombre = sa.Column(sa.String, primary_key=True)
    cocido = sa.Column(sa.Boolean, nullable = False)
    basico = sa.Column(sa.Boolean, nullable = False)
    
class Pedido(BaseModel):
    __tablename__ = 'pedido'
    
    id = sa.Column(sa.Integer, primary_key=True) 
    fecha = sa.Column(sa.String,nullable=False)
    #Por la relacion many-to-one entre Pedido y Cliente
    id_cliente = sa.Column(sa.String,
                           sa.ForeignKey('cliente.alias'),nullable=False)
    cliente = sa.orm.relationship('Cliente')
    #Por la relacion many-to-many entre Pedido e Ingrediente
    ingredientes = sa.orm.relationship('Ingrediente',secondary=association_table)
    asociaciones = sa.orm.relationship('Asociacion',cascade="all, delete-orphan")
    precio = sa.Column(sa.Integer)
###################

#To create the db    
engine = sa.create_engine('sqlite:///Database/bd_pausa_natural.sqlite')
session = scoped_session(sessionmaker(bind=engine, autocommit=True))

Base.metadata.create_all(engine)
BaseModel.set_session(session)


for c in lst_cubiertos:
    if Cubierto.find(c) is None:
        Cubierto.create(nombre=c)

for ing in hash_basicos.keys():
    if Ingrediente.find(ing) is None:
            Ingrediente.create(nombre=ing,cocido=hash_basicos[ing],basico=True)

for ing in hash_adicionales.keys():
    if Ingrediente.find(ing) is None:
        Ingrediente.create(nombre=ing,cocido=hash_adicionales[ing],basico=False)

