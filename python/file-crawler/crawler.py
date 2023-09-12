import requests
from bs4 import BeautifulSoup

url_list = [
    "http://mirrors.tencent.com/tlinux/2.4/tlinux/SRPMS/",
	"http://mirrors.tencent.com/tlinux/2.4/tlinux/debuginfo/i386/RPMS/",
	"http://mirrors.tencent.com/tlinux/2.4/tlinux/debuginfo/x86_64/RPMS/",
	"http://mirrors.tencent.com/tlinux/2.4/tlinux/i386/RPMS/",
	"http://mirrors.tencent.com/tlinux/2.4/tlinux/x86_64/RPMS/",
	"http://mirrors.tencent.com/tlinux/2.4/arm64/tlinux/aarch64/RPMS/",
	"http://mirrors.tencent.com/tlinux/2.4/arm64/tlinux/SRPMS/",
	"http://mirrors.tencent.com/tlinux/2.4/arm64/tlinux/debuginfo/aarch64/RPMS/",
	"http://mirrors.tencent.com/tlinux/3.1/Updates/SRPMS/",
	"http://mirrors.tencent.com/tlinux/3.1/Updates/aarch64/RPMS/",
	"http://mirrors.tencent.com/tlinux/3.1/Updates/aarch64/RPMS/kronosnet/",
	"http://mirrors.tencent.com/tlinux/3.1/Updates/debuginfo/aarch64/RPMS/",
	"http://mirrors.tencent.com/tlinux/3.1/Updates/debuginfo/x86_64/RPMS/",
	"http://mirrors.tencent.com/tlinux/3.1/Updates/x86_64/RPMS/",
	"http://mirrors.tencent.com/tlinux/3.1/Updates/x86_64/RPMS/kronosnet/",
	"http://mirrors.tencent.com/tlinux/3.1/TencentOS-AppStream/SRPMS/SPackages/",
	"http://mirrors.tencent.com/tlinux/3.1/TencentOS-AppStream/aarch64/Packages/",
	"http://mirrors.tencent.com/tlinux/3.1/TencentOS-AppStream/debuginfo/aarch64/Packages/",
	"http://mirrors.tencent.com/tlinux/3.1/TencentOS-AppStream/debuginfo/x86_64/Packages/",
	"http://mirrors.tencent.com/tlinux/3.1/TencentOS-AppStream/x86_64/Packages/"
]

for url in url_list:
    response = requests.get(url)
    html = response.content

    soup = BeautifulSoup(html, "html.parser")
    links = soup.find_all("a")

    count = 0
    for link in links:
        href = link.get("href")
        if href.endswith("/"):
            continue
        count += 1

    print("目录：", url, "，RPM包数量：", count)