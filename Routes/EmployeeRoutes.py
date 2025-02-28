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
    if AuthResponse["status"] == 200:
        return AuthResponse
    else:
        raise HTTPException(status_code=AuthResponse["status"], detail=AuthResponse["message"])
    
@router.post("/FetchEmployee")
def FetchEmployee(EmpData : EmployeeModel):
    FetchResponse = EmployeeController.FetchEmployee(EmpData)
    if FetchResponse["status"] == 200:
        return FetchResponse
    else:
        raise HTTPException(status_code=FetchResponse["status"], detail=FetchResponse["message"])