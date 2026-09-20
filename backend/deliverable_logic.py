from fastapi import FastAPI

app = FastAPI()

@app.api_route('/health', methods=['GET', 'POST'])
def health():
    return {'status': 'ok'}
