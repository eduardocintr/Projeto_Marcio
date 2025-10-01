from fastapi import APIRouter, Depends
from app.auth.dependencies import get_current_user, require_role

router = APIRouter(prefix="/users", tags=["Users"])

# Qualquer usuário logado
@router.get("/me")
def me(user=Depends(get_current_user)):
    return {"email": user['user_metadata']["email"], "nome": user['user_metadata']["nome"]}
