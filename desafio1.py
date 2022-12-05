from sqlalchemy.orm import declarative_base, Session
from sqlalchemy.orm import relationship
from sqlalchemy import Column, create_engine, inspect, select, func
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import ForeignKey

Base = declarative_base()

class Cliente(Base):
    __tablename__= "tbl_client"
    id = Column(Integer, primary_key = True)
    name= Column(String)
    cpf = Column(String)
    address = Column(String)

    conta= relationship(
        "Conta", back_populates="conta_id", cascade="all, delete-orphan"
    )


    def __repr__(self):
        return f"Nome = {self.name} - {self.cpf}, {self.address}"


class Conta(Base):
    __tablename__= "tbl_contas"
    id= Column(Integer, primary_key = True)
    agencia=  Column (String)
    tipo = Column(String)
    saldo = Column(Float)
    numero = Column(Integer, ForeignKey("tbl_client.id"))

    conta_id = relationship(
        "Cliente", back_populates="conta")


    def __repr__(self):
        return f"Agencia ={self.agencia}, Tipo + {self.tipo}, Saldo = {self.saldo} - Numero_cliente:{self.numero}"


print(Cliente.__tablename__)
print(Conta.__tablename__)


engine = create_engine("sqlite://")
Base.metadata.create_all(engine)
inspetor_engine = inspect(engine)

print(inspetor_engine.get_table_names())
print(inspetor_engine.default_schema_name)


with Session(engine) as session:
    fernanda = Cliente(
        name ="fernanda",
        cpf = "cpf",
        address =" meu endereco",
        conta =[Conta(
            agencia="001",
            tipo = "PF",
            saldo = 20.2

        )]

    )
    maria = Cliente(
        name="maria",
        cpf="22222222222",
        address=" meu endereco2222",
        conta=[Conta(
            agencia="001",
            tipo="PF",
            saldo=50.0

        )]

    )
session.add_all([fernanda,maria])
session.commit()

order_stmt= select(Conta).order_by(Conta.id)

for result in session.scalars(order_stmt):
    print(result)

stmt_join= select(Cliente.name, Cliente.cpf).join_from(Conta, Cliente)
for result in session.scalars(stmt_join):
    print(result)
