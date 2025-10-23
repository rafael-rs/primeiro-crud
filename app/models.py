import os
import dotenv
from pydal import DAL, Field
from datetime import datetime
from zoneinfo import ZoneInfo

zone = ZoneInfo('America/Sao_Paulo')

dotenv.load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
db = DAL(DATABASE_URL)
table_users = db.define_table('usuarios',
                        Field('nome','string', length=120, notnull=True),
                        Field('email', 'string', length=120, notnull=True, unique=True),
                        Field('idade','integer', length=120, notnull=True),
                        Field('senha', 'string', length=255, notnull=True),
                        Field('criado_em', 'datetime', default= lambda: datetime.now(zone)),
                        Field('atualizado_em', 'datetime', update= lambda: datetime.now(zone)))
