from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.db.session import get_db
from src.schemas.company import CompanyCreate, CompanyUpdate, CompanyOut
from src.services import company_service
from typing import List

router = APIRouter(prefix="/companies", tags=["Companies"])

@router.post("/", response_model=CompanyOut)
def create_company(company: CompanyCreate, db: Session = Depends(get_db)):
    return company_service.create_company_service(db, company)

@router.get("/", response_model=List[CompanyOut])
def get_companies(db: Session = Depends(get_db)):
    return company_service.list_companies_service(db)

@router.get("/{company_id}", response_model=CompanyOut)
def get_company(company_id: int, db: Session = Depends(get_db)):
    company = company_service.get_company_service(db, company_id)
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")
    return company

@router.put("/{company_id}", response_model=CompanyOut)
def update_company(company_id: int, company: CompanyUpdate, db: Session = Depends(get_db)):
    updated = company_service.update_company_service(db, company_id, company)
    if not updated:
        raise HTTPException(status_code=404, detail="Company not found")
    return updated

@router.delete("/{company_id}")
def delete_company(company_id: int, db: Session = Depends(get_db)):
    deleted = company_service.delete_company_service(db, company_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Company not found")
    return {"message": "Company deleted successfully"}
