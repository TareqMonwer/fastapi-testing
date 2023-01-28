from app.db.dependencies import get_db_session
from app.web.application import get_app
from app.web.lifetime import _setup_db
from behave import given, when, then, step
from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine


app = get_app()
_setup_db(app)
client = TestClient(app)


@given('the web server is running')
def step_impl(context):
    pass

@when('requesting for endpoint {endpoint_function}')
def step_impl(context, endpoint_function):
    print(">>>>> ")
    
    url = app.url_path_for(endpoint_function)
    print(url)
    response = client.get(url)
    context.response = response

@then('a 200 status code should be received')
def step_impl(context):
    assert context.response.status_code == 200

