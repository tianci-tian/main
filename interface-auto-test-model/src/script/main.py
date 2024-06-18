import requests,json

response = requests.request(
    method='GET',
    url='https://dppop.linksfield.net/prod-api/core/profileQuery/list',
    headers={
        "Authorization":"Bearer eyJhbGciOiJIUzUxMiJ9.eyJPcGVuLUlkIjpudWxsLCJVbmlvbi1JZCI6bnVsbCwidXNlcl9pZCI6MTYyLCJzdXJuYW1lIjoidGlhbiIsIk9wZW4tbmFtZSI6InRpYW5jaSIsInVzZXJfa2V5IjoiZjE5NzE4NDktMWY1Yy00N2JlLTg2ZjItOGM3ZTIxYzBhYTBlIiwidXNlcm5hbWUiOiJ0aWFuY2kudGlhbkBsaW5rc2ZpZWxkLm5ldCIsIlVzZXItSWQiOm51bGx9.0BfoZRMPYZrtzxutJAbm_gf2PuQyCT6IPZw_ZWLjGSUsSpXGeRWwg16bw6L2Qro172nCiQiSElzdeJ3BBd66mw"
    },
    params='blurry=89820221125200009898'
    )
#将响应内容解析为 JSON，并禁用 ASCII 编码
response_json = response.json()
response_str = json.dumps(response_json, indent=4, ensure_ascii=False)
print(response_str)