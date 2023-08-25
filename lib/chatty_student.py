from student import Student

class ChattyStudent(Student):
    def hello(self):
        parent_hello = super().hello()
        chatty_phrase = (
            "How are you doing today? I'm okay, but I'm kind of tired. "
            "Did you watch The Walking Dead last night? You didn't?! "
            "Oh man, it was so crazy! What, you don't want any spoilers? "
            "Okay well let me just tell you who died..."
        )
        return f"{parent_hello} {chatty_phrase}"

    def raise_hand(self):
        return super().raise_hand() * 10
