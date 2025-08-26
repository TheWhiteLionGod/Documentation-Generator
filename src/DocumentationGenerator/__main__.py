from DocumentationGenerator import load_generator


def main():
    generator = load_generator()
    # Each subpackage should expose a `main()` in its __main__.py
    generator.main()


if __name__ == "__main__":
    main()
