def read_transform_calculate_format():
    data = read_data()
    operations = parse_operations(data)
    total = calculate(operations)
    report = format_report(operations, total)
    return report


def read_data():
    # les alle data fra fila rett utenfor her
    data = open('./../data/calculations.csv').read()
    return data


def parse_operations(data):
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
        operations.append({'x': x, 'y': y})
    return operations


def format_report(operations, total):
    # forbered rapport
    report = ''
    # iterer over alle operasjoner
    for op in operations:
        # skriv ut regnestykket
        report += f"{op['x']} + {op['y']} = {op['subtotal']}\n"
    # skriv ut totalsum
    report += 'Total: ' + str(total)
    return report


def calculate(operations):
    # forbered total
    total = 0
    # iterer over alle operasjoner
    for op in operations:
        # beregn subtotal
        subtotal = op['x'] + op['y']
        op['subtotal'] = subtotal
        # aggreger totalsum
        total += subtotal
    return total


# gjør dette hvis det er denne .py-fila som ble kjørt
if __name__ == "__main__":
    print(read_transform_calculate_format())

