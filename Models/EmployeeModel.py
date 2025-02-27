from typing import Any
from dataclasses import dataclass
from pydantic import BaseModel

@dataclass
class EmployeeModel(BaseModel):
    EMP_ID : str = None
    EMP_PASSWORD : str = None
    EMP_ROLE : str = None
    EMP_DEPARTMENT : str = None
    EMP_POSITION : str = None
    EMP_NAME : str = None
    EMP_GENDER : str = None
    EMP_BIRTHDATE : str = None
    EMP_ADDRESS : str = None
    EMP_PHONE : str = None
    EMP_EMAIL : str = None
    EMP_STATUS : str = None

    @staticmethod
    def fc_EmployeeModel(obj: Any) -> "EmployeeModel":
        _EMP_ID = str(obj.get("EMP_ID"))
        _EMP_PASSWORD = str(obj.get("EMP_PASSWORD"))
        _EMP_ROLE = str(obj.get("EMP_ROLE"))
        _EMP_DEPARTMENT = str(obj.get("EMP_DEPARTMENT"))
        _EMP_POSITION = str(obj.get("EMP_POSITION"))
        _EMP_NAME = str(obj.get("EMP_NAME"))
        _EMP_GENDER = str(obj.get("EMP_GENDER"))
        _EMP_BIRTHDATE = str(obj.get("EMP_BIRTHDATE"))
        _EMP_ADDRESS = str(obj.get("EMP_ADDRESS"))
        _EMP_PHONE = str(obj.get("EMP_PHONE"))
        _EMP_EMAIL = str(obj.get("EMP_EMAIL"))
        _EMP_STATUS = str(obj.get("EMP_STATUS"))