from textnode import TextNode, TextType

def main():
    basic_thing = TextNode("this is some anchor text", TextType.LINK, "https://www.boot.dev")

    print("hello world")
    print(basic_thing)

if __name__ == "__main__":
    main()

