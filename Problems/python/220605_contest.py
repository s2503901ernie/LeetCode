class TextEditor:

    def __init__(self):
        self.c = ""
        self.p = -1

    def addText(self, text: str) -> None:
        left = self.c[:self.p+1]
        right = self.c[self.p+1:]
        self.c = left + text + right
        self.p += len(text)

    def deleteText(self, k: int) -> int:
        if self.p < k:
            self.c = self.c[self.p+1:]
            pos = self.p
            self.p = 0
            return min(pos, k)
        else:
            self.c = self.c[:self.p - k + 1] + self.c[self.p+1:]
            self.p -= k
            return k

    def cursorLeft(self, k: int) -> str:
        if self.p - k <= 0:
            self.p = 0
            return ""
        else:
            self.p -= k
            left = max(0, self.p - 10)
            return self.c[left:self.p + 1]

    def cursorRight(self, k: int) -> str:
        if self.p + k >= len(self.c):
            self.p = len(self.c) - 1
            left = max(0, self.p - 9)
            return self.c[left:]
        else:
            self.p += k
            left = max(0, self.p - 10)
            return self.c[left:self.p]


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)