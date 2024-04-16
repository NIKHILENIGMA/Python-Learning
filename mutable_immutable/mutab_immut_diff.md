When you first do:

```python
username = "nikhil"
print(username)
# output: "nikhil"
```

- You create a string object `"nikhil"` and assign it to the variable `username`.
- The variable `username` now references the string object `"nikhil"`.

When you later assign a new string to the same variable:

```python
username = "sahil"
print(username)
# output: "sahil"
```

- You are not changing the string object `"nikhil"` itself (which is immutable); instead, you are creating a new string object `"sahil"` and updating the variable `username` to reference this new object.
- The original string `"nikhil"` remains unchanged in memory until it's no longer referenced and is eventually cleaned up by Python's garbage collector.
- The key point here is that immutability refers to the inability to change the object that a variable references, not the inability to change which object a variable references.
- In your example, the strings `"nikhil"` and `"sahil"` are both immutable (you cannot change their content), but the variable `username` can be reassigned to reference different string objects.