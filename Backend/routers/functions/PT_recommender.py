import os

from fastapi import APIRouter, Depends, FastAPI
from sqlalchemy.orm import Session

from models import PT_recommender
from models.PT_recommender import UserInfo

from database import database

app = FastAPI()

# Configure API router
router = APIRouter(
    tags=['functions'],
)
app.include_router(router)

# Configure metadata
NAME = os.path.basename(__file__)[:-3]

# Dependency to get DB session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


###############################################
#                   Actions                   #
###############################################

@router.post(f'/func/{NAME}')
async def call_PT_recommender(model: PT_recommender.InputModel, db: Session = Depends(get_db)) -> PT_recommender.OutputModel:
    # Find data from database to recommend users
    algo = db.query(UserInfo).filter(UserInfo.region_i == model.region)
    algo_count = db.query(UserInfo).filter(UserInfo.region_i == model.region).count()
    algo_num = db.query(UserInfo).filter(UserInfo.interest_i < model.interest).count()
    
    # Output string with DB data
    if algo_count >= 3:
        if algo_count-algo_num >= 3:
            algo = db.query(UserInfo).filter(UserInfo.region_i == model.region).order_by(UserInfo.interest_i).offset(algo_num).limit(1)
            result1 = ' '.join(f"id: {i.id}/name: {i.name_i}/age: {i.age_i}/interest: {i.interest_i}" for i in algo)
            algo = db.query(UserInfo).filter(UserInfo.region_i == model.region).order_by(UserInfo.interest_i).offset(algo_num+1).limit(1)
            result2 = ' '.join(f"id: {i.id}/name: {i.name_i}/age: {i.age_i}/interest: {i.interest_i}" for i in algo)
            algo = db.query(UserInfo).filter(UserInfo.region_i == model.region).order_by(UserInfo.interest_i).offset(algo_num+2).limit(1)
            result3 = ' '.join(f"id: {i.id}/name: {i.name_i}/age: {i.age_i}/interest: {i.interest_i}" for i in algo)
        else:
            algo = db.query(UserInfo).filter(UserInfo.region_i == model.region).order_by(UserInfo.interest_i).offset(algo_count-3).limit(1)
            result1 = ' '.join(f"id: {i.id}/name: {i.name_i}/age: {i.age_i}/interest: {i.interest_i}" for i in algo)
            algo = db.query(UserInfo).filter(UserInfo.region_i == model.region).order_by(UserInfo.interest_i).offset(algo_count-2).limit(1)
            result2 = ' '.join(f"id: {i.id}/name: {i.name_i}/age: {i.age_i}/interest: {i.interest_i}" for i in algo)
            algo = db.query(UserInfo).filter(UserInfo.region_i == model.region).order_by(UserInfo.interest_i).offset(algo_count-1).limit(1)
            result3 = ' '.join(f"id: {i.id}/name: {i.name_i}/age: {i.age_i}/interest: {i.interest_i}" for i in algo)
    else:
        result1 = "Users are not enough for this region."
        result2 = "We need more than 3 users in same region."
        result3 = "Sorry for our inconvenience."

    # Input data to DB
    user_info = UserInfo(name_i=model.name, age_i=model.age, interest_i=model.interest, region_i=model.region)
    db.add(user_info)
    db.commit()

    return PT_recommender.OutputModel(output1=result1,output2=result2,output3=result3)
