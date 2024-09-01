import os
import httpx
from fastapi import APIRouter, Request, Response, HTTPException
from fastapi.responses import RedirectResponse, JSONResponse
from dotenv import load_dotenv
from .jw_tokens import sign_tokens
from .register_user import register_user

load_dotenv()
router = APIRouter()

@router.get('/')
async def discord_auth(request: Request, response: Response):
    client_id = f'client_id={os.getenv('dscrd_client_id')}'
    redirect_uri = f'redirect_uri={os.getenv('dscrd_redirect_uri')}'
    url = f"https://discord.com/oauth2/authorize?{client_id}&response_type=code&{redirect_uri}&scope=email%20identify"
    print(url)
    return RedirectResponse(url)

@router.get('/redirect')
async def discord_auth(request: Request, response: Response):
    data = {
        'client_id': os.getenv('dscrd_client_id'),
        'client_secret': os.getenv('dscrd_client_secret'),
        'redirect_uri': os.getenv('dscrd_redirect_uri'),
        'code': request.query_params.get("code"),
        'grant_type': 'authorization_code'
    }
    async with httpx.AsyncClient() as client:
        token_response = await client.post("https://discord.com/api/v10/oauth2/token", data=data)
        if token_response.status_code != 200:
            print(token_response)
            return HTTPException(status_code=400, content={"error": "Failed to retrieve access token"})
        token_data = token_response.json()
        user_info_response = await client.get(
            f"https://discord.com/api/v10/users/@me",
            headers = {
                'Authorization': f"Bearer { token_data.get('access_token') }"
            }
        )
        if user_info_response.status_code != 200:
            return HTTPException(status_code=400, content={"error": "Failed to retrieve user info"})
    user_info = user_info_response.json()
    # return user_info
    email = user_info.get('email')
    name = user_info.get('global_name')
    username = user_info.get('username')
    avatar = f'https://cdn.discordapp.com/avatars/{user_info.get('id')}/{user_info.get('avatar')}?size=256'
    user = await register_user(email, name, name, username, avatar)
    access_token, refresh_token = sign_tokens(user)
    response.set_cookie(key='access_token', value=access_token, httponly=True)
    response.set_cookie(key='refresh_token', value=refresh_token, httponly=True)
    return user