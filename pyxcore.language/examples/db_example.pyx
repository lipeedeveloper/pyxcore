// PyxCore Example: In-memory database usage

fn main() {
    let db = db_connect("shop")
    let users = db_create_collection(db, "users")

    db_insert(users, "user:1", "Alice")
    db_insert(users, "user:2", "Bob")
    db_insert(users, "user:3", "Carlos")

    let count = db_count(users)
    print("Users count: ")
    print(count)

    let found = db_find(users, "user:2")
    if found != null {
        print("Found user: ")
        print(found)
    }

    db_update(users, "user:2", "Robert")
    let updated = db_query(users, "user:2")
    print("\nUpdated: ")
    print(updated)

    let deleted = db_delete(users, "user:1")
    if deleted {
        print("\nDeleted user 1\n")
    }

    db_close(db)
}
