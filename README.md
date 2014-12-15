# Fishrob - a partial implementation of Rob Pike's Structural Regexps

I was super impressed by [this
paper](http://doc.cat-v.org/bell_labs/structural_regexps/se.pdf), and I just
had to try messing with it a bit.  I found it because of this [blog
post](https://www.hackerschool.com/blog/62-paper-of-the-week-structural-regular-expressions)
at Hacker School.

Hopefully, this will be interesting to someone - it's nothing more than a start.

Here's a demo - the `debian_package_file` string is defined in demo.py.

```
# Extract groups of non-blank lines,
# Where the Section is 'non-free/web',
# Split into individual lines,
# Take the one that's the package name,
# And print it.
fishrob(debian_package_file) \
    .x(r'(.+\n)+') \
    .g(r'Section: non-free/web') \
    .x(r'.+\n') \
    .g(r'^Package:') \
    .p()
# Should print:
#   Package: album-data
#   Package: album
```

Compare it to Pike's example on page 5 (adapted to Debian Package files):

```
x/(.+\n)+/ g/Section: non-free\/web/ x/.*\n/ g/Package/p
```

Keep being awesome, Hacker School!
