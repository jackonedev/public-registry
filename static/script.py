from js import document
import json
from pyodide.http import pyfetch
from pyodide import create_proxy


async def make_request(url, method, body=None, headers=None):
    default_headers = {
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Type': 'multipart/form-data',
    }
    
    if headers:
        default_headers.update(headers)

    response = await pyfetch(
        url=url,
        method=method,
        body=body,
        headers=default_headers
    )

    return await response.json()

async def get_onclick(e):
    data = await make_request(url='/api/v1/person/1/', method='GET')
    # data = await make_request(url='/app/get/', method='GET')
    # return data.json()

    ul = document.getElementById('list')
    # li = document.createElement('li')


    for element in data:
        li = document.createElement('li')
        li.textContent = element['first_name']
        li.innerHTML = element
        ul.appendChild(li)

    # ul.appendChild(li)



def main():
    
    button = document.getElementById('button')
    button.addEventListener('click', create_proxy(get_onclick))

main()