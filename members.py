from supabase_client import supabase

def add_member(name: str, email: str):
    res = supabase.table("members").insert({"name": name, "email": email}).execute()
    print(res.data)

def update_member(member_id: int, name: str = None, email: str = None):
    data = {}
    if name: data["name"] = name
    if email: data["email"] = email
    res = supabase.table("members").update(data).eq("member_id", member_id).execute()
    print(res.data)

def delete_member(member_id: int):
    borrowed = supabase.table("borrow_records").select("*").eq("member_id", member_id).is_("return_date", None).execute()
    if borrowed.data:
        print("Cannot delete: Member has borrowed books not returned.")
        return
    res = supabase.table("members").delete().eq("member_id", member_id).execute()
    print("Deleted:", res.data)

def list_members():
    res = supabase.table("members").select("*").execute()
    for m in res.data:
        print(m)
