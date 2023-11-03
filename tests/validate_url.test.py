import yt_dlp_helper
from src import utils

valid_urls = [
    'https://www.youtube.com/watch?v=Ds1--Gl9u68',
    'https://youtu.be/Ds1--Gl9u68',
    'https://www.youtube.com/playlist?list=PLfu_Bpi_zcDNEKmR82hnbv9UxQ16nUBF7'
]
invalid_urls = [
    'https://google.com',
    'https://you.tube/I-am-something'
]

validate_error = 0
invalidate_error = 0

for i in valid_urls:
    if not yt_dlp_helper.validate_url(i):
        validate_error += 1

for i in invalid_urls:
    if yt_dlp_helper.validate_url(i):
        invalidate_error += 1

if invalidate_error or validate_error > 0:
    print(f'The test {utils.Color.red}failed!{utils.Color.reset}\nThere {validate_error} valid urls were perceived as '
          f'invalid and {invalidate_error}  invalid urls were perceived as valid')
else:
    print(f'All test completed {utils.Color.green}successfully{utils.Color.reset}')
