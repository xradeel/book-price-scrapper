from .tasks import readings

llist = [
    'https://readings.com.pk/category/level4/1834/A',
    'https://readings.com.pk/category/level1/21/A',
    'https://readings.com.pk/category/level1/41/A',
    'https://readings.com.pk/category/level1/20/A',
    'https://readings.com.pk/category/level1/60/A',
    'https://readings.com.pk/category/level1/57/A',
]

for r_url in llist:
    readings.delay(r_url)