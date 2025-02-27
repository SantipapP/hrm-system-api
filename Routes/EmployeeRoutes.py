from fastapi import APIRouter, HTTPException
from Controllers.EmployeeController import EmployeeController
from Models.EmployeeModel import EmployeeModel
router = APIRouter(
    prefix="/Employee",
    tags=["Employee-Controller"],
)

@router.post("/AuthLogin")
def AuthLogin(EmpData : EmployeeModel):
    AuthResponse = EmployeeController.AuthLogin(EmpData)
    
    return AuthResponse