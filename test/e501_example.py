

# worked prior to logical line patch
t0 = ("test", "test", "test", "test", "test", "test", "test", "test", "test", "test", "test")

# fixed by logical line patch
t1 = ("test",
      "test", "test", "test", "test", "test", "test", "test", "test", "test", "test", "test")

# requires agressive
t2 = ("test", "test", "test", "test", "test", "test", "test", "test", "test", "test", "test",
      "test", "test", "test", "test", "test", "test", "test", "test", "test", "test", "test")

t3 = ("test", "test", "test", "test", "test", "test", "test", "test", "test",  # still fails on this
      "test", "test")
