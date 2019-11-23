# created by Scott "LittlemanSMG" Goes on DD/MM/YYYY


def main():
    print(f"Country\t\tWins\tYears\n"
          f"=======\t\t====\t=====")
    for key in sorted(teams.keys()):
        year = teams[key]['year']
        if key == 'Argentina':
            print(f"{key}\t{len(teams[key]['year'])}\t\t", end='')
            print(*year, sep=', ')
        else:
            print(f"{key}\t\t{len(teams[key]['year'])}\t\t", end='')
            print(*year, sep=', ')


if __name__ == "__main__":
    teams = {}
    with open('./world_cup_champions.txt', 'r') as file:
        for line in file.readlines():
            line = line.split(',')

            if line[1] not in teams.keys():
                teams[line[1]] = {'year': [line[0]]}
            else:
                teams[line[1]]['year'].append(line[0])

            if 'coach' not in teams.keys():
                teams[line[1]].update({'coach': line[2]})

            if 'capitan' not in teams.keys():
                teams[line[1]].update({'capitan': line[3]})
    main()
