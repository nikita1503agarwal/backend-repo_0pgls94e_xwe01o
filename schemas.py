"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogs" collection
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List

# Example schemas (replace with your own):

class User(BaseModel):
    """
    Users collection schema
    Collection name: "user" (lowercase of class name)
    """
    name: str = Field(..., description="Full name")
    email: str = Field(..., description="Email address")
    address: str = Field(..., description="Address")
    age: Optional[int] = Field(None, ge=0, le=120, description="Age in years")
    is_active: bool = Field(True, description="Whether user is active")

class Product(BaseModel):
    """
    Products collection schema
    Collection name: "product" (lowercase of class name)
    """
    title: str = Field(..., description="Product title")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., ge=0, description="Price in dollars")
    category: str = Field(..., description="Product category")
    in_stock: bool = Field(True, description="Whether product is in stock")

# Bolhuis Kwekerij specific schemas

class Inquiry(BaseModel):
    """
    Customer inquiry/quote request
    Collection name: "inquiry"
    """
    name: str = Field(..., description="Naam van de klant")
    email: EmailStr = Field(..., description="E-mailadres")
    phone: Optional[str] = Field(None, description="Telefoonnummer")
    tree_type: str = Field(..., description="Type kerstboom")
    size: str = Field(..., description="Gewenste maat (cm)")
    quantity: int = Field(1, ge=1, description="Aantal")
    message: Optional[str] = Field(None, description="Opmerkingen of vragen")
    newsletter_opt_in: bool = Field(False, description="Aanmelden voor nieuwsbrief")

class TreeProduct(BaseModel):
    """
    Catalogus item voor kerstbomen
    Collection name: "treeproduct" (not persisted by default, but available if needed)
    """
    name: str
    description: Optional[str] = None
    sizes: List[str] = []
    price_from: Optional[float] = None
    sku: Optional[str] = None
