from typing import Any
from dataclasses import dataclass
from pydantic import BaseModel

@dataclass
class EmployeeModel(BaseModel):
    EMP_ID : int = None
    EMP_USERNAME: str = None
    EMP_PASSWORD: str = None
    EMP_ROLE: str = None
    EMP_NAME: str = None
    EMP_NATIONAL_ID: str = None
    EMP_DOB: str = None
    EMP_GENDER: str = None
    EMP_NATIONAL: str = None
    EMP_ADDRESS: str = None
    EMP_EMAIL: str = None
    EMP_PHONE: str = None
    EMP_JOB_TITLE: str = None
    EMP_DEPARTMENT: str = None
    EMP_TYPE: str = None
    EMP_JOIN_DATE: str = None
    EMP_PIC: str = None 
    EMP_STATUS: str = None

    @staticmethod
    def fc_EmployeeModel(obj: Any) -> "EmployeeModel":
        _EMP_ID = int(obj.get("EMP_ID"))
        _EMP_USERNAME = str(obj.get("EMP_USERNAME"))
        _EMP_PASSWORD = str(obj.get("EMP_PASSWORD"))
        _EMP_ROLE = str(obj.get("EMP_ROLE"))
        _EMP_NAME = str(obj.get("EMP_NAME"))
        _EMP_NATIONAL_ID = str(obj.get("EMP_NATIONAL_ID"))
        _EMP_DOB = str(obj.get("EMP_DOB"))
        _EMP_GENDER = str(obj.get("EMP_GENDER"))
        _EMP_NATIONAL = str(obj.get("EMP_NATIONAL"))
        _EMP_ADDRESS = str(obj.get("EMP_ADDRESS"))
        _EMP_EMAIL = str(obj.get("EMP_EMAIL"))
        _EMP_PHONE = str(obj.get("EMP_PHONE"))
        _EMP_JOB_TITLE = str(obj.get("EMP_JOB_TITLE"))
        _EMP_DEPARTMENT = str(obj.get("EMP_DEPARTMENT"))
        _EMP_TYPE = str(obj.get("EMP_TYPE"))
        _EMP_JOIN_DATE = str(obj.get("EMP_JOIN_DATE"))
        _EMP_PIC = str(obj.get("EMP_PIC"))
        _EMP_STATUS = str(obj.get("EMP_STATUS"))

        return EmployeeModel