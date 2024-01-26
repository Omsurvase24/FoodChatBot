from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import JSONResponse

app = FastAPI()


@app.post("/")
async def handle_request(request: Request):
    payload = await request.json()

    intent = payload['queryResult']['intent']['displayName']
    parameters = payload['queryResult']['parameters']
    output_contexts = payload['queryResult']['outputContexts']

    if intent == "track.order - context: ongoing-tracking":
        track_order(parameters)


def track_order(parameters: dict):
    order_id = parameters['order_id']

    return JSONResponse(content={
        "fulfillmentText": f"Received =={intent}== in the backend"
    })
