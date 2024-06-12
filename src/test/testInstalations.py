try:
    import sqlalchemy
    import psycopg2
    import pandas as pd
    import numpy as np
    from sqlalchemy import create_engine
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import sessionmaker

    print("Todas las bibliotecas se han instalado correctamente.")
except ImportError as e:
    print(f"Error al importar una biblioteca: {e}")
