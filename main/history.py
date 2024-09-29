from datetime import datetime

"""
Writes and reads history of application usage to the file.
History format is 'date-time: username: cat-fact-response'
"""
class History:
    HISTORY_FILE_NAME = "history.cat"

    def addRecord(self, info):
        self.file = open(self.HISTORY_FILE_NAME, "a")
        now = datetime.now()
        self.file.write(str(now) + ": " + info + "\n")
        self.file.close()

    def getHistory(self):
        self.file = open(self.HISTORY_FILE_NAME, "r")
        return self.file.read()