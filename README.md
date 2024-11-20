FastAPI ABAC Application with OPA

This application is a FastAPI-based API that uses Attribute-Based Access Control (ABAC) policies enforced by an Open Policy Agent (OPA) server. Policies are defined in the policy.rego file and can be updated dynamically without restarting the FastAPI server.

Installation
Install fastapi and uvicorn : pip install fastapi uvicorn
Install OPA dependencies (you can interact with OPA via HTTP API) : pip install requests
Download the OPA binary from the official website : https://www.openpolicyagent.org/docs/latest/#running-opa
Start OPA as a server with the -watch-policy option so it auto-reloads policy changes: opa run --server --watch-policy
To starts OPA in server mode, auto-reloads policies on changes, and provides detailed debugging logs for real-time policy testing and troubleshooting : opa run --server --watch --log-level debug 

Starlette is a lightweight ASGI (Asynchronous Server Gateway Interface) framework that provides tools for building asynchronous web applications and services.Starlette provides the response type called the  JSONResponse to return different kinds of HTTP responses.

Running the api : run uvicorn api:app --reload
Running the Policy.rego : opa run --server --watch {path\to\policy.rego}