from fastapi import APIRouter, Response, Request, Response
from fastapi.responses import JSONResponse
from google.protobuf.json_format import MessageToDict
from src.grpc.grpc_client import getUserById, updateUsername, updateEmail, updateFirstname, updateLastname
from src.grpc import user_pb2 as user_pb2

router = APIRouter()

@router.post('/username')
async def update_username(request: Request, response: Response):
    if not request.state.user_id:
        return Response(status_code=403, content='Forbidden')
    try:
        body = await request.json()
    except Exception as e:
        print(f'[Profile Router] Failed to parse body: {e}')
        return Response(status_code=400, content='Bad Request')
    if not body.get('username'):
        return Response(status_code=400, content='Bad Request')
    update, error = updateUsername(request.state.user_id, body.get('username'))
    if update is None:
        print('[Profile Router] update failed')
        return Response(status_code=400, content=f'Bad Request: {error.details()}')
    update = MessageToDict(update, preserving_proto_field_name=True)
    return update

@router.post('/email')
async def update_email(request: Request, response: Response):
    if not request.state.user_id:
        return Response(status_code=403, content='Forbidden')
    try:
        body = await request.json()
    except Exception as e:
        print(f'[Profile Router] Failed to parse body: {e}')
        return Response(status_code=400, content='Bad Request')
    if not body.get('email'):
        return Response(status_code=400, content='Bad Request')
    update, error = updateEmail(request.state.user_id, body.get('email'))
    if update is None:
        print('[Profile Router] update failed')
        return Response(status_code=400, content=f'Bad Request: {error.details()}')
    update = MessageToDict(update, preserving_proto_field_name=True)
    return update

@router.post('/first_name')
async def update_firstname(request: Request, response: Response):
    if not request.state.user_id:
        return Response(status_code=403, content='Forbidden')
    try:
        body = await request.json()
    except Exception as e:
        print(f'[Profile Router] Failed to parse body: {e}')
        return Response(status_code=400, content='Bad Request')
    if not body.get('first_name'):
        return Response(status_code=400, content='Bad Request')
    update, error = updateFirstname(request.state.user_id, body.get('first_name'))
    if update is None:
        print('[Profile Router] update failed')
        return Response(status_code=400, content=f'Bad Request: {error.details()}')
    update = MessageToDict(update, preserving_proto_field_name=True)
    return update

@router.post('/last_name')
async def update_lastname(request: Request, response: Response):
    if not request.state.user_id:
        return Response(status_code=403, content='Forbidden')
    try:
        body = await request.json()
    except Exception as e:
        print(f'[Profile Router] Failed to parse body: {e}')
        return Response(status_code=400, content='Bad Request')
    if not body.get('last_name'):
        return Response(status_code=400, content='Bad Request')
    update, error = updateLastname(request.state.user_id, body.get('last_name'))
    if update is None:
        print('[Profile Router] update failed')
        return Response(status_code=400, content=f'Bad Request: {error.details()}')
    update = MessageToDict(update, preserving_proto_field_name=True)
    return update

#TODO: Passwd and Avatar edit
# @router.post('/passwd')
# @router.post('/avatar')