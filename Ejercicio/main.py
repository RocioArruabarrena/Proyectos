from userbuilder import UserBuilder
from database import Database

def main():
    
    user1 = UserBuilder("rocio", "rocio@gmail.com").with_age(22).build()
    user2 = UserBuilder("micaela", "micaela@gmail.com").with_address("calle 123").build()

 
    db = Database()
    db.add_user(user1)
    db.add_user(user2)

   
    for user in db.list_users():
        print(user)

if __name__ == "__main__":
    main()
