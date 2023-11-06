import os
import sys
import pytest

sys.path.append('./src')

@pytest.fixture(autouse=True, scope="module")
def environment_vars():
    os.environ["docs_input_location"] = os.path.join(os.getcwd(), 'tests', 'stubs', 'doc.yaml')
    os.environ["docs_output_location"] = os.path.join(os.getcwd(), 'tests', 'stubs', 'output.yaml')
    os.environ["server_desc"] = "My library"
    os.environ["server_url"] = "https://fake-url.com/jarrodiscool"
    os.environ["info_version"] = "1.0.0"
    os.environ["info_title"] = "my fake project"
    os.environ["info_desc"] = "The API for fake Project 🧔"
    
