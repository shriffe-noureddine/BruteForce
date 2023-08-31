import requests
import itertools
from itertools import islice
# Define the characters that can be used
characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

# Use itertools.product to generate all combinations
combinations = itertools.product(characters, repeat=4)

def is_valid_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True
        return False
    except requests.RequestException:
        return False


count = 356504
# Iterate through the combinations and print them
for combination in islice(combinations, count, None):
    combination_str = ''.join(combination)
    url = 'https://discord.com/api/v9/invites/hZTM' + \
        combination_str+'?with_counts=true&with_expiration=true'
    if is_valid_url(url):
        possible_target = 'https://discord.com/invite/'+combination_str
        with open('dis.txt', 'a') as file:
            file.write(possible_target + '\n')
    count += 1
    print(count)
