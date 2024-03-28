#!/usr/bin/python
if __name__ == "__main__":
    import hidden_4

    a = dir(hidden_4)

    fn = [name for name in a if not name.startswith('__')]

    for name in sorted(fn):
        print(name)
