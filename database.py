# IMPORTS
from sqlalchemy import create_engine, String, Integer, Column, DateTime, func
from sqlalchemy.orm import sessionmaker, declarative_base, scoped_session
from sqlalchemy.exc import SQLAlchemyError
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

# CONEXÃO
engine = create_engine('mysql+pymysql://root:senaisp@localhost:3306/empresa_db')

# SESSÃO
db_session = scoped_session(sessionmaker(bind=engine))

# BASE
Base = declarative_base()
Base.query = db_session.query_property()


# ======================
# TABELA USUARIO
# ======================
class Usuario(Base, UserMixin):
    __tablename__ = 'usuario'

    id = Column(Integer, primary_key=True)
    nome = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    senha = Column(String(255), nullable=False)
    criado_em = Column(DateTime, server_default=func.now())

    # REPRESENTAÇÃO
    def __repr__(self):
        return f'<Usuario {self.nome}>'

    # CRIPTOGRAFAR SENHA
    def set_password(self, password):
        self.senha = generate_password_hash(password)

    # VERIFICAR SENHA
    def check_password(self, password):
        return check_password_hash(self.senha, password)

    # SALVAR NO BANCO
    def save(self):
        try:
            db_session.add(self)
            db_session.commit()
        except SQLAlchemyError:
            db_session.rollback()
            raise


# ======================
# TABELA FUNCIONARIO
# ======================
class Funcionario(Base):
    __tablename__ = 'funcionarios'

    id = Column(Integer, primary_key=True)
    nome = Column(String(255), nullable=False)
    data_nascimento = Column(String(20), nullable=False)
    cpf = Column(String(14), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    senha = Column(String(255), nullable=False)
    cargo = Column(String(100), nullable=False)
    salario = Column(String(50), nullable=False)
    criado_em = Column(DateTime, server_default=func.now())

    def __repr__(self):
        return f'<Funcionario {self.nome}>'

    def save(self):
        try:
            db_session.add(self)
            db_session.commit()
        except Exception as e:
            db_session.rollback()
            raise e

    def delete(self):
        try:
            db_session.delete(self)
            db_session.commit()
        except Exception as e:
            db_session.rollback()
            raise e


# CRIAR TABELAS
if __name__ == "__main__":
    Base.metadata.create_all(engine)