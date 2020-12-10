from lecture_06.homework6.tasks.counter import instances_counter


def test_instances_counter():
    @instances_counter
    class User:
        pass

    assert User.get_created_instances() == 0
    user, _, _ = User(), User(), User()
    assert user.get_created_instances() == 3
    assert user.reset_instances_counter() == 3
    assert user.get_created_instances() == 0


def test_instances_counter_with_init_and_inheritance():
    @instances_counter
    class User:
        def __new__(cls, *args, **kwargs):
            print("I am in User new")
            return super().__new__(cls)

        def __init__(self, num):
            print("I am in User init")
            self.age = num

    user = User(34)
    assert user.age == 34

    class Admin(User):
        def __new__(cls, *args, **kwargs):
            print("I am in Admin new")
            return super().__new__(cls)

        def __init__(self, *args, **kwargs):
            print("I am in Admin init")
            super().__init__(*args, **kwargs)

    admin = Admin(50)
    assert admin.age == 50
    assert user.get_created_instances() == 1
    assert admin.get_created_instances() == 2
