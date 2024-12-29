from fastapi import HTTPException, UploadFile
import cloudinary.uploader

def upload_file_to_cloudinary(file: UploadFile) -> str:
    """
    Uploads a file to Cloudinary and returns the secure URL.
    """
    try:
        result = cloudinary.uploader.upload(file.file)
        return result["secure_url"]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Cloudinary upload failed: {str(e)}")
