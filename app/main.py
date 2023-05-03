from fastapi import FastAPI
from controllers import student_controller, subject_controller
from config import Base, engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(student_controller.router)
app.include_router(subject_controller.router)
