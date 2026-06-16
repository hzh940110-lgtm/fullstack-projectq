from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import get_db
from models import Item

router = APIRouter()


class ItemCreate(BaseModel):
    title: str
    description: str
    price: float
    user_id: int


class ItemResponse(BaseModel):
    id: int
    title: str
    description: str
    price: float
    user_id: int

    class Config:
        from_attributes = True


@router.get("/", response_model=list[ItemResponse])
def get_items(db: Session = Depends(get_db)):
    """获取所有商品"""
    items = db.query(Item).all()
    return items


@router.get("/{item_id}", response_model=ItemResponse)
def get_item(item_id: int, db: Session = Depends(get_db)):
    """获取单个商品"""
    item = db.query(Item).filter(Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="商品不存在")
    return item


@router.post("/", response_model=ItemResponse)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    """创建商品"""
    db_item = Item(
        title=item.title,
        description=item.description,
        price=item.price,
        user_id=item.user_id
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


@router.put("/{item_id}", response_model=ItemResponse)
def update_item(item_id: int, item: ItemCreate, db: Session = Depends(get_db)):
    """更新商品"""
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="商品不存在")

    db_item.title = item.title
    db_item.description = item.description
    db_item.price = item.price
    db_item.user_id = item.user_id

    db.commit()
    db.refresh(db_item)
    return db_item


@router.delete("/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    """删除商品"""
    item = db.query(Item).filter(Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="商品不存在")

    db.delete(item)
    db.commit()
    return {"message": "删除成功"}
