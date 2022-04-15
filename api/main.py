from fastapi_pagination import Page, add_pagination, paginate, LimitOffsetPage
from fastapi import FastAPI, Depends, Response, status, HTTPException
import models
import schemas
from database import engine, SessionLocal
from sqlalchemy.orm import Session
import logging


app = FastAPI()

models.Base.metadata.create_all(engine)


# dependency
def get_db():
    db = SessionLocal
    try:
        yield db
    finally:
        db.close()


# Creating Logging File
LOG_FORMAT = "%(levelname)s %(asctime)s - %(name)s - %(message)s"
logging.basicConfig(filename='/Users/akylbek/Desktop/development/DataOx/api/process.log', level=logging.DEBUG,
                    format=LOG_FORMAT)

logger = logging.getLogger()


# Create
@app.post('/fprints', status_code=201)
def create(request: schemas.Prints, db: Session = Depends(get_db)):
    new_fprint = models.Prints(key=request.key, author=request.author)
    db.add(new_fprint)
    db.commit()
    db.refresh(new_fprint)
    return new_fprint


# READ WITH PAGINATION
@app.get("/fprints", response_model=Page[schemas.Prints])
@app.get("/fprints/limit-offset", response_model=LimitOffsetPage[schemas.Prints])
def get_prints(db: Session = Depends(get_db)):
    logger.info('displaying factorio prints')
    return paginate(db.query(models.Prints).all())


add_pagination(app)

# READ WITH ID
@app.get('/fprints/{id}')
def show(id, response: Response, db: Session = Depends(get_db)):
    fprint = db.query(models.Prints).filter(
        models.Prints.id == id).first()  # in sqlalchemey we have comman filter operation so we use filter
    if not fprint:
        '''
        response.status_code = status.HTTP_404_NOT_FOUND
       return {"msg":f"blog with {id} is not available"}
       '''
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f'fprint with {id} is not available')
    return fprint


# DELETE
@app.delete('/fprints/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id, db: Session = Depends(get_db)):
    db.query(models.Prints).filter(models.Prints.id == id).delete(synchronize_session=False)  # documentation of sqlalchemy
    db.commit()
    return {'done': 'delete operation executed successfully'}


# PUT
@app.put('/fprints/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Prints, db: Session = Depends(get_db)):
    blog = db.query(models.Prints).filter(models.Prints.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'blog with {id} not found')
    blog.update(request.dict())  # need to use dict to edit parameters
    db.commit()
    return 'updated'
