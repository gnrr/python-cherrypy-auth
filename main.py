#! /usr/bin/env python
# -*- coding: utf-8 -*-

# python ./main.py

import cherrypy
import sqlite3

DBPATH = 'user.db'

HTML_LOGIN = '''
<html>
</body>
<H1>Login</H1>
<form action="check_login" method="post">
<table>
  <tr><th>Email address</th><td><input type="text" name="emailaddr" size="40"></td></tr>
  <tr><th>Password</th><td><input type="text" name="password" size="20"></td></tr>
 </table>
 <a><input type="submit" value="Send"><input type="reset" value="Clear"></a>
</form>
<p>or <a href="register">Register?</a></p>
</body>
</html>
'''

HTML_REGISTER = '''
<html>
</body>
<H1>Register</H1>
<form action="check_register" method="post">
<table>
  <tr><th>Email address</th><td><input type="text" name="emailaddr" size="40"></td></tr>
  <tr><th>Password</th><td><input type="text" name="password" size="20"></td></tr>
 </table>
 <a><input type="submit" value="Send"><input type="reset" value="Clear"></a>
</form>
<p>or <a href="index">Login?</a></p>
</body>
</html>
'''

HTML_LOGOUT = '''
<html>
</body>
<p>Now You've logged out. <a href="index">See you!</a></p>
</body>
</html>
'''

HTML_CHECK_LOGIN_OK = '''
<html>
</body>
<p>You've logged in. Enjoy!</p>
<p> Email address:%s</p>
<p> Password:     %s</p>
</body>
</html>
'''

HTML_CHECK_LOGIN_NG = '''
<html>
</body>
<p>Wrong Email address or Password. <a href="index">Try again?</a></p>
</body>
</html>
'''
HTML_CHECK_REGISTER_OK = '''
<html>
</body>
<p>You've registered just now. Enjoy!</p>
<p> Email address:%s</p>
<p> Password:     %s</p>
</body>
</html>
'''

HTML_CHECK_REGISTER_NG = '''
<html>
</body>
<p>The Email address is used already. <a href="register">Try again?</a></p>
</body>
</html>
'''

class Auth(object):
    def __init__(self):
        self.conn = sqlite3.connect(DBPATH)
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.conn.close()
        
    @cherrypy.expose
    def index(self):
        return HTML_LOGIN

    @cherrypy.expose
    def logout(self):
        return HTML_LOGOUT

    @cherrypy.expose
    def check_login(self, emailaddr, password):
        return HTML_CHECK_LOGIN_OK % (emailaddr, password)

    @cherrypy.expose
    def register(self):
        return HTML_REGISTER

    @cherrypy.expose
    def check_register(self, emailaddr, password):
        return HTML_CHECK_REGISTER_OK % (emailaddr, password)



##
if __name__ == '__main__':
    cherrypy.quickstart(Auth())
