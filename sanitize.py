import os

def sanitize_file(filepath):
    if not os.path.isfile(filepath):
        return
    
    print(f"Checking {filepath}...")
    with open(filepath, 'rb') as f:
        content = f.read()
    
    # 0xEF 0xBF 0xBD is the UTF-8 replacement character
    corrupted_sequence = b'\xef\xbf\xbd'
    
    if corrupted_sequence in content:
        count = content.count(corrupted_sequence)
        print(f"Found {count} corrupted characters in {filepath}. Removing them...")
        sanitized = content.replace(corrupted_sequence, b'')
        with open(filepath, 'wb') as f:
            f.write(sanitized)
        print(f"Successfully sanitized {filepath}.")
    else:
        print(f"No corruption found in {filepath}.")

files_to_check = [
    'index.html',
    'service-details.html',
    'service-data.js',
    'book-appointment.html',
    '404.html'
]

for filename in files_to_check:
    sanitize_file(filename)
