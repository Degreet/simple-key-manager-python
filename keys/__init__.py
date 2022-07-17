from msilib import datasizemask
import sqlite3

class KeyManager:
    db = sqlite3.connect("keys.db")
    cursor = db.cursor()

    def createTable(self):
        self.cursor.execute("CREATE TABLE `keys` (password text, website text)")

    def hasKey(self):
        mainKey = self.cursor.execute("SELECT * FROM `keys` WHERE `website` = 'main'").fetchone()
        self.mainKey = mainKey[0]
        return bool(mainKey)

    def checkKey(self, key):
        if not self.mainKey:
            return False
        
        return self.mainKey == key
    
    def saveKey(self, key):
        self.newKey(key, "main")
        self.db.commit()

    def newKey(self, key, website):
        self.cursor.execute("INSERT INTO `keys` VALUES (?, ?)", (key, website))
        self.db.commit()

    def getKey(self, website):
        websiteKey = self.cursor.execute("SELECT password FROM `keys` WHERE website=?", (website,)).fetchone()

        if not websiteKey:
            return False
        
        return websiteKey[0]

    def close(self):
        self.db.close()
