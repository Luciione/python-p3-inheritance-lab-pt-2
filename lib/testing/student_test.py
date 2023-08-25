from student import Student
from chatty_student import ChattyStudent

class TestStudent:
    def test_hello_method(self):
        student = Student("John", "Doe")
        assert student.hello() == "Hey there! I'm so excited to learn stuff."

    def test_raise_hand_method(self):
        student = Student("John", "Doe")
        assert student.raise_hand() == "Pick me!"

class TestChattyStudent:
    def test_hello_method(self):
        chatty_student = ChattyStudent("Jane", "Smith")
        expected_result = (
            "Hey there! I'm so excited to learn stuff. "
            "How are you doing today? I'm okay, but I'm kind of tired. "
            "Did you watch The Walking Dead last night? You didn't?! "
            "Oh man, it was so crazy! What, you don't want any spoilers? "
            "Okay well let me just tell you who died..."
        )
        assert chatty_student.hello() == expected_result

    def test_raise_hand_method(self):
        chatty_student = ChattyStudent("Jane", "Smith")
        expected_result = "Pick me!" * 10
        assert chatty_student.raise_hand() == expected_result
