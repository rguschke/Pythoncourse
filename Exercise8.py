# coding=utf-8
print "exercise8"
#printing printing printing

formatter = " %r %r %r %r "

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, True, False)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "If you had this thing.",
    "that you could type up right.",
    "But it didn't sing.",
    "so i said Goodnight"
)
