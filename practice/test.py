# 接收用户输入的原始文本
original_text = """-----BEGIN PGP MESSAGE-----
Version: BCPG v1.62

hIwDPYe2aQXQyfABA/47zkCdZW4GXNM74KxLTwUXwbOinTKElhE2aTKDRsnh7les
drT5Aw4Fj/3Uggt3pwJfBnibzPdvo57NwIvnwHmyVOrALaqsrlWzTfj22WptQzgZ
3GBdh/hlNL+Y1Aii73WfnySd0bKTUJo9OvwxRIE6hAF8SHOxRdjrWm2saO7u6dLB
IwHlz++CDMRns5v5Yo3TK3vcAiQekXrShvdlVXspK40LsXfZwD0Zm2HoagxNJCJe
T0u/Th49Is8XlsuPRi8LcZPnzOmv6BW9MsGsviSXUhJ9vxsVbFk6kyZ5ZvUHPuCl
sJVAFbG1uUanXS1cAO9I0ZsLpQsvqrsoc1IIp47o4b8ZyqmvQrdYpp0JJVortk5Y
BAO+9umqNhyjjxaKUUopBpvY1IhaxylpqoxaTXo9VXuxTAm+1GPCFe7/gM+2W0sF
LxJpC7ODgUjWbZMlMOgeTvbNfomNyMLJMN0+SnAqIeF2rHVQ7gJNyszIlPqCA9T8
vPJ9SWwLSPrZYG4WRBwQf3w0GDItYXnEmtxHFzRY/3ickdGm4w/QkYHyOUSyRbLZ
a4flJMqr9CG3irHnJD8ogCBO5JDAxKnOXxZM8eIBIRikBJMFszmNgoSxBAGIhkAE
cr9IUIX/grvr7cSTbLkloF+SEiT79mFKlXvLrcy5hqDr/oC4BjFQMuVW8leD0rPX
glmigJI8SNZlAHhJPfliu4gQo8BhdJJWJNVWQz+8+Che7TG3owXPRDjE/VlMD+Mp
bTLXQ3oJovXpBVtdPEK/EMnHz/sTnzAGiVEgcGtAi4Xe1ikWD33iseoBjpb7hPEO
MGZ0DQ==
=eMk+
-----END PGP MESSAGE-----
"""

# 将换行符替换为 \n
formatted_text = original_text.replace('\n', '\\n')

# 输出带有 \n 显示换行符的格式化文本
print("格式化后的文本：")
print(formatted_text)

