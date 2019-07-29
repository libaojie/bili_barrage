# log输出
LogPath = r"data/log"

# token
BaseUrl = "http://192.168.160.237:15011"
Token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NDQwNzk4NTAsImlhdCI6MTU0NDA3OTc5MCwiaXNzIjoia2VuIiwiZGF0YSI6eyJpZCI6IjdDNTM1QjUzMkIwNTExM0ZFMDUwMDA3RjAxMDA3N0EyIiwibG9naW5fdGltZSI6MTU0NDA3OTc5MH19.5AlHE6OgeEVDEOfdfWixi6Dqoe3pvjAjCNFOF7KnPrM"
Hearder = {
    "Authorization": f"Bearer {Token}",
    "Content-Type": "application/json"
}

# ExcelPath = "document/监测台.xlsx"
ExcelPath = r"C:\Users\li\Documents\01_Code\04_SVN\CertificationAuthority\03_SystemDesign\CA_02_认证中心清单.xlsx"
OutPath = r"../data/ca.sql"