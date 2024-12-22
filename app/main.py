from fastapi import FastAPI
from routers.UserRoleRouter import router as user_role_router
from routers.UserRouter import router as user_router
from routers.OrderRouter import router as order_router
from config.database import Base, engine
import uvicorn


app = FastAPI()


app.include_router(user_role_router)
app.include_router(user_router)
app.include_router(order_router)



# Create tables if running directly
if __name__ == "__main__":
    # Create all tables
    print("Creating tables if they do not exist...")
    Base.metadata.create_all(bind=engine)

    # Start the FastAPI application
    uvicorn.run(app, host="127.0.0.1", port=8000)


