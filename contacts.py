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

def view_contacts():
    if not phonebook:
        print("Danh bạ trống.")
    else:
        for i, contact in enumerate(phonebook, start=1):
            print(f"{i}. {contact['name']} - {contact['phone']}")
