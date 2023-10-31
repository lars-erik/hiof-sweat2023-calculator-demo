class AsciiReporter:
    def format_report(self, aggregation):
        report = ''
        for op in aggregation.operations:
            report += f"{str(op)}\n"
        report += 'Total: ' + str(aggregation.total)
        return report
