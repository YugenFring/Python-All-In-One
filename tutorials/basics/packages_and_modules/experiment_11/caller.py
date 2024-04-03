# Import statement with sub pakceg name.
import pkg.sub_pkg1.mod1
pkg.sub_pkg1.mod1.do_work()


from pkg.sub_pkg1 import mod2
mod2.do_work()


from pkg.sub_pkg2.mod3 import do_work
do_work()