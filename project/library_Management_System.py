import User
import Library

a = User.User()
a.registration(2013310045, "jongin")
a.user_info()

b = User.User()
b.registration(2014310045, "jin")
b.total_user_info()

c = Library.Library(2013310045)
