from supabase_client import supabase
from datetime import datetime

def borrow_book(member_id: int, book_id: int):
    book = supabase.table("books").select("*").eq("book_id", book_id).single().execute().data
    borrowed_count = supabase.table("borrow_records").select("*").eq("book_id", book_id).is_("return_date", None).execute()
    available = book["stock"] - len(borrowed_count.data)
    if available <= 0:
        print("Book not available to borrow.")
        return
    res = supabase.table("borrow_records").insert({
        "member_id": member_id,
        "book_id": book_id
    }).execute()
    print("Borrowed:", res.data)

def return_book(record_id: int):
    res = supabase.table("borrow_records").update({
        "return_date": datetime.now().isoformat()
    }).eq("record_id", record_id).execute()
    print("Returned:", res.data)

def overdue_books():
    res = supabase.table("borrow_records").select("*").is_("return_date", None).execute()
    print("Overdue Books:")
    for r in res.data:
        print(r)
