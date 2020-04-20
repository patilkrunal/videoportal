import os

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

print(EMAIL_ADDRESS)
print(EMAIL_PASSWORD)