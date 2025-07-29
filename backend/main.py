# backend/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Importamos Base y engine para crear las tablas
from backend.db.session import engine
from backend.db.base import Base

# Importamos las rutas de autenticación
from backend.auth import routes as auth_routes

# Importamos las rutas de inventory
from backend.inventory import routes as inventory_routes
from backend.inventory.category import routes as category_routes

# Importamos modelos para registrar tablas en metadata
import backend.auth.models  # modelos auth (usuario, etc)
import backend.inventory.models  # modelos inventory (categories, components, etc)

# Creamos todas las tablas declaradas en Base
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Agente IA – Backend")

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # luego podés restringir
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir routers
app.include_router(auth_routes.router, prefix="/auth", tags=["auth"])
app.include_router(inventory_routes.router, prefix="/inventory", tags=["inventory"])
app.include_router(
    category_routes.router, prefix="/inventory/categories", tags=["inventory"]
)


# Ruta raíz opcional
@app.get("/")
def read_root():
    return {"msg": "API del Agente IA funcionando ✅"}
