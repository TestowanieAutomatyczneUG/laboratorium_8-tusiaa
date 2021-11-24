class Password:
    def ValidPassword(self, password):
        numbersaray = ['0','1','2','3','4','5','6','7','8','9']
        numbers = 0

        if type(password) != str:
            raise Exception('Wrong type.')
        if len(password) < 8:
            return False
        if password.lower() == password:
            return False
        if password.isalnum():
            return False
        for i in range(0, len(numbersaray)):
            if password.find(numbersaray[i]) != -1:
                numbers += 1
        if numbers == 0:
            return False
        return True