import os
import requests
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict
from dotenv import load_dotenv

load_dotenv()

# client_id = "fzRHVgebnWqa3C2URcN8"
# client_secret = "4BQTFDBiYI"
# redirect_uri = "http://localhost:5173/naverLoginAPI"

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
redirect_uri = os.getenv("REDIRECT_URI")

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class RegisterData(BaseModel):
    name: str
    email: str
    birthday: str
    birthyear: str
    gender: str
    mobile: str
    password: str

class LoginData(BaseModel):
    email: str
    password: str

user_data: Dict[str, RegisterData] = {}
print(user_data)
@app.post("/login")
async def login(data: LoginData):
    # 이메일 확인
    if data.email not in user_data:
        raise HTTPException(status_code=404, detail="User not found.")
    
    # 비밀번호 확인
    user = user_data[data.email]
    if user.password != data.password:
        raise HTTPException(status_code=401, detail="Invalid password.")
    
    # 성공적으로 로그인된 사용자 정보 반환
    return {
        "message": "Login successful!",
        "user": {
            "name": user.name,
            "email": user.email,
            "birthday": user.birthday,
            "birthyear": user.birthyear,
            "gender": user.gender,
            "mobile": user.mobile,
        }
    }


@app.post("/register")
async def register(data: RegisterData):
    # 이메일 중복 확인
    if data.email in user_data:
        raise HTTPException(status_code=400, detail="Email already exists.")

    # 데이터 저장
    user_data[data.email] = data

    # 로그 출력
    print(f"Current users: {user_data}")

    # 성공 응답
    return {"message": "Registration successful!", "user": data}

@app.get("/callback")
async def callback(code: str):
    token_url = "https://nid.naver.com/oauth2.0/token"
    params = {
        "grant_type": "authorization_code",
        "client_id": client_id,
        "client_secret": client_secret,
        "redirect_uri": redirect_uri,
        "code": code
    }

    token_response = requests.get(token_url, params=params)
    token_json = token_response.json()
    
    if token_response.status_code == 200:
        access_token = token_json["access_token"]

        profile_url = "https://openapi.naver.com/v1/nid/me"
        profile_response = requests.get(
            profile_url,
            headers={"Authorization": f"Bearer {access_token}"}
        )

        print(profile_response)

        try:
            profile_data = profile_response.json()
            print(f"Profile Data: {profile_data}")
        except ValueError as e:
            print(f"Failed to decode JSON: {e}")
        
        if profile_response.status_code == 200:
            return JSONResponse(content=profile_response.json())
        else:
            return JSONResponse(content={"error": "Failed to fetch profile"}, status_code=profile_response.status_code)
    else:
        return JSONResponse(content={"error": "Failed to fetch access token"}, status_code=token_response.status_code)
