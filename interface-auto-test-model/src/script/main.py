import requests
import json

response = requests.request(
    method='POST',
    url='https://dppop.linksfield.net/prod-api/core/profileQuery/reset',
    headers={
        "Authorization": "Bearer eyJhbGciOiJIUzUxMiJ9.eyJPcGVuLUlkIjpudWxsLCJVbmlvbi1JZCI6bnVsbCwidXNlcl9pZCI6MTYyLCJzdXJuYW1lIjoidGlhbiIsIk9wZW4tbmFtZSI6InRpYW5jaSIsInVzZXJfa2V5IjoiZjYxY2NhYWQtOGRhMC00N2QzLWJlNDctMmJmMmIzMGU3YWI0IiwidXNlcm5hbWUiOiJ0aWFuY2kudGlhbkBsaW5rc2ZpZWxkLm5ldCIsIlVzZXItSWQiOm51bGx9.g9Xzf0bKrQbKpcLoxcFLFE2i8U3q2LuNgwsEJ4K_tdYKy6EQKktOQogof8yGhCnCI1ASiZAoCy6hGfNnPhDjeQ"
    },
    json={
        "iccids": [24020629000000000005],
        "isReserve": "0"
    }
)

response_json = response.json()
response_str = json.dumps(response_json, indent=4, ensure_ascii=False)
print(response_str)