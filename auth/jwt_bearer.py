from fastapi import Request, HTTPException
from fastapi.securtiy import HTTPBearer, HTTPAuthorizationCredentials

class jwtBearer(HTTPBearer):
    def __init__(self, auto_Error : bool = True):
        super(jwtBearer, self).__init__(auto_Error=auto_Error)
