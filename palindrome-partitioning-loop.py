rest = "abcd"  # the set
considered = 0
parsings = [[""]]  # all the ways to group all the considered elements, where each
# parsing is a list and an element of parsings, and each parsing is a grouping of all the considered
# elements, with the last element being in question - this grouping hasnt been checked.

# to consider an element (grow the parsing), the questioned element can be tested to see if it is a group,
# letting you make a candidate group that is only the currently considered element, or the candiate group
# can grow to include this most recent step. All parsings must take this step, and all parsings can either
# put this step into a large group or make it its own group. (thus deciding the size of the most recent
# group, which varies from parsing to parsing)


considered = 1
cand = rest[0]
rest = rest[1:]  # the set
parsings = [[cand]]  # the last element of each parsing is the candidate

while rest:
    print()
    print("STARTING LOOP W VALUES")
    print("cand: ", cand)
    print("rest: ", rest)
    print("parsings: ", parsings)

    considered += 1
    cand = rest[0]
    rest = rest[1:]

    new_parsings = []
    for parsing in parsings:
        if parsing[-1] == parsing[-1][::-1]:
            new_parsing = [group for group in parsing] + [cand]
            print("new_parsing: ", new_parsing)

            new_parsings.append(new_parsing)

    for parsing in parsings:
        print("PARSING", parsing)
        print("parsing[-1]: ", parsing[-1])
        parsing[-1] = parsing[-1] + cand


    parsings.append(new_parsings)
    print("parsings: ", parsings)

print(parsings)