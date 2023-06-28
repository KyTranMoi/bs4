import json
from googletrans import Translator

# Đường dẫn đến tệp JSON
json_file_path = 'test (1).json'

# Đọc dữ liệu từ tệp JSON với mã hóa utf-8-sig
with open(json_file_path, 'r', encoding='utf-8-sig') as json_file:
    data = json.load(json_file)

# Khởi tạo đối tượng Translator
translator = Translator(service_urls=['translate.google.com'])

# Dịch nội dung và gán giá trị dịch vào trường "translated_content"
for item in data:
    content = item['content']
    translated = translator.translate(content, src='en', dest='vi')
    item['translated_content'] = translated.text

# Lưu dữ liệu đã dịch vào tệp JSON mới
translated_json_file_path = 'translated_test.json'
with open(translated_json_file_path, 'w', encoding='utf-8') as translated_json_file:
    json.dump(data, translated_json_file, ensure_ascii=False, indent=4)
