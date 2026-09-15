from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import strawberry
from strawberry.fastapi import GraphQLRouter

app = FastAPI(title="UBPD Mediación Pedagógica API")

# Configuración de CORS para desarrollo
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # En producción se limitará al dominio de Railway
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Esquema GraphQL base (MVP)
@strawberry.type
class Query:
    @strawberry.field
    def hola(self) -> str:
        return "¡Hola desde GraphQL para la UBPD! Todo listo para armar los grafos."

schema = strawberry.Schema(query=Query)
graphql_app = GraphQLRouter(schema)

# Inyectando GraphQL en FastAPI
app.include_router(graphql_app, prefix="/graphql")

@app.get("/")
def read_root():
    return {"mensaje": "API de UBPD funcionando. Ve a /graphql para interactuar."}    
// Transición a la puntuación correcta después de 5 segundos
document.addEventListener('DOMContentLoaded', () => {
    const rawText = document.getElementById('heroRawText');
    const punctuatedText = document.getElementById('heroPunctuatedText');

    if (rawText && punctuatedText) {
        setTimeout(() => {
            // Ocultar texto sin puntuación
            rawText.classList.remove('active');
            
            // Mostrar texto corregido tras un breve fade out
            setTimeout(() => {
                punctuatedText.classList.add('active');
            }, 500); 
        }, 2000);
    }
});