import requests
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse

class OPAMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, opa_url: str):
        super().__init__(app)
        self.opa_url = opa_url 

    async def dispatch(self, request: Request, call_next):
        type = request.headers.get("type")
        role = request.headers.get("role")

# OPAs input data        
        input_data = {
            "user": {"role":role,"type" :type},  
            "method": request.method,
            "path": request.url.path 
        }
        # print(f"input",input_data)
# sending query to OPA
        response = requests.post(
            f"{self.opa_url}/v1/data/authenticate/allow",
            json={"input": input_data}
        )
        # print(f"res",response)

#OPAs response
        if response.status_code == 200:
            opa_response = response.json()  
            if "result" in opa_response:
                result = opa_response.get("result",False)
                print(f"res",result)
                if result: 
                    response = await call_next(request)
                    return response
                else:
                    return JSONResponse(status_code=403,content={"detail":"Acess Denied"})
        else:
            return JSONResponse(status_code=403,content={"detail":"Acess Denied"})