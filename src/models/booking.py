import pandas as pd
from sqlalchemy import create_engine, Column, Integer, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Leer el archivo CSV
csv_path = 'path/to/your/tourism_data_carnival.csv'
df = pd.read_csv(csv_path)


# Configuración de la base de datos
DATABASE_URI = 'postgresql+psycopg2://postgres:Carlos.2020#@localhost:5432/hakaton'


# Crear una conexión con la base de datos
engine = create_engine(DATABASE_URI)
Base = declarative_base()

# Definir la tabla
class TourismData(Base):
    __tablename__ = 'tourism_data'
    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(Date, nullable=False)
    place = Column(String, nullable=False)
    type = Column(String, nullable=False)
    occupancy_rate = Column(Float, nullable=False)
    tourist_count = Column(Integer, nullable=False)

# Crear la tabla en la base de datos
Base.metadata.create_all(engine)

# Crear una sesión
Session = sessionmaker(bind=engine)
session = Session()

# Insertar datos en la base de datos
for index, row in df.iterrows():
    tourism_data = TourismData(
        date=row['date'],
        place=row['place'],
        type=row['type'],
        occupancy_rate=row['occupancy_rate'],
        tourist_count=row['tourist_count']
    )
    session.add(tourism_data)

# Confirmar las transacciones
session.commit()

# Cerrar la sesión
session.close()