def read_data():
    # les alle data fra fila rett utenfor her
    data = open('./../data/calculations.csv').read()
    return data

def read_transform_calculate_format():
    data = read_data()
    # transformer dataene til linjer
    lines = data.split('\n')
    # forbered total og rapport
    total = 0
    report = ''
    # iterer over alle linjer
    for line in lines:
        # hopp over første linje
        if line.startswith('X'): continue
        # vask bort linjeskift og splitt på komma
        cols = line.strip('\n').split(',')
        # skriv ut venstre side av regnestykket
        report += cols[0] + ' + ' + cols[1]
        # transformer tekst til tall
        x = int(cols[0])
        y = int(cols[1])
        # skriv ut høre side av regnestykket
        report += ' = ' + str(x + y) + '\n'
        # aggreger totalsum
        total += x + y
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

