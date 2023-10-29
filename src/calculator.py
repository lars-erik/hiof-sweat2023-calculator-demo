def read_data():
    # les alle data fra fila rett utenfor her
    data = open('./../data/calculations.csv').read()
    return data

def read_transform_calculate_format():
    data = read_data()
    # transformer dataene til linjer
    lines = data.split('\n')

    # forbered operasjoner
    operations = []
    # iterer over alle linjer
    for line in lines:
        # hopp over første linje
        if line.startswith('X'): continue
        # splitt på komma
        cols = line.split(',')
        # transformer tekst til tall
        x = int(cols[0])
        y = int(cols[1])
        # legg til operasjon
        operations.append({'x':x, 'y':y})

    # forbered total og rapport
    total = 0
    report = ''
    # iterer over alle operasjoner
    for op in operations:
        # aggreger totalsum
        total += op['x'] + op['y']
        # skriv ut venstre side av regnestykket
        report += f"{op['x']} + {op['y']}"
        # skriv ut høyre side av regnestykket
        report += f" = {op['x'] + op['y']}\n"

    # skriv ut totalsum
    report += 'Total: ' + str(total)
    return report


def read_data():
    # les alle data fra fila rett utenfor her
    data = open('./../data/calculations.csv').read()
    return data


# gjør dette hvis det er denne .py-fila som ble kjørt
if __name__ == "__main__":
    print(read_transform_calculate_format())

