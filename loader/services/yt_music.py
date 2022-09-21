from pprint import pprint

from django.conf import settings
from ytmusicapi import YTMusic


headers = """accept: */*
accept-encoding: gzip, deflate, br
accept-language: en-US,en;q=0.9
authorization: SAPISIDHASH 1663712898_1c12f162c91d3619c42691137b7929db6a6251f3
content-length: 2022
content-type: application/json
cookie: YSC=5leaW4Yem94; VISITOR_INFO1_LIVE=UDzsS_wA2OI; _gcl_au=1.1.1669640293.1663712883; _ga=GA1.1.613641027.1663712884; SID=Owg-uPdK8lsgFzOBeQ8e1PnPpTc9mB1XyBlP6DANhds0r_9G3wtEs9Ljg172NZ9p23CMbg.; __Secure-1PSID=Owg-uPdK8lsgFzOBeQ8e1PnPpTc9mB1XyBlP6DANhds0r_9GM9dteENqqzFg-AiKNN6N3g.; __Secure-3PSID=Owg-uPdK8lsgFzOBeQ8e1PnPpTc9mB1XyBlP6DANhds0r_9GGQuKmy3FYjNcA1hDO3j8mw.; HSID=AuHOlSQ0kKMOhshWT; SSID=AK-2WBXkut4xJaASx; APISID=1AH3XoOUb5h99PRS/AHj4H9Zaw3vf_H8gt; SAPISID=s7UvnUFOY7xp2oIZ/AXGV1I1yCtdba0FTK; __Secure-1PAPISID=s7UvnUFOY7xp2oIZ/AXGV1I1yCtdba0FTK; __Secure-3PAPISID=s7UvnUFOY7xp2oIZ/AXGV1I1yCtdba0FTK; LOGIN_INFO=AFmmF2swRQIgIIHFbBm3KHbutfD2h_CW5KK0XjteCuK2nKuaj0SrIikCIQCC1JcvTFcWt2wcvrzy7v-TyrZ0oTEH0dz5g7G0d-p8WA:QUQ3MjNmeWxRMllPazlCNU5DVnFNV0Q5eURtNC03TUxmQ1NBWXpnSVNkUnFHd1JBMzJkaTE0UUUxd3hVbFRuM3FWeUNadjhSMGF0ZlFTMGx2ZzNLZkl1bXVUN1ZqOG9YTU9DSTNtSXhzYmVKdDFMVEg1Ulg3TGFKZG43RF95UXdFX1poVzliTk9sb1hlVmFlcjU1NG5rUWhRTzFINjc1STRB; _ga_VCGEPY40VB=GS1.1.1663712884.1.1.1663712896.0.0.0; SIDCC=AEf-XMQHV9eVXhS-yadsA0SJJKSCDOWx5L4MhXILpmNhJmQfCqZeMKH6VVKu9AnZycTDfgJ-; __Secure-1PSIDCC=AEf-XMRsyAscs89Az0RhfpC75S-HT79ZoN3RLKSUQDYCcO_DJoZxlMeueWwLe8lU-zy4PWhQ; __Secure-3PSIDCC=AEf-XMROHLAPGOOuX2TwuCWEMCf9upUyf50zE7A8_dqDi_rbRbF29Catn4i7IWmMFXP4u-VfBg
origin: https://music.youtube.com
referer: https://music.youtube.com/
sec-ch-ua: "Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"
sec-ch-ua-arch: "x86"
sec-ch-ua-bitness: "64"
sec-ch-ua-full-version: "105.0.5195.125"
sec-ch-ua-full-version-list: "Google Chrome";v="105.0.5195.125", "Not)A;Brand";v="8.0.0.0", "Chromium";v="105.0.5195.125"
sec-ch-ua-mobile: ?0
sec-ch-ua-model
sec-ch-ua-platform: "Linux"
sec-ch-ua-platform-version: "5.19.1"
sec-ch-ua-wow64: ?0
sec-fetch-dest: empty
sec-fetch-mode: same-origin
sec-fetch-site: same-origin
user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36
x-client-data: CJe2yQEIpLbJAQipncoBCMP7ygEIlqHLAQi0vMwBCP+8zAEIqsbMAQjWxswBCLvJzAEI4svMAQif0cwBCP/VzAEI/tfMAQiL2MwBCMzdzAE=
Decoded:
message ClientVariations {
  // Active client experiment variation IDs.
  repeated int32 variation_id = [3300119, 3300132, 3313321, 3325379, 3330198, 3350068, 3350143, 3351338, 3351382, 3351739, 3352034, 3352735, 3353343, 3353598, 3353611, 3354316];
}
x-goog-authuser: 0
x-goog-visitor-id: CgtVRHpzU193QTJPSSiA_aiZBg%3D%3D
x-origin: https://music.youtube.com
x-youtube-client-name: 67
x-youtube-client-version: 1.20220914.01.00"""


def _setup() -> YTMusic:
    ytmusic = YTMusic()
    ytmusic.setup(
        filepath=str(settings.ROOT_DIR / "headers_auth.json"), headers_raw=headers
    )
    return ytmusic


def search(name: str, filter=None):
    ytmusic = _setup()
    s = ytmusic.search(name, filter=filter)
    return s

