from linked_link import LinkedLink


def main():
    linked_link = LinkedLink()
    linked_link.append(1)
    linked_link.append(2)
    linked_link.append(2)
    linked_link.append(3)
    linked_link.append(4)
    linked_link.add_first(0)
    linked_link.print_linked_list()
    print("#####")
    linked_link.remove(0)
    linked_link.remove(2)
    linked_link.print_linked_list()
    print("#####")
    print(linked_link.is_exist(0))
    print("#####")
    print(linked_link.to_array())
    print("#####")
    print(linked_link.length())
    print("#####")
    linked_link.clear()
    linked_link.print_linked_list()
    print("#####")
    print(linked_link.length())


if __name__ == "__main__":
    main()
