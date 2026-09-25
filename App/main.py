from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from .database import Base, engine, get_db
from .models import User
from .schemas import UserCreate, UserLogin, UserResponse
from .auth import hash_password, verify_password, create_access_token


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Arkhe API",
    description="API REST para la inmobiliaria Arkhe",
    version="1.0.0"
)


@app.get("/")
def inicio():
    return {
        "message": "API Arkhe funcionando correctamente"
    }


@app.post(
    "/api/auth/register",
    response_model=UserResponse
)
def register(
    user: UserCreate,
    db: Session = Depends(get_db)
):

    usuario_existente = db.query(User).filter(
        User.email == user.email
    ).first()

    if usuario_existente:
        raise HTTPException(
            status_code=400,
            detail="El correo ya está registrado"
        )

    nuevo_usuario = User(
        nombre=user.nombre,
        email=user.email,
        password=hash_password(user.password)
    )

    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)

    return nuevo_usuario


@app.post("/api/auth/login")
def login(
    user: UserLogin,
    db: Session = Depends(get_db)
):

    usuario = db.query(User).filter(
        User.email == user.email
    ).first()

    if not usuario:
        raise HTTPException(
            status_code=401,
            detail="Correo o contraseña incorrectos"
        )

    if not verify_password(
        user.password,
        usuario.password
    ):
        raise HTTPException(
            status_code=401,
            detail="Correo o contraseña incorrectos"
        )

    token = create_access_token({
        "sub": str(usuario.id),
        "email": usuario.email
    })

    return {
        "message": "Inicio de sesión exitoso",
        "access_token": token,
        "token_type": "bearer"
    }
