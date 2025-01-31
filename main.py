from fastapi import FastAPI
from server.database.index import engine
from server.database.models.user import Base
# from server.routes.auth import router as auth_router

from server.routes.auth.register import router as register_router
from server.routes.auth.login import router as login_router

from server.routes.questions.index import router as question_router
from fastapi.middleware.cors import CORSMiddleware

# Initialize FastAPI App
app = FastAPI()

# Create Database Tables
Base.metadata.create_all(bind=engine)

# Register Routes
app.include_router(register_router)
app.include_router(login_router)
app.include_router(question_router)

@app.get("/")
def root():
    """
    Root API Endpoint.
    """
    return {"message": "Welcome to the Quiz API"}

# Enable CORS (Allowing Frontend to Access API)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to your frontend URL for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    
)
