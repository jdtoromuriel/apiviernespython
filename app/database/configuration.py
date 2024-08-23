from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import Engine
 # Conexión a la DB

 #nombreDB
 #usuarioDB
 #ContraseñaUser
 #HostName
 #Port

dataBaseName = "gestionbd"
userName = "root"
userPassword = ""
hostname = "localhost"
connectionPort = "3306"

# Crear conexión

connectionToDataBase = f"mysql+mysqlconnector://{userName}:{userPassword}@{hostname}:{connectionPort}/{dataBaseName}"

engine = create_engine(connectionToDataBase)

sessionLocal = sessionmaker(autocommit=False, autoFlush=False, bind=engine)
