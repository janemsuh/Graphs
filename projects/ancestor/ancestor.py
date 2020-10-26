
def earliest_ancestor(ancestors, starting_node):
    ancestors_hash = {}

    for value, key in ancestors:
        if key in ancestors_hash:
            ancestors_hash[key].add(value)
        else:
            ancestors_hash[key] = set([value])

    if starting_node not in ancestors_hash:
        return -1

    stack = [starting_node]
    visited = set()
    earliest_ancestor = None

    while len(stack) > 0:
        current_node = stack.pop()

        if current_node not in visited:
            visited.add(current_node)

            if current_node in ancestors_hash:
                for ancestor in ancestors_hash[current_node]:
                    if ancestor not in ancestors_hash:
                        earliest_ancestor = ancestor
                    stack.append(ancestor)

    return earliest_ancestor