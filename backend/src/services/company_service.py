from sqlalchemy.orm import Session
from src.schemas.company import CompanyCreate, CompanyUpdate
from src.repositories import company_repository

def create_company_service(db: Session, data: CompanyCreate):
    return company_repository.create_company(db, data)

def list_companies_service(db: Session):
    return company_repository.get_all_companies(db)

def get_company_service(db: Session, company_id: int):
    return company_repository.get_company_by_id(db, company_id)

def update_company_service(db: Session, company_id: int, data: CompanyUpdate):
    return company_repository.update_company(db, company_id, data)

def delete_company_service(db: Session, company_id: int):
    return company_repository.delete_company(db, company_id)
