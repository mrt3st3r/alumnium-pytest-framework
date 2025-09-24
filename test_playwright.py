import pytest
from playwright.sync_api import sync_playwright
from alumnium import Alumni
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture(scope="function")
def al():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://duckduckgo.com")
    alumni = Alumni(page)
    yield alumni
    browser.close()
    playwright.stop()

def test_complete_all_todos(al):
    al.do("type 'selenium' into the search field, then press 'Enter'")
    al.check("page title contains selenium")
    al.check("search results contain selenium.dev")
    assert al.get("atomic number") == 34

