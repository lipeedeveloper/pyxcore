// PyxCore Example: API de banco de dados tipo SQL/Mongo

fn main() {
    let db = db_connect("shop")
    let users = db_create_collection(db, "users")

    db_insert(users, "user:1", "Alice")
    db_insert(users, "user:2", "Bob")
    db_insert(users, "user:3", "Carol")

    let found = db_find(users, "user:2")
    if found != null {
        print("Found user: ")
        print(found)
    }

    let count = db_count(users)
    print("\nTotal users: ")
    print(count)

    db_update(users, "user:2", "Robert")
    let updated = db_query(users, "user:2")
    print("\nUpdated user: ")
    print(updated)

    let removed = db_delete(users, "user:1")
    if removed {
        print("\nDeleted user 1")
    }

    db_close(db)
}
