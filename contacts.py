phonebook = []
def main():
    print("Chương trình danh bạ - Base setup OK")

if __name__ == "__main__":
    main()

def add_contact():
    name = input("Nhập tên: ")
    phone = input("Nhập số điện thoại: ")
    phonebook.append({'name': name, 'phone': phone})
    print("Đã thêm liên hệ.")
