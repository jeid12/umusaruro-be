from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.UserRoleRouter import router as user_role_router
from routers.UserRouter import router as user_router
from routers.OrderRouter import router as order_router
from routers.SubscriptionRouter import router as subscription_router
from routers.warehouseRouter import router as warehouse_router
from routers.ProductRouter import router as product_router
from routers.OrderDetailsRouter import router as order_detail_router
from config.database import Base, engine
from dependencies.auth import router as auth_router
import os
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Enable CORS to allow cross-origin requests (change the origins based on your frontend settings)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this in production (use a specific domain instead of "*")
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(user_role_router)
app.include_router(user_router)
app.include_router(order_router)
app.include_router(subscription_router)
app.include_router(warehouse_router)
app.include_router(product_router)
app.include_router(order_detail_router)
app.include_router(auth_router)





# Dependency for getting the database
@app.on_event("startup")
def startup_event():
    print("App is starting up...")

@app.on_event("shutdown")
def shutdown_event():
    print("App is shutting down...")

if __name__ == "__main__":
    # Hard-code the port to 8080
    uvicorn.run(app, host="0.0.0.0", port=8080)




