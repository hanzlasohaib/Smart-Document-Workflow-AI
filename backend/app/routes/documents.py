from fastapi import APIRouter

router = APIRouter(prefix="/documents", tags=["Documents"])

@router.get("/test")
def test_documents_route():
    return {"message": "Documents route working"}
