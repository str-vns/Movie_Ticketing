from fastapi import HTTPException

def emailValidation(email_user):
    if email_user:
       raise HTTPException(
        status_code=400,
        detail="Email already registered"
    )
       
def ExistingUserValidation(existing_user, type):
    if not existing_user and type == "DE":
        raise HTTPException(
            status_code=400,
            detail="Payment doesn't Exist"
        )
    elif existing_user and type == "D": 
        raise HTTPException(
            status_code=400,
            detail="Payment does Exist"
        )

def paymentOpValidation(pay_user, type):
   
    if not pay_user and type == "DE":
        raise HTTPException(
            status_code=400,
            detail="Payment doesn't Exist"
        )
    elif pay_user and type == "D": 
        raise HTTPException(
            status_code=400,
            detail="Payment does Exist"
        )

