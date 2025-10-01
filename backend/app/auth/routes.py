from fastapi import APIRouter, HTTPException
from app.db import supabase
from .schemas import UserCreate, UserLogin, UserResponse

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register", response_model=UserResponse)
def register(user: UserCreate):
    try:
        response = supabase.auth.sign_up({
            "email": user.email,
            "password": user.password,
            "options": {
                "data": {
                    "nome": user.nome
                }
            }
        })
        if not response.user:
            raise HTTPException(status_code=400, detail="Erro ao criar usuário.")

        if not response.session:
            raise HTTPException(
                status_code=400,
                detail="Usuário criado, mas precisa confirmar o email."
            )

        return UserResponse(access_token=response.session.access_token)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/login", response_model=UserResponse)
def login(user: UserLogin):
    try:
        response = supabase.auth.sign_in_with_password({
            "email": user.email,
            "password": user.password
        })

        if not response.session:
            raise HTTPException(status_code=400, detail="Não foi possível autenticar usuário.")

        return UserResponse(access_token=response.session.access_token)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
