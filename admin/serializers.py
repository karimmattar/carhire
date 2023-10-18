from pydantic import BaseModel, Field, field_validator
from werkzeug.security import generate_password_hash


class Customer(BaseModel):
    """
    Body Customer data
    """
    ssn: str = Field(title="SSN", min_length=9, max_length=20, pattern="^\\d{3}-\\d{2}-\\d{4}$")
    first_name: str = Field(title="First Name", min_length=2, max_length=50, pattern="^[a-zA-Z]+$")
    last_name: str = Field(title="Last Name", min_length=2, max_length=50, pattern="^[a-zA-Z]+$")
    email: str = Field(title="Email", min_length=5, max_length=60,
                       pattern="^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$")
    mobile_phone: str = Field(title="Mobile Phone", min_length=10, max_length=20, pattern="^\\d{10}$")
    status: str = Field(title="Status", min_length=2, max_length=50, pattern="^[a-zA-Z]+$", default="initial")
    country: str = Field(title="Country", min_length=2, max_length=50, pattern="^[a-zA-Z]+$")

    @field_validator('status')
    @classmethod
    def validate_status(cls, value):
        """
        Validate status
        :param value: input value
        :return: value
        """
        if value not in ['initial', 'pending', 'hired']:
            raise ValueError("status must be either initial, active or inactive")
        return value


class CustomerCreate(Customer):
    """
    Body Customer Create
    """
    password: str = Field(title="Password", min_length=8, max_length=50, pattern="^[a-zA-Z0-9]+$")

    @field_validator('password')
    @classmethod
    def hashed_password(cls, value):
        """
        Hash password
        :param value: password plain text
        :return: hashed password
        """
        return generate_password_hash(value)


class RetrieveCustomer(Customer):
    """
    Query Customer data
    """
    id: int
