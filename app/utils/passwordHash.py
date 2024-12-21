# Description: This file contains functions to hash a password and verify if a provided password matches the hashed password.
import bcrypt

# Function to hash a password
def hash_password(password: str) -> str:
  
    # Generate a salt
    salt = bcrypt.gensalt()
    # Hash the password with the salt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    # Return the hashed password as a string
    return hashed_password.decode('utf-8')

# Function to verify if the provided password matches the hashed password
def verify_password(plain_password: str, hashed_password: str) -> bool:
    
    # Check if the hash of the plain password matches the hashed password
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))
