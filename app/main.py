from fastapi import FastAPI
from routers.UserRoleRouter import router as user_role_router

app = FastAPI()


app.include_router(user_role_router)


