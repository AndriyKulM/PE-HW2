class Profile:
    """
    Create regular class taking 8 params on init - name, last_name, phone_number, address, email, birthday, age, sex
    Override a printable string representation of Profile class and return: list of the params mentioned above
    """
    def __init__(self, name, last_name, phone_number, address, email, birthday, age, sex):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age
        self.sex = sex
    def repr_of_attr(self):
        return list(self.__dict__.values())
        
    
profile = Profile('Bob', 'Smith', '+380467889789', 'NY - 1st Avenue 25', 'bsmith@gmail.com', '12-08-1990', 32, 'mail')
print(profile.repr_of_attr())