class Profile:
    id = 0
    email = ""
    name = ""
    role = ""

    def __init__(self, id , email , name ,  role ):
        self.id  = id
        self.email = email
        self.name = name
        self.role = role

    def __init__(self, name):
        self.name = name

