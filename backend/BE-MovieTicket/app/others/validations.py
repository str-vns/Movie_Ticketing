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

def ExsistingMoviesValidation(existing_movie, type):
    
    if not existing_movie and type == "DE":
        raise HTTPException(
            status_code=400,
            detail="Movies doesn't exist"
        )
        
    elif existing_movie and type == "D":
        raise HTTPException(
            status_code=400,
            detail="Movies does Exist"
        )
        
def ExsistingCinemasValidation(existing_cinema, type):
    
    if not existing_cinema and type == "DE":
        raise HTTPException(
            status_code=400,
            detail="Cinemas doesn't exist"
        )
        
    elif existing_cinema and type == "D":
        raise HTTPException(
            status_code=400,
            detail="Cinemas does exist"
        )

def ExsistingSchedMovieValidation(existing_sched, type):
    
    if not existing_sched and type == "DE":
        raise HTTPException(
            status_code=400,
            detail="Movie Schedule doesn't exist"
        )
        
    elif existing_sched and type == "D":
        raise HTTPException(
            status_code=400,
            detail="Movie Schedule does exist"
        )
            
def ExsistingRoomsValidation(existing_sched, type):
    
    if not existing_sched and type == "DE":
        raise HTTPException(
            status_code=400,
            detail="Movie Schedule doesn't exist"
        )
        
    elif existing_sched and type == "D":
        raise HTTPException(
            status_code=400,
            detail="Movie Schedule does exist"
        )    