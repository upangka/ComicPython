"""传统包使用演示

演示如何从嵌套的传统包中导入和使用模块。
"""

from sz_library.second_floor.section_x.row_three import book

if __name__ == "__main__":
    print("深圳图书馆北馆藏书列表：")
    print("─" * 50)
    # 创建更多书籍
    books = [
        book.Book("流畅的Python", "Luciano Ramalho", "978-7-115-45466-9"),
        book.Book("Python编程入门与实战", "Fabrizio Romano", "978-7-115-35363-4"),
        book.Book("Effective Python", "Brett Slatkin", "978-7-111-55802-2")
    ]

    for book in books:
        print(book)
