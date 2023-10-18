from datetime import datetime
from pydantic import BaseModel, Field, field_validator, model_validator


class CustomerLogin(BaseModel):
    email: str = Field(title="Email", min_length=5, max_length=60,
                       pattern="^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$")
    password: str = Field(title="Password", min_length=8, max_length=50, pattern="^[a-zA-Z0-9]+$")


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


class CustomerToken(Customer):
    """
    Body Customer Token with data
    """
    auth_token: str
    refresh_token: str


class HireVehicle(BaseModel):
    customer_id: int = Field(title="Customer ID")
    vehicle_id: int = Field(title="Vehicle ID")
    pickup_date: datetime.date = Field(title="Pickup Date")
    return_date: datetime.date = Field(title="Return Date")
    amount: float = Field(title="Amount")  # present price

    @model_validator(mode='after')
    def check_passwords_match(self) -> 'HireVehicle':
        pickup_date = datetime.strptime(self.pickup_date, "%Y-%m-%d")
        return_date = datetime.strptime(self.return_date, "%Y-%m-%d")
        if return_date < pickup_date:
            raise ValueError('Invalid Period')
        if abs((return_date - pickup_date).days > 7):
            raise ValueError('Period Denied')
        return self
