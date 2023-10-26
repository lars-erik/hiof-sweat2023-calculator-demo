# gjør dette hvis det er denne .py-fila som ble kjørt
if __name__ == "__main__":
    # les alle data fra fila rett utenfor her
    data = open('./../data/calculations.csv').read()
    # transformer dataene til linjer
    lines = data.split('\n')
    # forbered total
    total = 0
    # iterer over alle linjer
    for line in lines:
        # hopp over første linje
        if line.startswith('X'): continue
        # vask bort linjeskift og splitt på komma
        cols = line.strip('\n').split(',')
        # skriv ut venstre side av regnestykket
        print(cols[0] + ' + ' + cols[1], end='')
        # transformer tekst til tall
        x = int(cols[0])
        y = int(cols[1])
        # skriv ut høre side av regnestykket
        print(' = ' + str(x + y))
        # aggreger totalsum
        total += x + y
    # skriv ut totalsum
    print('Total: ' + str(total))

