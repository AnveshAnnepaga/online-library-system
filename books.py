from supabase_client import supabase

def add_book(title: str, author: str, category: str, stock: int = 1):
    res = supabase.table("books").insert({
        "title": title,
        "author": author,
        "category": category,
        "stock": stock
    }).execute()
    print(res.data)

def update_book(book_id: int, title=None, author=None, category=None, stock=None):
    data = {}
    if title: data["title"] = title
    if author: data["author"] = author
    if category: data["category"] = category
    if stock is not None: data["stock"] = stock
    res = supabase.table("books").update(data).eq("book_id", book_id).execute()
    print(res.data)

def delete_book(book_id: int):
    borrowed = supabase.table("borrow_records").select("*").eq("book_id", book_id).is_("return_date", None).execute()
    if borrowed.data:
        print("Cannot delete: Book is currently borrowed.")
        return
    res = supabase.table("books").delete().eq("book_id", book_id).execute()
    print("Deleted:", res.data)

def list_books():
    books = supabase.table("books").select("*").execute()
    for b in books.data:
        borrowed_count = supabase.table("borrow_records").select("*").eq("book_id", b["book_id"]).is_("return_date", None).execute()
        available = b["stock"] - len(borrowed_count.data)
        print(f'{b["book_id"]}: {b["title"]} by {b["author"]} | Stock: {b["stock"]} | Available: {available}')

def search_books(keyword):
    books = supabase.table("books").select("*").ilike("title", f"%{keyword}%").execute()
    for b in books.data:
        print(b)
    
