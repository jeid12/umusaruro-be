from fastapi import FastAPI
from routers.UserRoleRouter import router as user_role_router

app = FastAPI()

# Include the User Role Router
app.include_router(user_role_router)

# You can add more routers for other modules here as well
