import requests
import struct

# url = 'https://ns-oss.hushijie.com.cn/customer_926/qiniuo_1cvihf2nficj1glmucf4e1c82i.mp4'
# r = requests.get(url, stream=True)
# print(r.iter_content(chunk_size=512))
# for data in r.iter_content(chunk_size=512):
#     # print(111)
#     if data.find(b'mvhd') > 0:
#         index = data.find(b'mvhd') + 4
#
#         time_scale = struct.unpack('>I', data[index + 13:index + 13 + 4])
#         durations = struct.unpack('>I', data[index + 13 + 4:index + 13 + 4 + 4])
#         duration = durations[0] / time_scale[0]
#         print(duration)
#         break
    # if len(data) != 10:
    #     continue


print(len("BhncQUt2DbE="))
import base64
b = base64.b64decode(b"BhncQUt2DbE==")
print(b)
a = base64.b64encode(b'a840528')
print(a)
print(len(a))


import base64

s = base64.b64encode('a840528'.encode('utf-8'))
print(s)
d = base64.b64decode(s).decode('utf-8')
print(d)

s = base64.urlsafe_b64encode('a840528'.encode('utf-8'))
print(s)
print(len(s))
d = base64.urlsafe_b64decode(s).decode('utf-8')
print(d)
