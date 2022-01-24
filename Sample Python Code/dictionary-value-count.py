def how_many(animals):
    counter = 0
    for item in animals.values():
        counter += len(item)

    return counter


def main():
    animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
    animals['d'] = ['donkey']
    animals['d'].append('dog')
    animals['d'].append('dingo')

    print(how_many(animals))


if __name__ == "__main__":
    main()
