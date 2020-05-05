import requests
url = 'https://sdd-pdf.s3.amazonaws.com/report-pdfs/2017/e5f90a2e5ff5ccce0ebe9e77e8935468.pdf?AWSAccessKeyId=AKIAJZQ4KYD2D35QKCDA&Expires=1588455906&Signature=hf6sPUH%2Fbq0qlYLarKNAiQDX%2Fjw%3D'
myfile = requests.get(url)
open('sample.pdf', 'wb').write(myfile.content)